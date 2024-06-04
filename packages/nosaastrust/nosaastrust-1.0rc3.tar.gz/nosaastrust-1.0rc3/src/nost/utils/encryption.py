# SPDX-License-Identifier: BSD-2-Clause-Patent
# SPDX-FileCopyrightText: 2023 Syslinbit <contact@syslinbit.com>

"""
Encryption helpers
"""


import os
import base64
from cryptography.fernet import Fernet


# Symmetric key
def create_fernet_key(path):
    """Generates a fernet key (symmetric key) and creates
    directories mentionned in the path argument if not found.

    :param path: Path to store the key
    :type path: String
    """

    key = Fernet.generate_key()

    if not os.path.isdir('/'.join(path.split("/")[:-1])):
        os.makedirs('/'.join(path.split("/")[:-1]))

    if os.path.isfile(path):
        print("Fernet key already exists")
        return
    else:
        with open(path, 'wb') as filekey:
            filekey.write(key)

    return


# Encrypt line
def encrypt_line_fernet(line, keypath):
    """Encrypt a line with fernet algorithm.

    :param line: String to encrypt
    :param keypath: Location of the fernet key to use
    :type line: String
    :type keypath: String

    :return: The string given as line argument but
        encrypted with the fernet key stored in keypath.
    :rtype: Bytes
    """

    with open(keypath, 'rb') as filekey:
        key = filekey.read()

    fernet = Fernet(key)
    return fernet.encrypt(line + str.encode("\n"))


def encrypt_line_b64(line):
    """Encrypt a line in base64.

    :param line: String to encrypt
    :type line: String

    :return: The string given as line argument but
        encrypted in base64.
    :rtype: Bytes
    """

    return base64.b64encode(line + str.encode("\n"))


# Encrypt file
def encrypt_file_fernet(filepath, keypath):
    """Encrypt a file with fernet algorithm.

    :param filepath: Location of the file to encrypt
    :param keypath: Location of the fernet key to use
    :type filepath: String
    :type keypath: String
    """

    with open(filepath, 'rb') as file:
        original = file.readlines()

    with open(filepath, 'wb') as encrypted_file:
        for line in original:
            encrypted_file.write(encrypt_line_fernet(line, keypath))

    return


def encrypt_file_b64(filepath):
    """Encrypt a file in base64.

    :param filepath: Location of the file to encrypt
    :type filepath: String
    """

    with open(filepath, 'rb') as file:
        original = file.readlines()

    with open(filepath, 'wb') as encrypted_file:
        for line in original:
            encrypted_file.write(encrypt_line_b64(line))

    return
