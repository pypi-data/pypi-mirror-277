# SPDX-License-Identifier: BSD-2-Clause-Patent
# SPDX-FileCopyrightText: 2023 Syslinbit <contact@syslinbit.com>

"""WEBDAV plugin, to fetch data with webdav"""


import xml.etree.ElementTree as ET
import os
import requests
import urllib.parse


from nost.plugins import Plugin
from nost.credentials import Password


class WEBDAV(Plugin):
    """WEBDAV plugin, to fetch data with webdav.

    :param name: Name of the sevice to fetch with current plugin
    :param host: Address to fetch data from
    :param cachedir: Path to store data locally before processing
    :param kwargs: Other configuration, from service description (.yml)
    :type name: String
    :type host: String
    :type cachedir: String
    :type kwargs: Dict
    """

    def do_authenticate(self, **kwargs):
        """Get username and password with credential object

        :param kwargs: Additional information
        :type kwargs: Dict

        :return: Credential object
        :rtype: Credentials
        """

        try:
            credentials = Password(self.service_name, **kwargs)
        except KeyError as e:
            self.logger.error(f"Description is missing {e}")
            raise (e)
        return credentials

    def find_content(self, credentials, path):
        """Explore service tree

        :param credentials: Credentials object to authenticate
        :param path: path to explore

        :return: Request result
        :rtype: Dict
        """
        webdav_login, webdav_password = credentials.auth()
        paths = None

        with requests.Session() as session:
            try:
                res = session.request(
                    method="PROPFIND",
                    headers={"Depth": "1"},
                    url=path,
                    auth=(webdav_login, webdav_password)
                )
                res.raise_for_status()

                result = ET.fromstring(
                    urllib.parse.unquote(res.content.decode("utf-8"))
                )

                paths = [
                    response.find("{DAV:}href").text
                    for response in result.findall("{DAV:}response")
                ]

            except requests.exceptions.ConnectionError as err:
                self.logger.error("Connection failed")
                raise (err)

            except requests.exceptions.HTTPError as err:
                self.logger.error("HTTP error occured")
                raise (err)

        return paths

    def download(self, credentials, path):
        """Download file

        :param credentials: Credentials object to authenticate
        :param path: Full path to the file
        """
        webdav_login, webdav_password = credentials.auth()

        filename = path.split("/")[-1]
        self.logger.info(f"Downloading {filename} ..")

        with requests.Session() as session:
            try:
                resp = session.request(
                    method="GET",
                    url=f"{self.source_host}/{path}",
                    auth=(webdav_login, webdav_password),
                    stream=True
                )
                resp.raise_for_status()

                if resp.status_code == 200:
                    with open(f"{self.cache_dir}/{path}", 'wb') as f:
                        for chunk in resp.iter_content(chunk_size=1024):
                            if chunk:
                                f.write(chunk)

            except requests.exceptions.ConnectionError as err:
                self.logger.error("Connection failed")
                raise (err)

            except requests.exceptions.HTTPError as err:
                self.logger.error("HTTP error occured")
                raise (err)

        return

    def walk(self, credentials, r, last_href):
        """Walk through service files and directories

        :param credentials: Credentials object to authenticate
        :param r: Last tree found
        :param last_href: Last folder explored (and already downloaded)
        :type credentials: Credentials
        :type r: Dict
        :type last_href: String
        """

        for el in r:
            if el == last_href:
                continue
            else:
                if el != "/webdav/" and el[-1] == "/":
                    self.create_local_dirs(
                        el[len("/webdav/"):]
                    )
                    res = self.find_content(
                        credentials,
                        "{}/{}".format(self.source_host,
                                       el[len('/webdav/'):]
                                       )
                    )
                    self.walk(credentials, res, el)
                else:
                    filename = el.split("/")[-1]
                    if not filename.startswith(".~lock"):
                        self.download(
                            credentials,
                            el[len("/webdav/"):]
                        )

        return

    def create_local_dirs(self, dir_path):
        """Mimic architecture found locally

        :param dir_path: Directories to create
        :type dir_path: String
        """
        self.logger.info("Creating architecture locally..")

        if not os.path.isdir(f"{self.cache_dir}/{dir_path[:-1]}"):
            os.makedirs(f"{self.cache_dir}/{dir_path[:-1]}")

        return

    def do_sync(self, credentials=None, backend=None, clean=True, **kwargs):
        """Fetch data of given service with webdav

        :param credentials: Credentials object to authenticate.
        :param backend: Backend object to use.
        :param clean: Default True. Remove data from cache directory.
        :param kwargs: Not used with this plugin.
        :type credentials: Credentials
        :type backend: Backend
        :type clean: Boolean
        :type kwargs: None
        """
        result = self.find_content(credentials, self.source_host)
        self.walk(credentials, result, "/webdav/")

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

        return
