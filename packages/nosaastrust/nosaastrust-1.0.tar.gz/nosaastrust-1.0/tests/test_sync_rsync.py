# SPDX-License-Identifier: BSD-2-Clause-Patent
# SPDX-FileCopyrightText: 2023 Syslinbit <contact@syslinbit.com>

import filecmp
import os
import shutil
import unittest

from nostplugins.rsync import RSYNC


class RsyncTest(unittest.TestCase):
    def setUp(self):
        self.name = "rsync_test"
        self.path = "./tests/testenv/"
        self.cachedir = "/tmp/nosttests"
        self.dest = os.path.join(self.cachedir, self.name)
        os.makedirs(self.cachedir)
        self.rsync = RSYNC(
            self.name,
            "local",
            path=self.path,
            cachedir=self.cachedir
        )

    def tearDown(self):
        shutil.rmtree(self.cachedir)

    def test_sync(self):
        self.rsync.do_sync(clean=False)
        self.assertTrue(os.path.exists(self.dest))
        self.assertTrue(filecmp.dircmp(self.path, self.dest))
