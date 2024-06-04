# SPDX-License-Identifier: BSD-2-Clause-Patent
# SPDX-FileCopyrightText: 2023 Syslinbit <contact@syslinbit.com>

"""Backend classes"""


import subprocess
import os
import json

from nost.storages import StorageManagerDraft
from nost.logger import logger
from nost import config


nost_backend = None


class Backend():
    """Abstract class describing backend main methods.
    This class is inherited by every instanciable backend.
    """

    def __init__(self):
        """Constructor method
        """

        self.storage = StorageManagerDraft()
        return

    def process(self, service_name, target_dir):
        """Store data of the given service

        :param service_name: Name of the service to backup
        :param target_dir: Location of the newly fetch data
        :type service_name: String
        :type target_dir: String
        """
        pass

    def do_alert(self):
        """Alert user
        """
        pass

    def do_rotate(self, service_name):
        """Apply rotations

        :param service_name: Name of the service to backup
        :type service_name: String
        """
        pass

    def do_encrypt(self):
        """Apply encryption
        """
        pass

    def list_data(self):
        """Output the list of archive stored
        """
        pass

    def retrieve(self, dataId, dest=None):
        """Pull an archive with its ID

        :param dataId: ID of a archive,
            default format service_name-timestamp.

        :type dataId: String
        """
        pass

    def delete(self, dataId):
        """Tear down an archive with its ID

        :param dataId: ID of a archive,
            default format service_name-timestamp.

        :type dataId: String
        """
        pass

    def do_clean(self):
        """Delete all archives
        """
        pass


class DumbBackend(Backend):
    """Dummy backend class for testing purposes.
    This class inherits from nostBackend.
    """
    pass


class Borg(Backend):
    """Backend class using Borgbackup to process data.
    This class inherits from nostBackend.
    """

    def borgcmd_wrapper(self, cmd_line):
        """Interact with borg repository using subprocess commands. Also reads
        from BORG_PASSPHRASE_FD to pipe the passphrase to every borg call.

        :param cmd_line: Borg command line
        :type cmd_line: List

        :return: Information resulted from the subprocess command.
            First, the generated stdout.
            Second, the generated error.
            Third, the generated code.

        :rtype: Tuple
        """

        fdr = None

        if self.passphrase is None and "BORG_PASSPHRASE_FD" in os.environ:
            with os.fdopen(int(os.environ["BORG_PASSPHRASE_FD"])) as f:
                self.passphrase = f.read()

        if self.passphrase is not None:
            fdr, fdw = os.pipe()
            with os.fdopen(fdw, "w") as f:
                f.write(self.passphrase)
            os.set_inheritable(fdr, True)
            os.environ["BORG_PASSPHRASE_FD"] = str(fdr)

        proc = subprocess.Popen(
            cmd_line,
            close_fds=False,
            stdout=subprocess.PIPE
        )

        if fdr is not None:
            os.close(fdr)

        out, error = proc.communicate()
        code = proc.returncode

        return out, error, code

    def repository_exists(self):
        """Check if a borg repository already exists.

        :return: True if the repository already exists,
            False if the repository doesn't exists.

        :rtype: Boolean

        """
        _, _, code = self.borgcmd_wrapper(
            [
                "borg",
                "list",
                f"{self.repo_path}"
            ]
        )

        if not code:
            self.logger.debug(f"Borg repository at {self.repo_path}")
            return True
        else:
            self.logger.info("Borg repository doesn't exist")
            return False

    def __init__(self):
        """Constructor method.
        Configure attributs with values found in
        the configuration file (nost.toml)
        """
        self.logger = logger
        self.passphrase = None

        try:
            self.repo_path = os.path.expanduser(config["backend"]["repo_path"])
        except KeyError as e:
            self.logger.error(f"Missing description {e}")
            raise (e)

        if "borg_key_path" in config["backend"]:
            self.borg_key_dir = os.path.expanduser(
                config["backend"]["borg_key_path"]
            )

        if not self.repository_exists():
            self.logger.info("Borg initialization started")
            _, error, code = self.borgcmd_wrapper(
                [
                    'borg',
                    'init',
                    '--make-parent-dirs',
                    '--encryption',
                    'repokey',
                    f'{self.repo_path}'
                ]
            )

            if code:
                logger.error("Borg initialization failed")
                raise Exception(error)
            else:
                logger.info("Borg initialization completed")

        return

    def get_last_archive(self, service_name):
        """Retrieve the name of the last
        archive created for a given service.

        :param service_name: Name of the service
        :type service_name: String

        :return: The name of the last archive found for the given service name,
            default if not found is None.

        :rtype: String
        """

        out, _, code = self.borgcmd_wrapper(
            [
                "borg",
                "list",
                f"{self.repo_path}"
            ]
        )

        if not code:
            dates = []
            lines = out.decode("utf-8").split("\n")
            for line in lines:
                if line != '' and line[:len(service_name)] == service_name:
                    dates.append(line[(len(service_name)+1):].split()[0])
            if len(dates) > 0:
                return f'{service_name}-{max(dates)}'
            else:
                return None
        else:
            return None

    def diff(self, service_name, target_dir):
        """Check if data has changed on a
        given service since the last backup was done.

        :param service_name: Name of the service
        :param target_dir: Location of the newly fetch data
        :type service_name: String
        :type target_dir: String

        :return: Status of the difference found:
            change = diff, if a difference was found.
            change = nodiff, if no difference was found and the dictionnary keep
            the name of the newly created archive made to test differences.
            change = nofile, if there is no archive found for the given service.

        :rtype: Dict
        """

        if self.get_last_archive(service_name) is not None:
            last_filename = self.get_last_archive(service_name)
            self.create_archive(service_name, target_dir)
            new_filename = self.get_last_archive(service_name)

            out, error, code = self.borgcmd_wrapper(
                [
                    "borg",
                    "diff",
                    "--json-lines",
                    f"{self.repo_path}::{last_filename}",
                    f"{new_filename}"
                ]
            )

            if not code:
                output = out.decode("utf-8").split("\n")
                output.pop()
                for el in output:
                    tmp = json.loads(el)
                    if "added" in tmp["changes"] and (
                        tmp["changes"][0]["added"] != 0 or
                        tmp["changes"][0]["removed"] != 0
                    ):
                        return {"change": "diff"}
                    else:
                        pass
                return {"change": "nodiff", "filename": new_filename}
            else:
                raise (error)
        else:
            # if no archive found
            return {"change": "nofile"}

    def create_archive(self, service_name, target_dir):
        """Create an archive for a given service
        using data pulled.

        :param service_name: Name of the service
        :param target_dir: Location of the newly fetch data
        :type service_name: String
        :type target_dir: String

        :return: the name of the newly created archive
        :rtype: String
        """

        current_path = os.getcwd()
        os.chdir("/".join(target_dir.split("/")[:-1]))

        name = f'{service_name}-{{now:%Y-%m-%dT%H:%M:%S.%f}}'
        borg_path = f'{self.repo_path}::{name}'

        _, error, code = self.borgcmd_wrapper(
            [
                "borg",
                "create",
                "--compression",
                "lz4",
                f"{borg_path}",
                f"{service_name}"
            ]
        )

        os.chdir(current_path)

        if not code:
            self.logger.info(f"{service_name} compressed, encrypted and stored")
        else:
            self.logger.error(f"{service_name} backup failed")
            raise (error)

        return name

    def process(self, service_name, target_dir):
        """Backuping data pulled for a given
        service with mechanism to avoid duplication.

        :param service_name: Name of the service
        :param target_dir: Location of the newly fetch data
        :type service_name: String
        :type target_dir: String

        :return: the name of the newly created archive
        :rtype: String
        """

        diff_result = self.diff(service_name, target_dir)

        if diff_result["change"] == "nofile":
            self.create_archive(service_name, target_dir)
        elif diff_result["change"] == "nodiff":
            # Remove archive created to compare
            _, error, code = self.borgcmd_wrapper(
                [
                    "borg",
                    "delete",
                    f'{self.repo_path}::{diff_result["filename"]}'
                ]
            )

            self.logger.info(
                f"Service {service_name} hadn't changed since last backup."
            )

            if not code:
                self.logger.info("Remove temporary archive")
            else:
                self.logger.info("Removing temporary archive failed")
                raise (error)

        return

    def retrieve(self, dataId, dest=None, filter=None):
        """Extract data archived for a given service.

        :param dataId: Name of the archive
        :param filter: Name of a specific folder or file to extract,
            default value is None.

        :type dataId: String
        :type filter: String
        """

        current_path = None
        if dest is not None:
            current_path = os.getcwd()
            os.chdir(dest)

        _, error, code = self.borgcmd_wrapper(
            [
                "borg",
                "extract",
                f"{self.repo_path}::{dataId}"
            ]
        )

        if current_path is not None:
            os.chdir(current_path)

        if not code:
            self.logger.info("Retrieve archive successful")
        else:
            self.logger.error(f'Archive {dataId} extraction failed.')
            raise (error)

        return

    def list_data(self):
        """Output the list of archive stored in this backend

        :return: All archives stored in this backend
        :rtype: String
        """
        out, _, code = self.borgcmd_wrapper(
            [
                "borg",
                "list",
                f"{self.repo_path}"
            ]
        )

        if not code:
            services = []
            lines = out.decode("utf-8").split("\n")
            for line in lines:
                if line != '':
                    dataId = line.split(" ")[0]
                    service_name = dataId.split("-")[0]
                    time = "-".join(dataId.split("-")[1:])
                    services.append(
                        {"id": dataId, "name": service_name, "time": time}
                    )
            return services
        else:
            self.logger.error("Cannot read archive from borg repository.")
            return None

    def delete(self, dataId):
        """Tear down an archive from the repository

        :param dataId: ID of the archive to delete
        :type dataId: String, default format: service_name-timestamp
        """

        _, error, code = self.borgcmd_wrapper(
            [
                "borg",
                "delete",
                f"{self.repo_path}::{dataId}"
            ]
        )
        if not code:
            self.logger.info(f"Archive {dataId} deleted")
        else:
            self.logger.error(f"Archive {dataId} deletion failed")
            raise (error)

    # By default rotation mentioned in nost.toml is used
    def do_rotate(self, service_name, rotation=None):
        """Apply rotations on archives of given service

        :param service_name: Name of the service
        :param rotation: Rotation configuration
        :type service_name: String
        :type rotation: Dict
        """

        if rotation is None:
            rotation = config["backend"]["rotate"]

        cmd_line = [
            "borg",
            "prune",
            "-v",
            "--list"
        ]

        for k, v in rotation.items():
            match k:
                case "year":
                    cmd_line.append(f"--keep-yearly={v}")
                case "month":
                    cmd_line.append(f"--keep-monthly={v}")
                case "week":
                    cmd_line.append(f"--keep-weekly={v}")
                case "day":
                    cmd_line.append(f"--keep-daily={v}")
                case _:
                    raise KeyError(f"Rotation option {k} not supported")

        cmd_line.append(f"--glob-archives={service_name}-*")
        cmd_line.append(f"{self.repo_path}")

        self.borgcmd_wrapper(cmd_line)

        return


#: Backend type mapping
BACKEND = {
    "dumb": DumbBackend,
    "borg": Borg
}


def init_backend():
    """Creates backends depending on was type of
        backends are found in the configuration file (nost.toml).
    """
    return BACKEND[config["backend"]["type"].lower()]()


def getBackend():
    global nost_backend
    if nost_backend is None:
        nost_backend = init_backend()
    return nost_backend
