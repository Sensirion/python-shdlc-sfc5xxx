# -*- coding: utf-8 -*-
# (c) Copyright 2020 Sensirion AG, Switzerland

from __future__ import absolute_import, division, print_function

import logging
log = logging.getLogger(__name__)


class Sfc5xxxCalibrationConditions(object):
    """
    A class representing the calibration condition parameters as used to store
    the initial calibration conditions and recalibration conditions of
    gas calibration blocks.

    The class provides some public members which you can access directly.
    """

    def __init__(self, company, operator, datetime, temperature,
                 inlet_pressure, differential_pressure,
                 is_real_gas_calibration, accuracy_setpoint,
                 accuracy_fullscale):
        """Constructor.

        :param str company:
            The company which has created the calibration.
        :param str operator:
            The operator who has created the calibration.
        :param ~datetime.datetime datetime:
            Date and time when the calibration was created.
        :param float temperature:
            System/gas temperature [°C].
        :param float inlet_pressure:
            Absolute pressure of gas inlet [bar].
        :param float differential_pressure:
            Pressure difference between inlet and outlet [bar].
        :param bool is_real_gas_calibration:
            Whether the calibration was performed with the real process gas
            (true) or if it was calculated from a different gas (false).
        :param float accuracy_setpoint:
            Calibration accuracy in percent of the setpoint.
        :param float accuracy_fullscale:
            Calibration accuracy in percent of fullscale.
        """
        super(Sfc5xxxCalibrationConditions, self).__init__()

        #: The company which has created the calibration (str).
        self.company = company

        #: The operator who has created the calibration (str).
        self.operator = operator

        #: Date and time when the calibration was created (datetime).
        self.datetime = datetime

        #: System/gas temperature [°C] (float).
        self.temperature = temperature

        #: Absolute pressure [bar] of gas inlet (float).
        self.inlet_pressure = inlet_pressure

        #: Pressure difference [bar] between inlet and outlet (float).
        self.differential_pressure = differential_pressure

        #: Whether the calibration was performed with the real process gas
        #: (true) or if it was calculated from a different gas (false).
        self.is_real_gas_calibration = is_real_gas_calibration

        #: Calibration accuracy in percent of the setpoint (float).
        self.accuracy_setpoint = accuracy_setpoint

        #: Calibration accuracy in percent of fullscale (float).
        self.accuracy_fullscale = accuracy_fullscale

    def __str__(self):
        """
        Pretty-print the calibration information.

        :return: Multiline string representation of the calibration.
        :rtype: str
        """
        s = "Company: {}\n".format(self.company)
        s += "Operator: {}\n".format(self.operator)
        s += "Date/Time: {}\n".format(self.datetime)
        s += "Temperature: {} °C\n".format(self.temperature)
        s += "Inlet Pressure: {} bar\n".format(self.inlet_pressure)
        s += "Differential Pressure: {} bar\n".format(
            self.differential_pressure)
        s += "Is Real Gas Calibration: {}\n".format(
            'Yes' if self.is_real_gas_calibration else 'No')
        s += "Accuracy: {}% of setpoint / {}% of fullscale".format(
            round(self.accuracy_setpoint, 2),
            round(self.accuracy_fullscale, 2))
        return s


class Sfc5xxxReadBufferResponse(object):
    """
    Helper class representing the response to the "read measured value buffer"
    command, i.e. of the method
    :py:meth:`~sensirion_shdlc_sfc5xxx.device.Sfc5xxxShdlcDevice.read_measured_value_buffer`.

    The class provides some public members which you can access directly.
    """  # noqa: E501

    def __init__(self, scaling, read_count, lost_values, remaining_values,
                 sampling_time, values):
        """
        Creates an instance from the data received from the device.

        :param ~sensirion_shdlc_sfc5xxx.definitions.Sfc5xxxScaling scaling:
            With which scale resp. unit the measured flow was read (parameter
            sent to the "read measured value buffer" command).
        :param int read_count:
            How many times the "read measured value buffer" was executed
            to fetch the values contained in this object.
        :param int lost_values:
            Number of lost values (received from the "read measured value
            buffer" command).
        :param int remaining_values:
            Number of values remaining in the buffer (received from the last
            "read measured value buffer" command).
        :param float sampling_time:
            The sampling time of the measured values in Seconds (received from
            the "read measured value buffer" command).
        :param list(float) values:
            The measured values read from the buffer (received from the "read
            measured value buffer" command).
        """
        super(Sfc5xxxReadBufferResponse, self).__init__()

        #: The scaling of the measured values
        #: (:py:class:`~sensirion_shdlc_sfc5xxx.definitions.Sfc5xxxScaling`).
        self.scaling = scaling

        #: How many times the "read measured value buffer" was executed
        #: to fetch the values contained in this object (int).
        self.read_count = read_count

        #: Number of lost values due to buffer overrun (int).
        self.lost_values = lost_values

        #: Number of values remaining in the buffer after reading it (int).
        #: If the whole buffer was read out, this is zero.
        self.remaining_values = remaining_values

        #: The sampling time of the measured values in Seconds (float).
        self.sampling_time = sampling_time

        #: The measured values read from the buffer (list of float).
        self.values = values

    def __str__(self):
        """
        Pretty-print this object.

        :return: Multiline string representation of the object.
        :rtype: str
        """
        s = "Scaling: {}\n".format(self.scaling.name)
        s += "Number Of Read Commands: {}\n".format(self.read_count)
        s += "Lost Values: {}\n".format(self.lost_values)
        s += "Remaining Values: {}\n".format(self.remaining_values)
        s += "Sampling Time: {} s\n".format(round(self.sampling_time, 3))
        s += "Measured Values ({}): {}".format(len(self.values), self.values)
        return s
