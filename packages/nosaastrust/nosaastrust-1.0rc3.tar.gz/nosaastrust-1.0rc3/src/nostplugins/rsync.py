# SPDX-License-Identifier: BSD-2-Clause-Patent
# SPDX-FileCopyrightText: 2023 Syslinbit <contact@syslinbit.com>

"""RSYNC plugin, to fetch data through SSH"""


import os
import subprocess


from nost.plugins import Plugin


class RSYNC(Plugin):
    """RSYNC plugin, to fetch data through SSH.

    :param args: Initial argument used in plugin instanciation
    :param path: Optional path to specify the path on server
    :param files: Optional list to specify files for download
    :param kwargs: Additionnal information of the targeted service (.yml)
        Use to get ssh key path.

    :type args: List
    :type path: String
    :type files: List
    :type kwargs: Dict
    """

    def __init__(self, *args, path="", files=None, **kwargs):
        """Constructor method
        """
        super().__init__(*args, **kwargs)

        self.source_path = path
        self.files = files

        self.extra_sources = []

        if self.source_host == "local":
            self.source = self.source_path
        else:
            if self.files is None:
                self.source = f'{self.source_host}:{self.source_path}'
            else:
                s = os.path.join(self.source_path, self.files[0])
                self.source = f'{self.source_host}:{s}'
                for f in self.files[1:]:
                    self.extra_sources.append(
                        ":" + os.path.join(self.source_path, f)
                    )

            if "auth" in kwargs and "keyname" in kwargs["auth"]:
                self.key = kwargs["auth"]["keyname"] or ""
        return

    def do_sync(self, credentials=None, backend=None, clean=True, **kwargs):
        """Fetch data of given service through SSH.

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

        if hasattr(self, "ssh_key_dir") and hasattr(self, "key"):
            command = [
                'rsync',
                '-e',
                f'ssh -i {self.ssh_key_dir}/{self.key}'
                f' -o "StrictHostKeyChecking=no"',
                '-a',
                ]
        else:
            command = [
                'rsync',
                '-a',
            ]

        command.append(f'{self.source}')
        command += self.extra_sources
        command.append(f'{self.cache_dir}')

        self.logger.debug(f'Running command: {" ".join(command)}')
        proc = subprocess.Popen(command, stderr=subprocess.PIPE)
        error = proc.communicate()
        code = proc.returncode

        if not code:
            self.logger.info(
                f"Service {self.service_name} sync succeded"
            )
            if backend is not None:

                if backend is not None:
                    backend.process(self.service_name, self.cache_dir)

                if hasattr(self, "rotation"):
                    backend.do_rotate(self.service_name, self.rotation)
                else:
                    backend.do_rotate(self.service_name)
            else:
                self.logger.info("Sync without processing")
        else:
            self.logger.error(
                f"Service {self.service_name} sync failed.\n{error[1].decode()}"
            )

        if clean:
            self.do_clean_cache()

        return
