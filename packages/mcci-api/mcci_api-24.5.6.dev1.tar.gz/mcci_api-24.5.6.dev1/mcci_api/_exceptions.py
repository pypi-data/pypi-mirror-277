# SPDX-FileCopyrightText: 2024 osfanbuff63 <osfanbuff63@osfanbuff63.tech>
#
# SPDX-License-Identifier: MIT

"""Exceptions used by the library."""


class MCCIException(Exception):
    """Base library exception. Use this to catch all exception from the library."""


class NoUsernameOrUUIDException(MCCIException):
    """No username or UUID was provided!"""


class InvalidTrophyType(MCCIException):
    """An invalid trophy type was provided."""
