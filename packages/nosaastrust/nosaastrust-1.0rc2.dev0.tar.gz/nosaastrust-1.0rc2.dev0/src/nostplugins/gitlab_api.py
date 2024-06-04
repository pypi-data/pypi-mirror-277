# SPDX-License-Identifier: BSD-2-Clause-Patent
# SPDX-FileCopyrightText: 2023 Syslinbit <contact@syslinbit.com>

"""
GitlabAPI plugin, to fetch git repositories, project
and group information through GitlabAPI.
"""


import json
import requests
import time


from nost.plugins import Plugin
from nost.credentials import Password
from nostplugins.git import Git

#: Current GitLab API endpoint
API_ENDPOINT = 'api/v4'

#: Current GitLab export endpoint
EXPORT_ENDPOINT = 'export'


class GitlabAPI(Plugin):
    """GitlabAPI plugin, to fetch git repositories, project
    and group information through GitlabAPI.

    :param name: Name of the sevice to fetch with current plugin
    :param host: Address to fetch data from
    :param cachedir: Path to store data locally before processing
    :param kwargs: Other configuration, from service description (.yml)
    :type name: String
    :type host: String
    :type cachedir: String
    :type kwargs: Dict
    """

    def do_configure(self, **kwargs):
        """Prepare URL to use

        :param kwargs: Additional information. Use to get GitLab group ID.
        :type kwargs: Dict
        """

        try:
            self.group_url = \
                f'{self.source_host}/{API_ENDPOINT}/groups/{kwargs["group_id"]}'
            self.group_all_project_url = \
                f'{self.group_url}/projects?include_subgroups=true'
            self.project_base_url = \
                f'{self.source_host}/{API_ENDPOINT}/projects'
        except KeyError as e:
            self.logger.error(f"Missing argument {e}")
            raise (e)
        return

    def get_export_project_url(self, p_id):
        """Build URL to use for project fetch.

        :param p_id: Project ID
        :type p_id: String

        :return: URL
        :rtype: String
        """
        return f"{self.project_base_url}/{p_id}/{EXPORT_ENDPOINT}"

    def do_authenticate(self, **kwargs):
        """Get GitLab PAT with a credential object.

        :param kwargs: Additional information
        :type kwargs: Dict

        :return: Credential instance
        :rtype: Credentials
        """
        try:
            credential = Password(self.service_name, **kwargs)
        except KeyError as e:
            self.logger.error(f"Missing information {e}")

        return credential

    def get_root_group(self, gl_PAT):
        """Get root group information

        :param gl_PAT: GitLab Personal Access Token
        :type gl_PAT: String

        :return: Group root information
        :rytpe: Dict (json)
        """
        rgroup = None
        params = {
            "Content-Type": "application/json",
            "PRIVATE-TOKEN": gl_PAT
        }

        with requests.Session() as session:
            try:
                group_req = session.get(
                    self.group_url,
                    headers=params
                )
                group_req.raise_for_status()

                tmp = group_req.content.decode('utf-8')
                rgroup = json.loads(tmp)

            except requests.exceptions.ConnectionError as err:
                self.logger.error("Connection failed")
                raise (err)

            except requests.exceptions.HTTPError as err:
                self.logger.error("HTTP error occured")
                raise (err)

        return rgroup

    def get_subgroup(self, gl_PAT):
        """Get subgroup information

        :param gl_PAT: GitLab Personal Access Token
        :type gl_PAT: String

        :return: Subgroup information
        :rytpe: Dict (json)
        """
        subgroups = None
        params = {
            "Content-Type": "application/json",
            "PRIVATE-TOKEN": gl_PAT
        }

        with requests.Session() as session:
            try:
                subgroup_req = session.get(
                    f"{self.group_url}/descendant_groups",
                    headers=params
                )
                subgroup_req.raise_for_status()

                tmp = subgroup_req.content.decode('utf-8')
                subgroups = json.loads(tmp)

            except requests.exceptions.ConnectionError as err:
                self.logger.error("Connection failed")
                raise (err)

            except requests.exceptions.HTTPError as err:
                self.logger.error("HTTP error occured")
                raise (err)

        return subgroups

    def get_project_list(self, gl_PAT):
        """List every project accessible with given PAT.
        :param gl_PAT: GitLab Personal Access Token
        :type gl_PAT: String

        :return: Every project information
        :rytpe: Dict (json)
        """
        projects = None
        params = {
            "Content-Type": "application/json",
            "PRIVATE-TOKEN": gl_PAT
        }

        with requests.Session() as session:
            try:
                p_list_req = session.get(
                    self.group_all_project_url,
                    headers=params
                )
                p_list_req.raise_for_status()

                tmp = p_list_req.content.decode("utf-8")
                projects = json.loads(tmp)

            except requests.exceptions.ConnectionError as err:
                self.logger.error("Connection failed")
                raise (err)

            except requests.exceptions.HTTPError as err:
                self.logger.error("HTTP error occured")
                raise (err)

        return projects

    def export_project(self, gl_PAT, p_id):
        """Fetch GitLab project.

        :param gl_PAT: GitLab Personal Access Token
        :param p_id: Project ID
        :type gl_PAT: String
        :type p_id: String
        """
        url = self.get_export_project_url(p_id)

        params = {
            "Content-Type": "application/gzip",
            "PRIVATE-TOKEN": gl_PAT
        }

        with requests.Session() as session:
            session.post(
                url,
                headers=params
            )

            export_status = None
            while export_status != "finished":
                try:
                    req_get = session.get(
                        url,
                        headers=params
                    )
                    req_get.raise_for_status()

                    tmp = req_get.content.decode("utf-8")
                    result = json.loads(tmp)

                    if result["export_status"] == "finished":
                        self.logger.info(f"{result['name']} export finished.")
                        export_status = "finished"
                    else:
                        self.logger.info(
                            f"{result['name']} export in progress."
                        )
                        time.sleep(60)

                except requests.exceptions.ConnectionError as err:
                    self.logger.error("Connection failed")
                    raise (err)

            try:
                req_download = session.get(
                    result["_links"]["api_url"],
                    headers=params
                )
                req_download.raise_for_status()

                if req_download.status_code == 200:
                    with open(f"{self.cache_dir}/{result['name']}-info.archive",
                              mode="wb") as file:
                        file.write(req_download.content)
                    self.logger.info(f"Downloaded project {result['name']}.")

            except requests.exceptions.ConnectionError as err:
                self.logger.error("Connection failed")
                raise (err)

            except requests.exceptions.HTTPError as err:
                self.logger.error("HTTP error occured")
                raise (err)

        return

    def do_sync(self, credentials=None, backend=None, clean=True, **kwargs):
        """Fetch data of given service with GitLab API

        :param credentials: Credentials object to authenticate..
        :param backend: Backend object to use.
        :param clean: Default True. Remove data from cache directory.
        :param kwargs: Not used with this plugin.
        :type credentials: Credentials
        :type backend: Backend
        :type clean: Boolean
        :type kwargs: None
        """
        _, gl_PAT = credentials.auth()

        if gl_PAT is None:
            self.logger.warning("Token not found")

        # Group information
        group_info = self.get_root_group(gl_PAT)
        with open(f'{self.cache_dir}/group_info.json', 'w') as group_f:
            json.dump(group_info, group_f)

        # Subgroup information
        subgroup_info = self.get_subgroup(gl_PAT)
        with open(f'{self.cache_dir}/subgroup_info.json', 'w') as subgroup_f:
            json.dump(subgroup_info, subgroup_f)

        # Get project list
        project_list = self.get_project_list(gl_PAT)

        for p in project_list:
            self.export_project(gl_PAT, p["id"])
            gitconfig = {"host": "local", "path": p["ssh_url_to_repo"]}
            repo = Git(p["name"], cachedir=self.cache_dir, **gitconfig)
            repo.do_sync(clean=False)

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
