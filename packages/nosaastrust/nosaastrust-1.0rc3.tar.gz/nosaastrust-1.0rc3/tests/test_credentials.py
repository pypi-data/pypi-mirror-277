# SPDX-License-Identifier: BSD-2-Clause-Patent
# SPDX-FileCopyrightText: 2023 Syslinbit <contact@syslinbit.com>

import unittest

from nost import credentials


class CredentialsTest(unittest.TestCase):

    def test_Credentials(self):
        c = credentials.Credentials("service", auth={"user": "userA"})
        self.assertIsInstance(c, credentials.Credentials)

        c = credentials.Password("service", auth={"user": "userA"})
        self.assertIsInstance(c, credentials.Password)

        c = credentials.Password(
            "service",
            auth={"user": "userA", "password": "passA"}
        )
        self.assertIsInstance(c, credentials.Credentials)
        self.assertEqual(c.auth(), ("userA", "passA"))

        c = credentials.Password(
            "service",
            auth={"user": "userA", "password": "passA"}
        )
        self.assertIsInstance(c, credentials.Credentials)
        self.assertIsNone(c.auth("userB")[1])
