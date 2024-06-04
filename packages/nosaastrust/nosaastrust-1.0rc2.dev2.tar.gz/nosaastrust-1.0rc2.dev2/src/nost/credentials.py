# SPDX-License-Identifier: BSD-2-Clause-Patent
# SPDX-FileCopyrightText: 2023 Syslinbit <contact@syslinbit.com>

"""Credentials classes"""


from nost.vaults import getVaults
from nost.logger import logger


class Credentials():
    """Abstract class describing credentials management.
    This class is inherited by every instanciable credentials classes.

    :param service_name: Name of the targeted service
    :param auth:
    :param kwargs:

    :type service_name: String
    :type auth: Boolean
    :type kwargs: Dict
    """

    def __init__(self, service_name, auth=None, **kwargs):
        """Contructor method
        """

        self.service_name = service_name
        self.cred = auth
        self.vaults = getVaults()

    def auth(self, **kwargs):
        """Authentification method
        """

        raise NotImplementedError("The method auth has not been implemented")


class Token(Credentials):
    """Credential class to handle token

    :param token: Token to store
    """

    def __init__(self, token):
        """Constructor method
        """

        self.token = token


class Password(Credentials):
    """Credential class to handle password
    """
    def auth(self, user=None, **kwargs):
        """
        Look for user or self.auth["user"] password. Looks into attributes and
        vaults.

        :param user: Username
        :param kwargs:

        :type user: String
        :type kwargs: Dict

        :return: Username and password
        :rtype: Tuple
        """
        if user is None:
            if self.cred is None or "user" not in self.cred:
                raise NotImplementedError("User not defined")
            else:
                user = self.cred["user"]

        if user == self.cred["user"] and "password" in self.cred:
            return user, self.cred["password"]

        if self.vaults is not None:
            for v in self.vaults:
                p = v.retrieve(self.service_name, user)
                if p is not None:
                    return user, p

        logger.warning(f"User credential not found ({user})")

        return None, None
