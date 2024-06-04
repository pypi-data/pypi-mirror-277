# SPDX-License-Identifier: BSD-2-Clause-Patent
# SPDX-FileCopyrightText: 2024 Syslinbit <contact@syslinbit.com>

import argparse
import getpass
import os
import sys
import subprocess

from nost import config
from nost.logger import default_log_level, logger
from nost.utils import encryption


def nostvault():
    parser = argparse.ArgumentParser(
        description="nost-vault - manage local vaults"
    )

    parser.add_argument("-d", "--debug",
                        action="store_const", const="debug", dest="log_level",
                        help="Enable debug logging")
    parser.add_argument("-l", "--log-level",
                        choices=["debug", "info", "warning", "error",
                                 "critical"],
                        default="%s" % (default_log_level),
                        help="Set log level (default: %s)" % default_log_level)
    parser.add_argument("-L", "--log-file",
                        dest="filename", nargs=1,
                        help="Log to file")

    subparser = parser.add_subparsers(
        title="subcommands",
        help="additional help")

    vaultinitparser = subparser.add_parser("init",
                                           help="Create local vault")
    vaultinitparser.add_argument("vaultname",
                                 metavar="vaultname|all",
                                 help="Local vault name")
    vaultinitparser.set_defaults(func=vault_init)

    vaultaddparser = subparser.add_parser(
        "add-password",
        help="Encrypt a password in a local vault"
    )
    vaultaddparser.add_argument("vaultname", help="Local vault name")
    vaultaddparser.add_argument(
        "service",
        help="Service name to which the password may connect"
    )
    vaultaddparser.add_argument(
        "user",
        help="Username to which the password should match"
    )
    vaultaddparser.set_defaults(func=vault_add_password)

    if len(sys.argv[1:]) == 0:
        # Exit if no command is provided
        parser.print_usage()
        sys.exit(1)

    args = parser.parse_args(sys.argv[1:])

    if args.log_level:
        logger.setLevelStr(args.log_level)

    if args.filename:
        logger.toFile(args.filename[0])

    return args.func(args)


def vault_add_password(args):
    try:
        config["vaults"][args.vaultname]["mode"]
    except KeyError as e:
        logger.error(f"Failed to get vault {args.vaultname}"
                     f" in nost configuration ({e})")
        return 1

    if config["vaults"][args.vaultname]["mode"] == "pass":
        add_password_pass(args)
    else:
        add_password(args)


def add_password_pass(args):
    vaultname = args.vaultname
    service = args.service
    username = args.user

    try:
        config["vaults"][vaultname]
    except KeyError as e:
        logger.error(f"Failed to get vault {vaultname} in nost configuration"
                     f"({str(e)})")
        return 1

    env = os.environ
    if config["vaults"][vaultname]["path"] is not None:
        env["PASSWORD_STORE_DIR"] = config["vaults"][vaultname]["path"]

    subprocess.run(
        ["pass", "insert", f"{service}/{username}"],
        env=env
    )

    return


def add_password(args):
    vaultname = args.vaultname
    service = args.service
    username = args.user

    try:
        vaultconfig = config["vaults"][vaultname]
        path = vaultconfig["path"]
        vaultencryption = vaultconfig["encryption"]
    except KeyError as e:
        logger.error(f"Failed to get vault {vaultname} in nost configuration"
                     f"({str(e)})")
        return 1

    password = getpass.getpass('Enter your password :')
    confirm = getpass.getpass('Confirm your password :')

    if password != confirm:
        logger.error("Error during password confirmation. Abort password"
                     "addition")
        return 1

    if vaultencryption == "fernet":
        try:
            keypath = vaultconfig["keypath"]
        except KeyError as e:
            logger.error(
                f"No keypath for vault {vaultname} in nost configuration"
                f"({str(e)})")
            return 1

        line = encryption.encrypt_line_fernet(
            f'{username} {password}'.encode(),
            keypath
        )
    elif vaultencryption == "b64":
        line = encryption.encrypt_line_b64(
            f'{username} {password}'.encode()
        )
    else:
        confirm = input(
            "Password will not be encrypted, continue ? [yN]"
        ).lower()
        if not confirm:
            logger.warning("Password not encrypted")
            line = f'{username} {password}'
            return 0

    fullpath = f"{path}/{service}"
    if os.path.isfile(fullpath):
        logger.debug(
            f"Erasing existing {service} in vault {vaultname}")
        with open(fullpath, 'ab') as file:
            file.write(line)
    else:
        with open(fullpath, 'xb') as file:
            file.write(line)
    logger.info(f"User {username} added to vault {vaultname} for {service}")

    return 0


def vault_init(args):
    vaultname = args.vaultname

    if vaultname == "all":
        return vault_create_all()
    else:
        if config["vaults"][vaultname]["mode"] == "pass":
            return vault_create_pass(vaultname)
        else:
            return vault_create(vaultname)


def vault_create_pass(vaultname):
    try:
        vaultconfig = config["vaults"][vaultname]
        path = vaultconfig["path"]
    except KeyError as e:
        logger.error(f"Failed to get vault {vaultname} in nost configuration"
                     f"({str(e)}")
        return 1

    env = os.environ
    env["PASSWORD_STORE_DIR"] = path

    gpg_id = getpass.getpass('Enter your GPG key ID :')
    proc = subprocess.run(
        ["pass", "init", f"{gpg_id}"],
        env=env
    )

    if proc.returncode == 0:
        logger.info(f"Vault {vaultname} created at {path}")
    else:
        logger.error(f"Failed to create vault {vaultname}")
        return 1

    return 0


def vault_create(vaultname):
    try:
        vaultconfig = config["vaults"][vaultname]
        path = vaultconfig["path"]
        vaultencryption = vaultconfig["encryption"]
    except KeyError as e:
        logger.error(f"Failed to get vault {vaultname} in nost configuration"
                     f"({str(e)}")
        return 1

    try:
        os.makedirs(path, mode=0o770)
    except (FileExistsError, PermissionError) as e:
        logger.error(str(e))
        return 1

    if vaultencryption == "fernet":
        try:
            keypath = vaultconfig["keypath"]
        except KeyError as e:
            logger.error(
                f"No keypath for vault {vaultname} in nost configuration"
                f"({str(e)}")
            return 1

        if os.path.exists(keypath):
            logger.warning(f"Key already exist: {keypath}")
        else:
            encryption.create_fernet_key(keypath)

    logger.info(f"Vault {vaultname} created at {path}")
    return 0


def vault_create_all():
    if not ("vaults" in config and "order" in config["vaults"]):
        logger.error("No vaults defined in nost configuration")

    vaults = config["vaults"]["order"]
    res = 0

    for v in vaults:
        if "mode" in config["vaults"][v] \
           and config["vaults"][v]["mode"] == "local":
            res += vault_create(v)
        elif "mode" in config["vaults"][v] \
             and config["vaults"][v]["mode"] == "pass":
            res += vault_create_pass(v)

    return res
