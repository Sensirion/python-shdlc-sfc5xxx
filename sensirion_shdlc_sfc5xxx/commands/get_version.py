# -*- coding: utf-8 -*-
# (c) Copyright 2020 Sensirion AG, Switzerland

##############################################################################
##############################################################################
#                 _____         _    _ _______ _____ ____  _   _
#                / ____|   /\  | |  | |__   __|_   _/ __ \| \ | |
#               | |       /  \ | |  | |  | |    | || |  | |  \| |
#               | |      / /\ \| |  | |  | |    | || |  | | . ` |
#               | |____ / ____ \ |__| |  | |   _| || |__| | |\  |
#                \_____/_/    \_\____/   |_|  |_____\____/|_| \_|
#
#     THIS FILE IS AUTOMATICALLY GENERATED AND MUST NOT BE EDITED MANUALLY!
#
# Generator:    sensirion-shdlc-interface-generator 0.8.2
# Product:      SFC5xxx
# Version:      0.1.0
#
##############################################################################
##############################################################################

# flake8: noqa

from __future__ import absolute_import, division, print_function
from sensirion_shdlc_driver.command import ShdlcCommand
from struct import pack, unpack

import logging
log = logging.getLogger(__name__)


class Sfc5xxxCmdGetVersionBase(ShdlcCommand):
    """
    SHDLC command 0xD1: "Get Version".
    """

    def __init__(self, *args, **kwargs):
        """
        Constructor.
        """
        super(Sfc5xxxCmdGetVersionBase, self).__init__(
            0xD1, *args, **kwargs)


class Sfc5xxxCmdGetVersion(Sfc5xxxCmdGetVersionBase):
    """
    Get Version Command

    Get the version information for the hardware, firmware and SHDLC protocol.
    """

    def __init__(self):
        """
        Constructor.
        """
        super(Sfc5xxxCmdGetVersion, self).__init__(
            data=[],
            max_response_time=0.01,
            post_processing_time=0.0,
            min_response_length=7,
            max_response_length=7
        )

    @staticmethod
    def interpret_response(data):
        """
        :return:
            - firmware_major (int) -
              Firmware major version number.
            - firmware_minor (int) -
              Firmware minor version number.
            - firmware_debug (bool) -
              Firmware debug state. All officially released and delivered
              firmware versions have this set to false (i.e. 0x00).
            - hardware_major (int) -
              Hardware major version number.
            - hardware_minor (int) -
              Hardware minor version number.
            - protocol_major (int) -
              Protocol major version number.
            - protocol_minor (int) -
              Protocol minor version number.
        :rtype: tuple
        """
        firmware_major = int(unpack(">B", data[0:1])[0])  # uint8
        firmware_minor = int(unpack(">B", data[1:2])[0])  # uint8
        firmware_debug = bool(unpack(">?", data[2:3])[0])  # bool
        hardware_major = int(unpack(">B", data[3:4])[0])  # uint8
        hardware_minor = int(unpack(">B", data[4:5])[0])  # uint8
        protocol_major = int(unpack(">B", data[5:6])[0])  # uint8
        protocol_minor = int(unpack(">B", data[6:7])[0])  # uint8
        return firmware_major,\
            firmware_minor,\
            firmware_debug,\
            hardware_major,\
            hardware_minor,\
            protocol_major,\
            protocol_minor
