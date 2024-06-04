# SPDX-License-Identifier: BSD-2-Clause-Patent
# SPDX-FileCopyrightText: 2023 Syslinbit <contact@syslinbit.com>

import os
import unittest

from nost import vaults


class VaultsTest(unittest.TestCase):
    def setUp(self):
        self.vault = os.path.join(os.getenv("NOSTDIR"), "vault")

    def test_initVaults(self):
        v = vaults.init_vaults()
        self.assertIsInstance(v[0], vaults.LocalVault)
        self.assertIsInstance(v[1], vaults.LocalVault)

    def test_retrieveExistingService(self):
        v = vaults.LocalVault(path=self.vault, encryption="b64")
        password = v.retrieve("serviceA", "userA")
        self.assertEqual(password, "passA")
        password = v.retrieve("serviceA", "userB")
        self.assertEqual(password, "passB")
        password = v.retrieve("serviceA", "userC")
        self.assertEqual(password, "passC")

    def test_retrieveWrongService(self):
        v = vaults.LocalVault(path=self.vault, encryption="b64")
        password = v.retrieve("serviceB", "userA")
        self.assertIsNone(password)

    def test_retrieveWrongUser(self):
        v = vaults.LocalVault(path=self.vault, encryption="b64")
        password = v.retrieve("serviceA", "ghost")
        self.assertIsNone(password)


class VaultsInstanceTest(unittest.TestCase):
    def test_instanciateLocalVault(self):
        v = vaults.instanciate_vault(mode="local", path="/my/path")
        self.assertIsInstance(v, vaults.LocalVault)
        self.assertEqual(v.path, "/my/path")

    def test_instanciateBitwardenVault(self):
        v = vaults.instanciate_vault(mode="bitwarden")
        self.assertIsInstance(v, vaults.BitwardenVault)
