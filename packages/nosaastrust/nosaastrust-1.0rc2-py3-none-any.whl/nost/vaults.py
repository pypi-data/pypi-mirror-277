# SPDX-License-Identifier: BSD-2-Clause-Patent
# SPDX-FileCopyrightText: 2023 Syslinbit <contact@syslinbit.com>

"""Vault management"""


import os
import base64
from cryptography.fernet import Fernet
import subprocess
import sys

from nost.logger import logger
from nost import config


vaults = None


class Vault():
    """Abstract class describing vaults main methods.
    This class is inherited by every instanciable vaults.
    """
    def __init__(self, **kwargs):
        return

    def retrieve(self, service_name, username):
        """Retrieve password for a given service and username.

        :param service_name: Name of the targeted service
        :param username: Username
        :type service_name: String
        :type username: String
        """
        raise NotImplementedError()


class LocalVault(Vault):
    """Vault class to handle local vault

    :param path: Path to vault folder
    :param encryption: Type of encryption (fernet, b64)
    :param kwargs: Additionnal information
    :type path: String
    :type encryption: String
    :type kwargs: Dict
    """

    def __init__(self, path="", encryption=None, **kwargs):
        """Constructor method
        """

        self.path = path
        self.encryption = encryption

        if self.encryption == "fernet":
            self.fernet_key_path = kwargs["keypath"]

        return

    def decrypt_line(self, line):
        """Decrypt one line

        :param line: Encrypted line found in vault
        :type line: String

        :return: Decrypted line
        :rtype: String
        """
        match self.encryption:
            case "b64":
                return base64.b64decode(line).decode("utf-8").split()
            case "fernet":
                with open(self.fernet_key_path, 'rb') as filekey:
                    key = filekey.read()
                    fernet = Fernet(key)
                return fernet.decrypt(line).decode("utf-8").split()
            case None:
                return line.split()

    def retrieve(self, service_name, username):
        """Retrieve password for a given service and username.

        :param service_name: Name of the targeted service
        :param username: Username
        :type service_name: String
        :type username: String

        :return: Password found
        :rtype: String
        """
        path = os.path.join(self.path, f"{service_name}")

        if os.path.exists(path):
            with open(path, 'rb') as file:
                for line in file.readlines():
                    if line.decode("utf-8") != '\n':
                        try:
                            u, p = self.decrypt_line(
                                line.decode("utf-8").strip()
                            )
                            if u == username:
                                return p
                        except Exception as e:
                            logger.error("Local vault file unreadable.")
                            raise (e)
        else:
            return None


class PasswordStoreVault(Vault):
    def __init__(self, path="", subpass="", **kwargs):
        self.path = os.path.expanduser(path)
        self.subpass = subpass

    def retrieve(self, service_name, username):
        """Retrieve password for a given service and username.

        :param service_name: Name of the targeted service
        :param username: Username
        :type service_name: String
        :type username: String
        """
        env = os.environ
        if self.path != "":
            env["PASSWORD_STORE_DIR"] = self.path

        res = subprocess.run(
            ["pass", f"{self.subpass}/{service_name}/{username}"],
            capture_output=True,
            env=env
        )

        if res.returncode != 0:
            return None

        return res.stdout.strip().decode("utf-8")


class BitwardenVault(Vault):
    """Remote vault using Bitwarden
    """
    pass


#: Vault type mapping
VAULTS = {
    "local": LocalVault,
    "bitwarden": BitwardenVault,
    "pass": PasswordStoreVault,
}


def instanciate_vault(mode=None, **kwargs):
    """
    Instanciate vault of class given by mode
    """
    if mode in VAULTS:
        return VAULTS[mode](**kwargs)


def init_vaults():
    vaults = []
    for v in config["vaults"]["order"]:
        if v in config["vaults"]:
            vaults.append(instanciate_vault(**config["vaults"][v]))

    return vaults


def getVaults():
    return vaults


if vaults is None:
    try:
        vaults = init_vaults()
    except Exception as e:
        print(e, file=sys.stderr)
        vaults = None
