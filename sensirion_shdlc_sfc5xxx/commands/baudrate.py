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


class Sfc5xxxCmdBaudrateBase(ShdlcCommand):
    """
    SHDLC command 0x91: "Baudrate".
    """

    def __init__(self, *args, **kwargs):
        """
        Constructor.
        """
        super(Sfc5xxxCmdBaudrateBase, self).__init__(
            0x91, *args, **kwargs)


class Sfc5xxxCmdGetBaudrate(Sfc5xxxCmdBaudrateBase):
    """
    Get Baudrate Command

    Get the SHDLC baudrate of the device.
    """

    def __init__(self):
        """
        Constructor.
        """
        super(Sfc5xxxCmdGetBaudrate, self).__init__(
            data=[],
            max_response_time=0.01,
            post_processing_time=0.0,
            min_response_length=4,
            max_response_length=4
        )

    @staticmethod
    def interpret_response(data):
        """
        :return: Current baudrate in bit/s.
        :rtype: int
        """
        baudrate = int(unpack(">I", data[0:4])[0])  # uint32
        return baudrate


class Sfc5xxxCmdSetBaudrate(Sfc5xxxCmdBaudrateBase):
    """
    Set Baudrate Command

    Set the SHDLC baudrate of the device.

    .. note:: The baudrate is stored in non-volatile memory of the device and
              thus persists after a device reset. So the next time connecting
              to the device, you have to use the new baudrate.
    """

    def __init__(self, baudrate):
        """
        Constructor.

        :param int baudrate:
            The new baudrate in bit/s. Allowed values are 9600, 19200, 38400,
            115200 (default), 230400 and 460800.
        """
        super(Sfc5xxxCmdSetBaudrate, self).__init__(
            data=b"".join([pack(">I", baudrate)]),
            max_response_time=0.01,
            post_processing_time=0.0,
            min_response_length=0,
            max_response_length=0
        )
