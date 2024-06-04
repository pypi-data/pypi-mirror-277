# SPDX-License-Identifier: BSD-2-Clause-Patent
# SPDX-FileCopyrightText: 2023 Syslinbit <contact@syslinbit.com>

"""Git plugin, to fetch git repository"""


import subprocess

from nost.plugins import Plugin


class Git(Plugin):
    """Git plugin, to fetch git repository.

    :param name: Name of the sevice to fetch with current plugin
    :param host: Address to fetch data from
    :param cachedir: Path to store data locally before processing
    :param kwargs: Other configuration, from service description (.yml)
    :type name: String
    :type host: String
    :type cachedir: String
    :type kwargs: Dict
    """

    def do_sync(self, credentials=None, backend=None, clean=True, **kwargs):
        """Fetch repository

        :param credentials: Default None.
            Access to repository must be checked ahead.
        :param backend: Backend object to use.
        :param clean: Default True. Remove data from cache directory.
        :param kwargs: Not used with this plugin.
        :type credentials: None
        :type backend: Backend
        :type clean: Boolean
        :type kwargs: None
        """

        proc = subprocess.Popen(
            ["git", "clone", "--mirror", self.source_path],
            stderr=subprocess.PIPE
        )
        error = proc.communicate()
        code = proc.returncode

        if not code:
            self.logger.info(
                f"Service {self.service_name} : git clone succeded"
            )

            if backend is not None:
                backend.process(self.service_name, self.cache_dir)

                if hasattr(self, "rotation"):
                    backend.do_rotate(self.service_name, self.rotation)
                else:
                    backend.do_rotate(self.service_name)
            else:
                self.logger.info("Sync without processing")

            if clean:
                self.do_clean_cache()
        else:
            self.logger.error(
                f"Service {self.service_name} : git clone failed.\
                \n{error[1].decode()}"
            )
            raise (error)

        return
