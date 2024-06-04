#!/bin/env python3
# SPDX-License-Identifier: BSD-2-Clause-Patent
# SPDX-FileCopyrightText: 2023 Syslinbit <contact@syslinbit.com>
"""NoSaasTrust entrypoint"""


import argparse
import glob
import importlib
import inspect
import os
import shutil
import signal
import sys
import tempfile
import yaml

from nost import config
from nost.plugins import Plugin
from nost.logger import default_log_level, logger
from nost.backend import getBackend
from nost._version import __version__

#: Prefix given to cache directories
CACHE_SYNC_PREFIX = "sync_"


def load_plugin(p):
    """
    Finds plugin class with plugin filename
    Returns tuple of plugin name and its corresponding class
    """
    namespace = importlib.import_module(f"nostplugins.{p}")
    cls = inspect.getmembers(namespace, inspect.isclass)
    return {
        p: c[1]
        for c in cls
        if issubclass(c[1], Plugin) and c[1] != Plugin
    }


def read_yml(filepath):
    """
    Reads and parses Yaml input
    """
    with open(filepath, "r") as file:
        description = yaml.safe_load(file)
        return description


def sync_initialize_cache():
    """
    Create a temporary directory for synchronized data
    """
    return tempfile.mkdtemp(prefix="sync_", dir=config["cache"]["path"])


def sync_clean_cache():
    """
    Clean sync cache
    """
    for d in glob.glob("{}/{}*".format(config["cache"]["path"],
                                       CACHE_SYNC_PREFIX)):
        shutil.rmtree(d)


def sync(args, backend=None):
    klasses = {}

    try:
        if not os.path.isfile(args.description):
            err = f"Desciption is not a file: {args.description}"
            logger.error(err)
            raise FileNotFoundError(err)
        description = read_yml(args.description)
    except FileNotFoundError as e:
        logger.error(f"Could not read description: {e}")
        raise e

    try:
        cachedir = sync_initialize_cache()
    except FileNotFoundError as e:
        logger.error(f"Cache directory cannot be reached: {e}")
        raise e

    for service_name, service_conf in description["services"].items():
        if service_name in description["backuplist"]:
            klasses.update(load_plugin(service_conf["type"]))

    for service_name in description["backuplist"]:
        try:
            service_conf = description["services"][service_name]
            p = klasses[service_conf["type"]](service_name,
                                              cachedir=cachedir,
                                              **service_conf)
        except KeyError as e:
            logger.error(f"Could not find key {e} in description")
            raise (e)

        try:
            service_dir = os.path.join(cachedir, service_name)
            os.makedirs(service_dir, mode=0o700)
        except FileExistsError as e:
            logger.error(f"Directory already exists in cache: {service_name}")
            raise (e)

        p.do_configure(**service_conf)
        cred = p.do_authenticate(**service_conf)
        p.do_prepare(cred)
        os.chdir(service_dir)
        p.do_sync(cred, backend, **service_conf)

    sync_clean_cache()


def list_data_text(args, backend=None):
    services = backend.list_data()
    for el in services:
        print(f'{el["name"]} {el["time"]} {el["id"]}')


def list_data_human(args, backend=None):
    services = backend.list_data()
    if services is not None:
        print(
            f'{"-" * 90}\n'
            f'|{" ":40}Archives{" ":40}|\n'
            f'{"-" * 90}\n'
            f'| {" ":5}Name{" ":5} | {" ":8}Timestamp {" ":8} '
            f'| {" ":19}ID{" ":19} |\n'
            f'{"-" * 90}\n'
        )
        for el in services:
            print(f'| {el["name"]:14} | {el["time"]:26} | {el["id"]:40} |\n')
    else:
        logger.info("No archives found.")
    return


def list_data(args, backend=None):
    if args.form == "human":
        return list_data_human(args, backend)
    if args.form == "text":
        return list_data_text(args, backend)

    raise KeyError(f"Incorrect format {args.form}")


def retrieve(args, backend=None):
    if backend is None:
        logger.info("No backend provided, nothing to retrieve")
        return

    if args.destination:
        backend.retrieve(args.ID, dest=args.destination)
    else:
        backend.retrieve(args.ID)
    return


def delete(args, backend=None):
    backend.delete(args.ID)
    return


def create_parser():
    parser = argparse.ArgumentParser(
        description='nost - tools to backup backups'
    )

    parser.add_argument("--version", action="store_true",
                        help="Show the version and exit")
    parser.add_argument("-d", "--debug",
                        action="store_const", const="debug", dest="log_level",
                        help="Enable debug logging (deprecated, use "
                             "--log-level debug).")
    parser.add_argument("-l", "--log-level",
                        choices=["debug", "info", "warning", "error",
                                 "critical"],
                        default="%s" % (default_log_level),
                        help="Set log level (default: %s)" % default_log_level)
    parser.add_argument("-L", "--log-file",
                        dest="filename", nargs=1,
                        help="Log to file")
    parser.set_defaults(func=None)

    subparser = parser.add_subparsers(title="subcommands",
                                      description="valid subcommands",
                                      help="additional help")

    syncparser = subparser.add_parser(
        "sync", help="Fetch the targets and store the data"
    )
    syncparser.add_argument("description", help="YAML description file")
    syncparser.set_defaults(func=sync)

    listparser = subparser.add_parser("list", help="List stored data")
    listparser.add_argument("-f", "--format", dest="form",
                            help="Output format",
                            choices=["human", "text"], default="human")
    listparser.set_defaults(func=list_data)

    retrieveparser = subparser.add_parser(
        "retrieve", help="Retrieve stored data"
    )
    retrieveparser.add_argument("ID", help="Archive ID")
    retrieveparser.add_argument("-D", "--destination",
                                dest="destination", required=False,
                                help="Destination")
    retrieveparser.set_defaults(func=retrieve)

    deleteparser = subparser.add_parser("delete", help="Delete stored data")
    deleteparser.add_argument("ID", help="Archive ID")
    deleteparser.set_defaults(func=delete)

    return parser


def main(argv):
    parser = create_parser()
    args = parser.parse_args(argv)

    if args.version:
        print("NoSaasTrust, " + __version__)
        sys.exit(0)

    if args.func is None:
        parser.print_help()
        sys.exit(1)

    if args.log_level:
        logger.setLevelStr(args.log_level)

    if args.filename:
        logger.toFile(args.filename[0])

    try:
        backend = getBackend()
    except Exception as e:
        logger.error(f"Failed to initialize the backend: {e}")
        sys.exit(1)

    try:
        args.func(args, backend=backend)
    except Exception as e:
        logger.error("Failed: {}".format(e))
        sys.exit(1)


def interruption(signum, frame):
    signame = signal.Signals(signum).name
    logger.warn(f'Signal handler called with signal {signame}')
    sync_clean_cache()
    sys.exit(0)


def entrypoint():
    signal.signal(signal.SIGINT, interruption)
    signal.signal(signal.SIGTERM, interruption)

    main(sys.argv[1:])
