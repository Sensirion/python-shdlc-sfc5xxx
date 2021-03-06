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


class Sfc5xxxCmdControllerConfigurationBase(ShdlcCommand):
    """
    SHDLC command 0x22: "Controller Configuration".
    """

    def __init__(self, *args, **kwargs):
        """
        Constructor.
        """
        super(Sfc5xxxCmdControllerConfigurationBase, self).__init__(
            0x22, *args, **kwargs)


class Sfc5xxxCmdGetUserControllerGain(Sfc5xxxCmdControllerConfigurationBase):
    """
    Get User Controller Gain Command

    Get the user defined controller gain.
    """

    def __init__(self):
        """
        Constructor.
        """
        super(Sfc5xxxCmdGetUserControllerGain, self).__init__(
            data=b"".join([bytes(bytearray([0x00]))]),
            max_response_time=0.005,
            post_processing_time=0.0,
            min_response_length=4,
            max_response_length=4
        )

    @staticmethod
    def interpret_response(data):
        """
        :return: The current user controller gain.
        :rtype: float
        """
        gain = float(unpack(">f", data[0:4])[0])  # float
        return gain


class Sfc5xxxCmdSetUserControllerGain(Sfc5xxxCmdControllerConfigurationBase):
    """
    Set User Controller Gain Command

    Set the user defined controller gain.

    .. note:: This configuration is stored in non-volatile memory of the device
              and thus persists after a device reset.
    """

    def __init__(self, gain):
        """
        Constructor.

        :param float gain:
            The user controller gain to set.
        """
        super(Sfc5xxxCmdSetUserControllerGain, self).__init__(
            data=b"".join([bytes(bytearray([0x00])),
                           pack(">f", gain)]),
            max_response_time=0.005,
            post_processing_time=0.0,
            min_response_length=0,
            max_response_length=0
        )


class Sfc5xxxCmdGetPressureDependentGainEnable(Sfc5xxxCmdControllerConfigurationBase):
    """
    Get Pressure Dependent Gain Enable Command

    Get the pressure dependent gain enable state.
    """

    def __init__(self):
        """
        Constructor.
        """
        super(Sfc5xxxCmdGetPressureDependentGainEnable, self).__init__(
            data=b"".join([bytes(bytearray([0x10]))]),
            max_response_time=0.005,
            post_processing_time=0.0,
            min_response_length=1,
            max_response_length=1
        )

    @staticmethod
    def interpret_response(data):
        """
        :return: The current state of the pressure dependent gain.
        :rtype: bool
        """
        enable = bool(unpack(">?", data[0:1])[0])  # bool
        return enable


class Sfc5xxxCmdSetPressureDependentGainEnable(Sfc5xxxCmdControllerConfigurationBase):
    """
    Set Pressure Dependent Gain Enable Command

    Set the pressure dependent gain enable state.

    .. note:: This configuration is stored in non-volatile memory of the device
              and thus persists after a device reset.
    """

    def __init__(self, enable):
        """
        Constructor.

        :param bool enable:
            The pressure dependent gain state to set.
        """
        super(Sfc5xxxCmdSetPressureDependentGainEnable, self).__init__(
            data=b"".join([bytes(bytearray([0x10])),
                           pack(">?", enable)]),
            max_response_time=0.005,
            post_processing_time=0.0,
            min_response_length=0,
            max_response_length=0
        )


class Sfc5xxxCmdGetInletPressureForGainCorrection(Sfc5xxxCmdControllerConfigurationBase):
    """
    Get Inlet Pressure For Gain Correction Command

    Get the inlet pressure used for the pressure dependent gain.
    """

    def __init__(self):
        """
        Constructor.
        """
        super(Sfc5xxxCmdGetInletPressureForGainCorrection, self).__init__(
            data=b"".join([bytes(bytearray([0x11]))]),
            max_response_time=0.005,
            post_processing_time=0.0,
            min_response_length=4,
            max_response_length=4
        )

    @staticmethod
    def interpret_response(data):
        """
        :return: The currently set inlet pressure [bar].
        :rtype: float
        """
        pressure = float(unpack(">f", data[0:4])[0])  # float
        return pressure


class Sfc5xxxCmdSetInletPressureForGainCorrection(Sfc5xxxCmdControllerConfigurationBase):
    """
    Set Inlet Pressure For Gain Correction Command

    Set the inlet pressure used for the pressure dependent gain.

    .. note:: This configuration is stored in non-volatile memory of the device
              and thus persists after a device reset.
    """

    def __init__(self, pressure):
        """
        Constructor.

        :param float pressure:
            The inlet pressure to set [bar].
        """
        super(Sfc5xxxCmdSetInletPressureForGainCorrection, self).__init__(
            data=b"".join([bytes(bytearray([0x11])),
                           pack(">f", pressure)]),
            max_response_time=0.005,
            post_processing_time=0.0,
            min_response_length=0,
            max_response_length=0
        )


class Sfc5xxxCmdGetGasTemperatureCompensationEnable(Sfc5xxxCmdControllerConfigurationBase):
    """
    Get Gas Temperature Compensation Enable Command

    Get the gas temperature compensation enable state.
    """

    def __init__(self):
        """
        Constructor.
        """
        super(Sfc5xxxCmdGetGasTemperatureCompensationEnable, self).__init__(
            data=b"".join([bytes(bytearray([0x20]))]),
            max_response_time=0.005,
            post_processing_time=0.0,
            min_response_length=1,
            max_response_length=1
        )

    @staticmethod
    def interpret_response(data):
        """
        :return: The current state of the temperature compensation.
        :rtype: bool
        """
        enable = bool(unpack(">?", data[0:1])[0])  # bool
        return enable


class Sfc5xxxCmdSetGasTemperatureCompensationEnable(Sfc5xxxCmdControllerConfigurationBase):
    """
    Set Gas Temperature Compensation Enable Command

    Set the gas temperature compensation enable state.

    .. note:: This configuration is stored in non-volatile memory of the device
              and thus persists after a device reset.
    """

    def __init__(self, enable):
        """
        Constructor.

        :param bool enable:
            The temperature compensation state to set.
        """
        super(Sfc5xxxCmdSetGasTemperatureCompensationEnable, self).__init__(
            data=b"".join([bytes(bytearray([0x20])),
                           pack(">?", enable)]),
            max_response_time=0.005,
            post_processing_time=0.0,
            min_response_length=0,
            max_response_length=0
        )


class Sfc5xxxCmdGetInletGasTemperatureForCompensation(Sfc5xxxCmdControllerConfigurationBase):
    """
    Get Inlet Gas Temperature For Compensation Command

    Get the inlet gas temperature used for the temperature compensation.
    """

    def __init__(self):
        """
        Constructor.
        """
        super(Sfc5xxxCmdGetInletGasTemperatureForCompensation, self).__init__(
            data=b"".join([bytes(bytearray([0x21]))]),
            max_response_time=0.005,
            post_processing_time=0.0,
            min_response_length=4,
            max_response_length=4
        )

    @staticmethod
    def interpret_response(data):
        """
        :return: The currently set inlet gas temperature [°C].
        :rtype: float
        """
        temperature = float(unpack(">f", data[0:4])[0])  # float
        return temperature


class Sfc5xxxCmdSetInletGasTemperatureForCompensation(Sfc5xxxCmdControllerConfigurationBase):
    """
    Set Inlet Gas Temperature For Compensation Command

    Set the inlet gas temperature used for the temperature compensation.

    .. note:: This configuration is stored in non-volatile memory of the device
              and thus persists after a device reset.
    """

    def __init__(self, temperature):
        """
        Constructor.

        :param float temperature:
            The inlet gas temperature to set [°C].
        """
        super(Sfc5xxxCmdSetInletGasTemperatureForCompensation, self).__init__(
            data=b"".join([bytes(bytearray([0x21])),
                           pack(">f", temperature)]),
            max_response_time=0.005,
            post_processing_time=0.0,
            min_response_length=0,
            max_response_length=0
        )
