# SPDX-License-Identifier: BSD-2-Clause-Patent
# SPDX-FileCopyrightText: 2023 Syslinbit <contact@syslinbit.com>

"""Logs handler"""


import logging

logger = None

#: Default log level
default_log_level = 'info'


class Logger(logging.Logger):
    """Handle logging

    :param name: Logger name
    :type name: String
    """

    def __init__(self, name):
        """Constructor method
        """

        super().__init__(name)
        self.setLevelStr(default_log_level.upper())
        self.stream_handler = logging.StreamHandler()
        self.addHandler(self.stream_handler)

    def setLevelStr(self, level):
        """Get level to log?

        :param level: Level of log
        :type level: Sting
        """

        super().setLevel(logging.getLevelName(level.upper()))

    def toFile(self, filename):
        """Add log file

        :param filename: Path to log file
        :type filename: String
        """

        self.removeHandler(self.stream_handler)
        self.file_handler = logging.FileHandler(filename)
        self.addHandler(self.file_handler)


if logger is None:
    logging.setLoggerClass(Logger)
    logger = Logger("nost")
