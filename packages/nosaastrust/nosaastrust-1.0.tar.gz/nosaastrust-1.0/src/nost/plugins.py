# SPDX-License-Identifier: BSD-2-Clause-Patent
# SPDX-FileCopyrightText: 2023 Syslinbit <contact@syslinbit.com>

"""Abstract class for plugin creation"""

import os
import subprocess

from nost.logger import logger
from nost import config


class Plugin():
    """Abstract class describing plugins main methods.
    This class is inherited by every instanciable plugin.

    :param name: Name of the sevice to fetch with current plugin
    :param host: Address to fetch data from
    :param cachedir: Path to store data locally before processing
    :param rotation: Specify when rotations should be made
    :param kwargs: Other configuration, from service description (.yml)
    :type name: String
    :type host: String
    :type cachedir: String
    :type rotation: Dict
    :type kwargs: Dict
    """

    def __init__(self, name,
                 host=None, cachedir=None, rotation=None, **kwargs):
        """Constructor method
        """

        self.service_name = name
        self.logger = logger

        try:
            self.cache_dir = f'{cachedir}/{name}'
            self.source_host = host
        except KeyError as e:
            self.logger.error(f"Description is missing {e}")
            raise (e)

        self.rotation = rotation

        self.ssh_key_dir = \
            config["general"].get("ssh_key_dir",
                                  os.path.join(os.environ["HOME"], ".ssh"))

        return

    def do_configure(self, **kwargs):
        """Configure plugin
        """
        pass

    def do_authenticate(self, **kwargs):
        """Get authentification information
        """
        return kwargs

    def do_prepare(self, cred):
        """Prepare data before backend processing
        """
        pass

    def do_sync(self, credentials=None, backend=None, clean=True):
        """Fetch data

        :param credentials: Authentification information
        :param backend: Backend object to use
        :param clean: If set to true,
            empty cache folder after backend processing
        :type credentials: Credentials
        :type backend: Backend
        :type clean: Boolean
        """
        raise NotImplementedError

    def do_postsync(self):
        """Post synchronisation operation
        """
        pass

    def do_clean_cache(self):
        """Empty cache folder
        """

        proc = subprocess.Popen(['rm', '-rf', self.cache_dir])

        error = proc.communicate()
        code = proc.returncode

        if not code:
            self.logger.info(f"{self.service_name} cache emptied.")
        else:
            self.logger.error("Empting cache failed.")
            raise (error)

        return
