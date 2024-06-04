# SPDX-License-Identifier: BSD-2-Clause-Patent
# SPDX-FileCopyrightText: 2023 Syslinbit <contact@syslinbit.com>

import os
import filecmp
import subprocess


class TestCommands:
    def init(self, testdir):
        # Create required directories
        testdir.joinpath("cache/nosaastrust").mkdir(parents=True)

        self.env = os.environ.copy()
        self.env.update({"NOSTDIR": str(testdir),
                         "BORG_PASSPHRASE": "test"})

        self.testdir = testdir
        self.make_data()
        self.make_config()
        self.make_description()

    def make_data(self):
        self.datadir = self.testdir.joinpath("data")
        filename = "data.txt"
        self.datadir.mkdir()
        with open(self.datadir.joinpath(filename), 'x') as f:
            f.write("Lorem Ipsum")

    def make_config(self, template="nost.toml.in"):
        """Create toml config from template"""
        template_path = os.path.join("tests/testenv/testcase", template)
        config_path = self.testdir.joinpath("nost.toml")
        with open(template_path, "r") as fr, \
             open(config_path, "w") as fw:
            for line in fr.readlines():
                fw.write(line.replace("@TESTDIR@", str(self.testdir)))

    def make_description(self, template="description.yml.in"):
        """Create description from template"""
        template_path = os.path.join("tests/testenv/testcase", template)
        self.description = self.testdir.joinpath("description.yml")
        with open(template_path, "r") as fr, \
             open(self.description, "w") as fw:
            for line in fr.readlines():
                fw.write(line.replace("@TESTDIR@", str(self.testdir)))

    def test_version(self):
        try:
            process = subprocess.run(
                ["nost", "--version"]
            )
        except Exception:
            assert False
        assert process.returncode == 0

    def test_sync(self, tmp_path):
        self.init(tmp_path)

        try:
            process = subprocess.run(
                ["nost", "sync", self.description],
                env=self.env
            )
        except Exception:
            assert False
        assert process.returncode == 0

        try:
            process = subprocess.run(
                ["nost", "list", "-ftext"],
                capture_output=True,
                env=self.env
            )
        except Exception:
            assert False
        assert process.returncode == 0
        list = process.stdout.decode('utf-8').split("\n")

        oldpwd = os.getcwd()
        os.chdir(tmp_path)
        try:
            process = subprocess.run(
                ["nost", "retrieve", list[0].split()[2]],
                env=self.env
            )
        except Exception:
            assert False
        assert process.returncode == 0
        retrieve_path = tmp_path.joinpath("testcase1/data")
        assert retrieve_path.exists()
        assert filecmp.dircmp(retrieve_path, self.datadir)

        os.chdir(oldpwd)

    def test_help(self):
        for command in [
                ["nost", "-h"], ["nost", "--help"]
        ]:
            try:
                process = subprocess.run(command)
            except Exception:
                assert False
            assert process.returncode == 0

    def test_wrong_commands(self):
        for command in [
                ["nost"], ["nost", "sync"],
                ["nost", "retrieve"], ["nost", "delete"],
                ["nost", "-d"], ["nost", "--debug"],
                ["nost", "-l"], ["nost", "--level"],
                ["nost", "-x"], ["nost", "-L"],
        ]:
            try:
                process = subprocess.run(command)
            except Exception:
                assert False
            assert process.returncode != 0
