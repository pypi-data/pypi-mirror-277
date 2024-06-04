# SPDX-License-Identifier: BSD-2-Clause-Patent
# SPDX-FileCopyrightText: 2023 Syslinbit <contact@syslinbit.com>

"""Handle configuration given in .toml"""


import os
import sys
import tomllib

config = None

#: Possible locations of the configuration file
CONFIG_LOCATIONS = [
    os.path.expanduser("~/.config"),
    "/etc",
    "/usr/share/nost"
]

#: Configuration file's name
CONFIG_NAME = "nost.toml"


def get_config_path():
    """
    Find config in one of possible locations
    """
    env_nostdir = os.getenv("NOSTDIR")
    if env_nostdir is not None:
        path = os.path.join(env_nostdir, CONFIG_NAME)
        if os.path.exists(path):
            return path

    for c in CONFIG_LOCATIONS:
        path = os.path.join(c, CONFIG_NAME)
        if os.path.exists(path):
            return path
    raise Exception("No config found")


if config is None:
    """
    Store configuration
    """
    try:
        with open(get_config_path(), "rb") as cf:
            config = tomllib.load(cf)
    except Exception as e:
        print(e, file=sys.stderr)
        config = None
