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


class Sfc5xxxCmdValveInputSourceConfigurationBase(ShdlcCommand):
    """
    SHDLC command 0x20: "Valve Input Source Configuration".
    """

    def __init__(self, *args, **kwargs):
        """
        Constructor.
        """
        super(Sfc5xxxCmdValveInputSourceConfigurationBase, self).__init__(
            0x20, *args, **kwargs)


class Sfc5xxxCmdGetValveInputSource(Sfc5xxxCmdValveInputSourceConfigurationBase):
    """
    Get Valve Input Source Command

    Get the input source for the valve, i.e. the input which controls the valve
    voltage.
    """

    def __init__(self):
        """
        Constructor.
        """
        super(Sfc5xxxCmdGetValveInputSource, self).__init__(
            data=b"".join([bytes(bytearray([0x00]))]),
            max_response_time=0.005,
            post_processing_time=0.0,
            min_response_length=1,
            max_response_length=1
        )

    @staticmethod
    def interpret_response(data):
        """
        :return: The current valve input source:

                 -  0x00: Controller (default), driven by the flow controller.
                 -  0x01: Force closed, valve remains fully closed.
                 -  0x02: Force open, valve remains fully open.
                 -  0x03: Hold, hold the voltage on the valve.
                 -  0x10: User defined, apply user defined value [0..1].
        :rtype: int
        """
        input_source = int(unpack(">B", data[0:1])[0])  # uint8
        return input_source


class Sfc5xxxCmdSetValveInputSource(Sfc5xxxCmdValveInputSourceConfigurationBase):
    """
    Set Valve Input Source Command

    Set the input source for the valve, i.e. the input which controls the valve
    voltage.

    .. note:: This configuration is volatile.
    """

    def __init__(self, input_source):
        """
        Constructor.

        :param int input_source:
            The valve input source to set:

            -  0x00: Controller (default), driven by the flow controller.
            -  0x01: Force closed, valve remains fully closed.
            -  0x02: Force open, valve remains fully open.
            -  0x03: Hold, hold the voltage on the valve.
            -  0x10: User defined, apply user defined value [0..1].
        """
        super(Sfc5xxxCmdSetValveInputSource, self).__init__(
            data=b"".join([bytes(bytearray([0x00])),
                           pack(">B", input_source)]),
            max_response_time=0.005,
            post_processing_time=0.0,
            min_response_length=0,
            max_response_length=0
        )


class Sfc5xxxCmdGetUserDefinedValveValue(Sfc5xxxCmdValveInputSourceConfigurationBase):
    """
    Get User Defined Valve Value Command

    Get the value which is applied to the valve when the valve input source is
    set to *user defined*.
    """

    def __init__(self):
        """
        Constructor.
        """
        super(Sfc5xxxCmdGetUserDefinedValveValue, self).__init__(
            data=b"".join([bytes(bytearray([0x01]))]),
            max_response_time=0.005,
            post_processing_time=0.0,
            min_response_length=4,
            max_response_length=4
        )

    @staticmethod
    def interpret_response(data):
        """
        :return: The current user defined valve value [0..1]. 0.0 means fully
                 closed, 1.0 means fully open.
        :rtype: float
        """
        value = float(unpack(">f", data[0:4])[0])  # float
        return value


class Sfc5xxxCmdSetUserDefinedValveValue(Sfc5xxxCmdValveInputSourceConfigurationBase):
    """
    Set User Defined Valve Value Command

    Set the value which is applied to the valve when the valve input source is
    set to *user defined*.

    .. note:: This configuration is volatile.
    """

    def __init__(self, value):
        """
        Constructor.

        :param float value:
            The user defined valve value to set [0..1]. 0.0 means fully closed,
            1.0 means fully open.
        """
        super(Sfc5xxxCmdSetUserDefinedValveValue, self).__init__(
            data=b"".join([bytes(bytearray([0x01])),
                           pack(">f", value)]),
            max_response_time=0.005,
            post_processing_time=0.0,
            min_response_length=0,
            max_response_length=0
        )
