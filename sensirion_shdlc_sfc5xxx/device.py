# -*- coding: utf-8 -*-
# (c) Copyright 2020 Sensirion AG, Switzerland

from __future__ import absolute_import, division, print_function
from datetime import datetime
from sensirion_shdlc_driver import ShdlcDeviceBase, ShdlcFirmwareUpdate
from sensirion_shdlc_driver.types import FirmwareVersion, HardwareVersion, \
    ProtocolVersion, Version
from .definitions import Sfc5xxxValveInputSource
from .types import Sfc5xxxCalibrationConditions, Sfc5xxxReadBufferResponse
from .units import Sfc5xxxUnitPrefix, Sfc5xxxUnit, Sfc5xxxUnitTimeBase, \
    Sfc5xxxMediumUnit
from .device_errors import SFC5XXX_DEVICE_ERROR_LIST
from .firmware_image import Sfc5xxxFirmwareImage
from .commands import \
    Sfc5xxxCmdActivateCalibration, \
    Sfc5xxxCmdDeviceReset, \
    Sfc5xxxCmdFactoryReset, \
    Sfc5xxxCmdGetArticleCode, \
    Sfc5xxxCmdGetBaudrate, \
    Sfc5xxxCmdGetCalibrationFullscale, \
    Sfc5xxxCmdGetCalibrationGasDescription, \
    Sfc5xxxCmdGetCalibrationGasId, \
    Sfc5xxxCmdGetCalibrationGasUnit, \
    Sfc5xxxCmdGetCalibrationInitialConditions, \
    Sfc5xxxCmdGetCalibrationRecalibrationConditions, \
    Sfc5xxxCmdGetCalibrationThermalConductivityReference, \
    Sfc5xxxCmdGetCalibrationValidity, \
    Sfc5xxxCmdGetCurrentFullscale, \
    Sfc5xxxCmdGetCurrentGasDescription, \
    Sfc5xxxCmdGetCurrentGasId, \
    Sfc5xxxCmdGetCurrentGasUnit, \
    Sfc5xxxCmdGetCurrentInitialCalibrationConditions, \
    Sfc5xxxCmdGetCurrentRecalibrationConditions, \
    Sfc5xxxCmdGetCurrentThermalConductivityReference, \
    Sfc5xxxCmdGetGasTemperatureCompensationEnable, \
    Sfc5xxxCmdGetInletGasTemperatureForCompensation, \
    Sfc5xxxCmdGetInletPressureForGainCorrection, \
    Sfc5xxxCmdGetNumberOfCalibrations, \
    Sfc5xxxCmdGetPressureDependentGainEnable, \
    Sfc5xxxCmdGetProductName, \
    Sfc5xxxCmdGetProductSubtype, \
    Sfc5xxxCmdGetProductType, \
    Sfc5xxxCmdGetReplyDelay, \
    Sfc5xxxCmdGetSerialNumber, \
    Sfc5xxxCmdGetSetpoint, \
    Sfc5xxxCmdGetSetpointPersist, \
    Sfc5xxxCmdGetSlaveAddress, \
    Sfc5xxxCmdGetUserControllerGain, \
    Sfc5xxxCmdGetUserDefinedFullscale, \
    Sfc5xxxCmdGetUserDefinedMediumUnit, \
    Sfc5xxxCmdGetUserDefinedMediumUnitWithoutWildcards, \
    Sfc5xxxCmdGetUserDefinedValveValue, \
    Sfc5xxxCmdGetValveInputSource, \
    Sfc5xxxCmdGetVersion, \
    Sfc5xxxCmdMeasureRawFlow, \
    Sfc5xxxCmdMeasureRawThermalConductivity, \
    Sfc5xxxCmdMeasureRawThermalConductivityWithClosedValve, \
    Sfc5xxxCmdMeasureTemperature, \
    Sfc5xxxCmdReadDeviceStatus, \
    Sfc5xxxCmdReadMeasuredValue, \
    Sfc5xxxCmdReadMeasuredValueBuffer, \
    Sfc5xxxCmdReadUserMemory, \
    Sfc5xxxCmdSetBaudrate, \
    Sfc5xxxCmdSetGasTemperatureCompensationEnable, \
    Sfc5xxxCmdSetInletGasTemperatureForCompensation, \
    Sfc5xxxCmdSetInletPressureForGainCorrection, \
    Sfc5xxxCmdSetPressureDependentGainEnable, \
    Sfc5xxxCmdSetReplyDelay, \
    Sfc5xxxCmdSetSetpoint, \
    Sfc5xxxCmdSetSetpointAndReadMeasuredValue, \
    Sfc5xxxCmdSetSetpointPersist, \
    Sfc5xxxCmdSetSlaveAddress, \
    Sfc5xxxCmdSetUserControllerGain, \
    Sfc5xxxCmdSetUserDefinedMediumUnit, \
    Sfc5xxxCmdSetUserDefinedValveValue, \
    Sfc5xxxCmdSetValveInputSource, \
    Sfc5xxxCmdWriteUserMemory

import logging
log = logging.getLogger(__name__)


class Sfc5xxxShdlcDevice(ShdlcDeviceBase):
    """
    Sfc5xxx device.

    This is a low-level driver which just provides all SHDLC commands as Python
    methods. Typically, calling a method sends one SHDLC request to the device
    and interprets its response. There is no higher level functionality
    available, please look for other drivers if you need a higher level
    interface.

    There is no (or very few) caching functionality in this driver. For example
    if you call :func:`get_serial_number` 100 times, it will send the command
    100 times over the SHDLC interface to the device. This makes the driver
    (nearly) stateless.
    """

    def __init__(self, connection, slave_address):
        """
        Create an Sfc5xxx device instance on an SHDLC connection.

        .. note:: This constructor does not communicate with the device, so
                  it's possible to instantiate an object even if the device is
                  not connected or powered yet.

        :param ~sensirion_shdlc_driver.connection.ShdlcConnection connection:
            The connection used for the communication.
        :param byte slave_address:
            The address of the device. The default address of the SFC5xxx is 0.
        """
        super(Sfc5xxxShdlcDevice, self).__init__(connection, slave_address)
        self._register_device_errors(SFC5XXX_DEVICE_ERROR_LIST)

    def get_product_type(self, as_int=False):
        """
        Get the product type. The product type (sometimes also called "device
        type") can be used to detect what kind of SHDLC product is connected.

        :param bool as_int: If ``True``, the product type is returned as an
                            integer, otherwise as a string of hexadecimal
                            digits (default).
        :return: The product type as an integer or string of hexadecimal
                 digits.
        :rtype: string/int
        """
        product_type = self.execute(Sfc5xxxCmdGetProductType())
        if as_int:
            product_type = int(product_type, 16)
        return product_type

    def get_product_subtype(self):
        """
        Get the product subtype. Some product types exist in multiple slightly
        different variants, this command allows to determine the exact variant
        of the connected device. Sometimes this is called "device subtype".

        .. note:: This command is not supported by every product type.

        :return: The product subtype as a byte (the interpretation depends on
                 the connected product type).
        :rtype: byte
        """
        return self.execute(Sfc5xxxCmdGetProductSubtype())

    def get_product_name(self):
        """
        Get the product name of the device.

        .. note:: This command is not supported by every product type.

        :return: The product name as an ASCII string.
        :rtype: string
        """
        return self.execute(Sfc5xxxCmdGetProductName())

    def get_article_code(self):
        """
        Get the article code of the device.

        .. note:: This command is not supported by every product type.

        :return: The article code as an ASCII string.
        :rtype: string
        """
        return self.execute(Sfc5xxxCmdGetArticleCode())

    def get_serial_number(self):
        """
        Get the serial number of the device.

        :return: The serial number as an ASCII string.
        :rtype: string
        """
        return self.execute(Sfc5xxxCmdGetSerialNumber())

    def get_version(self):
        """
        Get the version of the device firmware, hardware and SHDLC protocol.

        :return: The device version as a Version object.
        :rtype: Version
        """
        fw_maj, fw_min, fw_dbg, hw_maj, hw_min, pc_maj, pc_min = \
            self.execute(Sfc5xxxCmdGetVersion())
        return Version(
            firmware=FirmwareVersion(major=fw_maj, minor=fw_min, debug=fw_dbg),
            hardware=HardwareVersion(major=hw_maj, minor=hw_min),
            protocol=ProtocolVersion(major=pc_maj, minor=pc_min)
        )

    def read_device_status(self, clear=True, as_exception=False):
        """
        Read and optionally clear the device status and the last error. The
        status and error code interpretation is documented in the device
        interface specification.

        :param bool clear:
            If ``True``, the status flags on the device get cleared.
        :param bool as_exception:
            If ``True``, the last error is returned as an
            :py:class:`~sensirion_shdlc_driver.errors.ShdlcDeviceError`
            object instead of a byte.
        :return: The device status as a 32-bit unsigned integer containing all
                 status flags, and the last error which occurred on the device.
                 If ``as_exception`` is ``True``, it's returned as an
                 :py:class:`~sensirion_shdlc_driver.errors.ShdlcDeviceError`
                 object or ``None``, otherwise as a byte.
        :rtype: int, byte/ShdlcDeviceError/None
        """
        state, error = self.execute(Sfc5xxxCmdReadDeviceStatus(clear=clear))
        if as_exception:
            error = self._get_device_error(error)
        return state, error

    def get_slave_address(self):
        """
        Get the SHDLC slave address of the device.

        .. note:: See also the property
                  :py:attr:`~sensirion_shdlc_driver.device.ShdlcDevice.slave_address`
                  which returns the device's slave address without sending a
                  command. This method really sends a command to the device,
                  even though the slave address is actually already known by
                  this object.

        :return: The slave address of the device.
        :rtype: byte
        """
        return self.execute(Sfc5xxxCmdGetSlaveAddress())

    def set_slave_address(self, slave_address, update_driver=True):
        """
        Set the SHDLC slave address of the device.

        .. note:: The slave address is stored in non-volatile memory of the
                  device and thus persists after a device reset. So the next
                  time connecting to the device, you have to use the new
                  address.

        .. warning:: When changing the address of a slave, make sure there
                     isn't already a slave with that address on the same bus!
                     In that case you would get communication issues which can
                     only be fixed by disconnecting one of the slaves.

        :param byte slave_address:
            The new slave address [0..254]. The address 255 is reserved for
            broadcasts.
        :param bool update_driver:
            If ``True``, the property
            :py:attr:`~sensirion_shdlc_driver.device.ShdlcDevice.slave_address`
            of this object is also updated with the new address. This is
            needed to allow further communication with the device, as its
            address has changed.
        """
        self.execute(Sfc5xxxCmdSetSlaveAddress(slave_address))
        if update_driver:
            self._slave_address = slave_address

    def get_baudrate(self):
        """
        Get the SHDLC baudrate of the device.

        .. note:: This method really sends a command to the device, even though
                  the baudrate is already known by the used
                  :py:class:`~sensirion_shdlc_driver.port.ShdlcPort` object.

        :return: The baudrate of the device [bit/s].
        :rtype: int
        """
        return self.execute(Sfc5xxxCmdGetBaudrate())

    def set_baudrate(self, baudrate, update_driver=True):
        """
        Set the SHDLC baudrate of the device.

        .. note:: The baudrate is stored in non-volatile memory of the
                  device and thus persists after a device reset. So the next
                  time connecting to the device, you have to use the new
                  baudrate.

        .. warning:: If you pass ``True`` to the argument ``update_driver``,
                     the baudrate of the underlaying
                     :py:class:`~sensirion_shdlc_driver.port.ShdlcPort` object
                     is changed. As the baudrate applies to the whole bus (with
                     all its slaves), you might no longer be able to
                     communicate with other slaves. Generally you should change
                     the baudrate of all slaves consecutively, and only set
                     ``update_driver`` to ``True`` the last time.

        :param int baudrate:
            The new baudrate. See device documentation for a list of supported
            baudrates. Many devices support the baudrates 9600, 19200 and
            115200.
        :param bool update_driver:
            If true, the baudrate of the
            :py:class:`~sensirion_shdlc_driver.port.ShdlcPort` object is also
            updated with the baudrate. This is needed to allow further
            communication with the device, as its baudrate has changed.
        """
        self.execute(Sfc5xxxCmdSetBaudrate(baudrate))
        if update_driver:
            self._connection.port.bitrate = baudrate

    def get_reply_delay(self):
        """
        Get the SHDLC reply delay of the device.

        See
        :py:meth:`~sensirion_shdlc_driver.device.ShdlcDevice.set_reply_delay()`
        for details.

        :return: The reply delay of the device [μs].
        :rtype: byte
        """
        return self.execute(Sfc5xxxCmdGetReplyDelay())

    def set_reply_delay(self, reply_delay_us):
        """
        Set the SHDLC reply delay of the device.

        The reply delay allows to increase the minimum response time of the
        slave to a given value in Microseconds. This is needed for RS485
        masters which require some time to switch from sending to receiving.
        If the slave starts sending the response while the master is still
        driving the bus lines, a conflict on the bus occurs and communication
        fails. If you use such a slow RS485 master, you can increase the reply
        delay of all slaves to avoid this issue.

        :param byte reply_delay_us: The new reply delay [μs].
        """
        # Due to a bug in some firmware versions, reject values 0 or 1 here
        if reply_delay_us < 2:
            raise ValueError("Reply delay must be >= 2us!")
        self.execute(Sfc5xxxCmdSetReplyDelay(reply_delay_us))

    def device_reset(self):
        """
        Execute a device reset (reboot firmware, similar to power cycle).
        """
        self.execute(Sfc5xxxCmdDeviceReset())

    def factory_reset(self):
        """
        Perform a factory reset (restore the off-the-shelf factory
        configuration).

        .. warning:: This resets any configuration done after leaving the
                     factory! Keep in mind that this command might also change
                     communication parameters (i.e. baudrate and slave address)
                     and thus you might have to adjust the driver's parameters
                     to allow further communication with the device.
        """
        self.execute(Sfc5xxxCmdFactoryReset())

    def get_setpoint(self, scaling):
        """
        Get the current flow setpoint.

        :param ~sensirion_shdlc_sfc5xxx.definitions.Sfc5xxxScaling scaling:
            Defines with which scale resp. unit the setpoint should be
            returned.
        :return:
            The current setpoint with the specified scaling.
        :rtype:
            float
        """
        return self.execute(Sfc5xxxCmdGetSetpoint(int(scaling)))

    def set_setpoint(self, setpoint, scaling):
        """
        Set the flow setpoint which is used by the flow controller as reference
        input.

        :param float setpoint:
            The new setpoint with the specified scaling.
        :param ~sensirion_shdlc_sfc5xxx.definitions.Sfc5xxxScaling scaling:
            Defines with which scale resp. unit the setpoint is passed.
        """
        self.execute(Sfc5xxxCmdSetSetpoint(int(scaling), setpoint))

    def get_setpoint_persist(self):
        """
        Get the setpoint persist configuration.

        :return:
            Whether the setpoint should persist after a device reset or not.
        :rtype:
            bool
        """
        return self.execute(Sfc5xxxCmdGetSetpointPersist())

    def set_setpoint_persist(self, persist):
        """
        Set the setpoint persist configuration.

        Allows to define if a setpoint should persist after a device reset
        (soft or hardreset) or if it should be set to zero. Default is
        ``False``, i.e. the setpoint is set to zero after a device reset.

        :param bool persist:
            Whether the setpoint should persist after a reset or not.
        """
        self.execute(Sfc5xxxCmdSetSetpointPersist(persist))

    def set_setpoint_and_read_measured_value(self, setpoint, scaling):
        """
        Set the flow setpoint and return the last measured flow value in
        one command.

        This is the same as calling
        :py:meth:`~sensirion_shdlc_sfc5xxx.device.Sfc5xxxShdlcDevice.set_setpoint`
        and
        :py:meth:`~sensirion_shdlc_sfc5xxx.device.Sfc5xxxShdlcDevice.read_measured_value`,
        but it's more efficient since only one SHDLC command is executed.

        :param float setpoint:
            The new setpoint with the specified scaling.
        :param ~sensirion_shdlc_sfc5xxx.definitions.Sfc5xxxScaling scaling:
            Defines with which scale resp. unit the setpoint is passed and the
            measured flow is returned.
        :return:
            The last measured flow with the specified scaling.
        :rtype:
            float
        """
        return self.execute(Sfc5xxxCmdSetSetpointAndReadMeasuredValue(
            int(scaling), setpoint))

    def read_measured_value(self, scaling):
        """
        Read the last measured flow value.

        :param ~sensirion_shdlc_sfc5xxx.definitions.Sfc5xxxScaling scaling:
            Defines with which scale resp. unit the measured flow should be
            returned.
        :return:
            The last measured flow with the specified scaling.
        :rtype:
            float
        """
        return self.execute(Sfc5xxxCmdReadMeasuredValue(int(scaling)))

    def read_measured_value_buffer(self, scaling, max_reads=100):
        """
        Read the measured flow value buffer.

        The MFC has an internal ring buffer in which the measured flow values
        are automatically stored in a regular interval. The size of the buffer
        is between 85 and 256 (depends on the specific device configuration).
        This method sends "read buffer" commands to the device until the whole
        buffer was read out (since the SHDLC frame length is limited, it's not
        possible to read out the whole buffer with a single command). The
        received values will automatically be removed from the buffer in the
        device, so you will only get the values received since the last call
        to this method.

        .. warning:: If you call this method too rarely, the buffer in the
                     device will overrun, i.e. the oldest values are lost. You
                     should check for lost values by reading the property
                     :py:attr:`~sensirion_shdlc_sfc5xxx.types.Sfc5xxxReadBufferResponse.lost_values`
                     of the returned object. This method does not raise an
                     exception if there are values lost since depending on the
                     use-case, this might be expected behavior.

        .. note:: If the buffer gets filled faster than you read it out, it's
                  not possible to read out the whole buffer. In that case, the
                  property
                  :py:attr:`~sensirion_shdlc_sfc5xxx.types.Sfc5xxxReadBufferResponse.remaining_values`
                  of the returned object will hold a value greater than zero.
                  You might want to check this property to be sure the whole
                  buffer was read out. However, often that's not needed since
                  sooner or later you will also get a buffer overrun in this
                  situation.

        :param ~sensirion_shdlc_sfc5xxx.definitions.Sfc5xxxScaling scaling:
            Defines with which scale resp. unit the measured flow values should
            be returned.
        :param int max_reads:
            The maximum count of read commands which should be sent until the
            read operation will be aborted. This abort condition is needed to
            avoid an infinite loop if the buffer gets filled faster than it
            can be read out.
        :return:
            An object containing the buffered flow values and some metadata.
            See
            :py:class:`~sensirion_shdlc_sfc5xxx.types.Sfc5xxxReadBufferResponse`
            for details.
        :rtype:
            :py:class:`~sensirion_shdlc_sfc5xxx.types.Sfc5xxxReadBufferResponse`
        """
        read_count = 0
        total_lost_values = 0
        total_measured_values = []
        for i in range(0, max_reads):
            lost_values, remaining_values, sampling_time, measured_values = \
                self.execute(Sfc5xxxCmdReadMeasuredValueBuffer(int(scaling)))
            read_count += 1
            total_lost_values += lost_values
            total_measured_values += measured_values
            if remaining_values == 0:
                break
        return Sfc5xxxReadBufferResponse(
            scaling, read_count, total_lost_values, remaining_values,
            sampling_time, total_measured_values)

    def get_valve_input_source(self):
        """
        Get the valve input source configuration.

        :return:
            The current valve input source configuration.
        :rtype:
            ~sensirion_shdlc_sfc5xxx.definitions.Sfc5xxxValveInputSource
        """
        raw_value = self.execute(Sfc5xxxCmdGetValveInputSource())
        return Sfc5xxxValveInputSource(raw_value)

    def set_valve_input_source(self, source):
        """
        Set the valve input source configuration.

        By default, the valve is controlled by the flow controller according
        the setpoint and measured flow. But with this configuration you can
        take over the valve control and set the valve to a specific value.
        This configuration is volatile, i.e. it is reset to its default value
        after a device reset.

        .. note:: When changing the valve input source to
                  :py:attr:`~sensirion_shdlc_sfc5xxx.definitions.Sfc5xxxValveInputSource.USER_DEFINED`.
                  you also need to specify the user defined value by calling
                  the method
                  :py:meth:`~sensirion_shdlc_sfc5xxx.device.Sfc5xxxShdlcDevice.set_user_defined_valve_value`.

        :param ~sensirion_shdlc_sfc5xxx.definitions.Sfc5xxxValveInputSource source:
            The valve input source to set.
        """  # noqa: E501
        self.execute(Sfc5xxxCmdSetValveInputSource(int(source)))

    def get_user_defined_valve_value(self):
        """
        Get the current user defined valve value.

        :return:
            The current user defined valve value [0..1]. Zero means
            "fully closed", 1.0 means "fully open".
        :rtype:
            float
        """
        return self.execute(Sfc5xxxCmdGetUserDefinedValveValue())

    def set_user_defined_valve_value(self, value):
        """
        Set the user defined valve value.

        .. note:: Writing the user defined valve value has no effect as long as
                  the valve input source is not set to
                  :py:attr:`~sensirion_shdlc_sfc5xxx.definitions.Sfc5xxxValveInputSource.USER_DEFINED`.
                  So you'll also have to call
                  :py:meth:`~sensirion_shdlc_sfc5xxx.device.Sfc5xxxShdlcDevice.set_valve_input_source()`
                  to change the valve input source.

        :param float value:
            The new user defined valve value as a normalized value in the range
            [0..1]. Zero means "fully closed", 1.0 means "fully open".
        """
        self.execute(Sfc5xxxCmdSetUserDefinedValveValue(value))

    def get_user_defined_medium_unit(self, substitute_wildcards=False):
        """
        Get the currently configured user defined medium unit.

        :param bool substitute_wildcards:
            By default, the user defined medium unit is set to "undefined"
            values, which means to fall back to the calibration unit. With this
            parameter you can choose whether you want to get the actually
            configured user defined unit (which then might be undefined), or
            whether the calibration unit should be returned instead in that
            case. Default is ``False``, i.e. you will get the actual
            configuration without falling back to the calibration unit.
        :return:
            The current user defined medium unit.
        :rtype:
            ~sensirion_shdlc_sfc5xxx.units.Sfc5xxxMediumUnit
        """
        cmd = Sfc5xxxCmdGetUserDefinedMediumUnitWithoutWildcards() \
            if substitute_wildcards else Sfc5xxxCmdGetUserDefinedMediumUnit()
        raw_prefix, raw_unit, raw_timebase = self.execute(cmd)
        return Sfc5xxxMediumUnit(
            prefix=Sfc5xxxUnitPrefix.from_int(raw_prefix),
            unit=Sfc5xxxUnit.from_int(raw_unit),
            timebase=Sfc5xxxUnitTimeBase.from_int(raw_timebase),
        )

    def set_user_defined_medium_unit(self, unit):
        """
        Set the user defined medium unit.

        This is the unit which will be used when reading or writing flow values
        like setpoint or measured flow with the scaling
        :py:attr:`~sensirion_shdlc_sfc5xxx.definitions.Sfc5xxxScaling.USER_DEFINED`.
        This allows to always work with the same flow unit, no matter what's
        the actual calibration unit of the MFC.

        .. note:: This setting is stored permanently in the device, i.e. it
                  persists after a device reset.

        :param ~sensirion_shdlc_sfc5xxx.units.Sfc5xxxMediumUnit unit:
            The user defined medium unit to set.
        """
        self.execute(Sfc5xxxCmdSetUserDefinedMediumUnit(
            prefix=unit.prefix.value,
            unit=unit.unit.value,
            timebase=unit.timebase.value,
        ))

    def get_user_defined_fullscale(self):
        """
        Get the fullscale flow in the currently set user defined unit.

        :return:
            The fullscale flow in the current user defined unit.
        :rtype:
            float
        """
        return self.execute(Sfc5xxxCmdGetUserDefinedFullscale())

    def get_user_controller_gain(self):
        """
        Get the current user controller gain.

        :return:
            The current user controller gain (normalized value, default 1.0).
        :rtype:
            float
        """
        return self.execute(Sfc5xxxCmdGetUserControllerGain())

    def set_user_controller_gain(self, gain):
        """
        Set the current user controller gain.

        This allows to adjust the speed of the flow controller by changing its
        overall gain.

        .. note:: This value is stored permanently in the device, i.e. it
                  persists after a device reset.

        :param float gain:
            The new gain to set (normalized value, default 1.0).
        """
        self.execute(Sfc5xxxCmdSetUserControllerGain(gain))

    def get_pressure_dependent_gain_enable(self):
        """
        Get the state of the pressure dependent gain setting.

        :return:
            Whether the pressure dependent gain is enabled or not.
        :rtype:
            bool
        """
        return self.execute(Sfc5xxxCmdGetPressureDependentGainEnable())

    def set_pressure_dependent_gain_enable(self, enable):
        """
        Set the state of the pressure dependent gain setting.

        If the pressure dependent gain is enabled, you'll have to set the
        actual inlet pressure with the method
        :py:meth:`~sensirion_shdlc_sfc5xxx.device.Sfc5xxxShdlcDevice.set_inlet_pressure_for_gain_correction()`.

        .. note:: This value is stored permanently in the device, i.e. it
                  persists after a device reset.

        :param bool enable:
            Whether the pressure dependent gain should be enabled or not.
        """
        self.execute(Sfc5xxxCmdSetPressureDependentGainEnable(enable))

    def get_inlet_pressure_for_gain_correction(self):
        """
        Get the currently configured inlet pressure as used for the pressure
        dependent controller gain.

        :return:
            The currently configured inlet pressure [bar].
        :rtype:
            float
        """
        return self.execute(Sfc5xxxCmdGetInletPressureForGainCorrection())

    def set_inlet_pressure_for_gain_correction(self, pressure):
        """
        Set the inlet pressure used for the pressure dependent controller gain.

        .. note:: This value is stored permanently in the device, i.e. it
                  persists after a device reset.

        :param float pressure:
            The new pressure [bar] to set.
        """
        self.execute(Sfc5xxxCmdSetInletPressureForGainCorrection(pressure))

    def get_gas_temperature_compensation_enable(self):
        """
        Get the state of the gas temperature compensation setting.

        :return:
            Whether the gas temperature compensation is enabled or not.
        :rtype:
            bool
        """
        return self.execute(Sfc5xxxCmdGetGasTemperatureCompensationEnable())

    def set_gas_temperature_compensation_enable(self, enable):
        """
        Set the state of the gas temperature compensation setting.

        If the gas temperature compensation is enabled, you'll have to set the
        actual inlet gas temperature with the method
        :py:meth:`~sensirion_shdlc_sfc5xxx.device.Sfc5xxxShdlcDevice.set_inlet_gas_temperature_for_compensation()`.

        .. note:: This value is stored permanently in the device, i.e. it
                  persists after a device reset.

        :param bool enable:
            Whether the gas temperature compensation should be enabled or not.
        """
        self.execute(Sfc5xxxCmdSetGasTemperatureCompensationEnable(enable))

    def get_inlet_gas_temperature_for_compensation(self):
        """
        Get the currently configured inlet gas temperature as used for the
        gas temperature compensation.

        :return:
            The currently configured inlet gas temperature [°C].
        :rtype:
            float
        """
        return self.execute(Sfc5xxxCmdGetInletGasTemperatureForCompensation())

    def set_inlet_gas_temperature_for_compensation(self, temperature):
        """
        Set the inlet gas temperature used for the gas temperature
        compensation.

        .. note:: This value is stored permanently in the device, i.e. it
                  persists after a device reset.

        :param float temperature:
            The new temperature [°C] to set.
        """
        self.execute(
            Sfc5xxxCmdSetInletGasTemperatureForCompensation(temperature))

    def measure_raw_flow(self):
        """
        Measure the raw flow ticks.

        :return:
            Measured raw flow ticks.
        :rtype:
            int
        """
        return self.execute(Sfc5xxxCmdMeasureRawFlow())

    def measure_temperature(self):
        """
        Measure the sensor temperature.

        :return:
            Measured temperature [°C].
        :rtype:
            float
        """
        return self.execute(Sfc5xxxCmdMeasureTemperature())

    def measure_raw_thermal_conductivity(self, close_valve=True):
        """
        Measure the raw thermal conductivity.

        :param bool close_valve:
            If ``True`` (default), the valve will be forcibly closed for
            500ms before measuring the thermal conductivity. This is needed
            to guarantee a correct and stable measurement. If you are sure that
            the valve is closed anyway, you could set this to ``False`` to
            speed up the measurement.
        :return:
            Measured raw thermal conductivity ticks.
        :rtype:
            int
        """
        cmd = Sfc5xxxCmdMeasureRawThermalConductivityWithClosedValve() \
            if close_valve else Sfc5xxxCmdMeasureRawThermalConductivity()
        return self.execute(cmd)

    def get_number_of_calibrations(self):
        """
        Get the number of possible calibrations. Each calibration can either
        contain a valid calibration or not. Use
        :py:meth:`~sensirion_shdlc_sfc5xxx.device.Sfc5xxxDevice.get_calibration_validity`
        to determine which indices contain a valid calibration.

        :return:
            The number of calibrations the device memory can hold.
        :rtype:
            int
        """
        return self.execute(Sfc5xxxCmdGetNumberOfCalibrations())

    def get_calibration_validity(self, index):
        """
        Check whether there exists a valid calibration block at a specific
        index or not.

        :param int index:
            The index of the calibration to check.
        :return:
            Whether at the specified index exists a valid calibration block or
            not.
        :rtype:
            bool
        """
        return self.execute(Sfc5xxxCmdGetCalibrationValidity(index))

    def get_calibration_gas_description(self, index):
        """
        Get the gas description of a specific calibration index.

        :param int index:
            The index of the calibration to read from.
        :return:
            Gas description string.
        :rtype:
            str
        """
        return self.execute(Sfc5xxxCmdGetCalibrationGasDescription(index))

    def get_calibration_gas_id(self, index):
        """
        Get the gas ID of a specific calibration index.

        :param int index:
            The index of the calibration to read from.
        :return:
            Gas ID.
        :rtype:
            int
        """
        return self.execute(Sfc5xxxCmdGetCalibrationGasId(index))

    def get_calibration_gas_unit(self, index):
        """
        Get the gas unit of a specific calibration index.

        :param int index:
            The index of the calibration to read from.
        :return:
            Gas unit.
        :rtype:
            ~sensirion_shdlc_sfc5xxx.units.Sfc5xxxMediumUnit
        """
        raw_prefix, raw_unit, raw_timebase = \
            self.execute(Sfc5xxxCmdGetCalibrationGasUnit(index))
        return Sfc5xxxMediumUnit(
            prefix=Sfc5xxxUnitPrefix.from_int(raw_prefix),
            unit=Sfc5xxxUnit.from_int(raw_unit),
            timebase=Sfc5xxxUnitTimeBase.from_int(raw_timebase),
        )

    def get_calibration_fullscale(self, index):
        """
        Get the fullscale flow of a specific calibration index.

        :param int index:
            The index of the calibration to read from.
        :return:
            Fullscale flow in the unit of the calibration.
        :rtype:
            float
        """
        return self.execute(Sfc5xxxCmdGetCalibrationFullscale(index))

    def get_calibration_initial_conditions(self, index):
        """
        Get the initial calibration conditions of a specific calibration index.

        :param int index:
            The index of the calibration to read from.
        :return:
            Initial calibration conditions.
        :rtype:
            ~sensirion_shdlc_sfc5xxx.types.Sfc5xxxCalibrationConditions
        """
        company, operator, year, month, day, hour, minute, temperature, \
            inlet_pressure, differential_pressure, is_real_gas_calibration, \
            accuracy_setpoint, accuracy_fullscale = self.execute(
                Sfc5xxxCmdGetCalibrationInitialConditions(index))
        return Sfc5xxxCalibrationConditions(
            company=company,
            operator=operator,
            datetime=datetime(year, month, day, hour, minute),
            temperature=temperature,
            inlet_pressure=inlet_pressure,
            differential_pressure=differential_pressure,
            is_real_gas_calibration=is_real_gas_calibration,
            accuracy_setpoint=accuracy_setpoint,
            accuracy_fullscale=accuracy_fullscale,
        )

    def get_calibration_recalibration_conditions(self, index):
        """
        Get the recalibration conditions of a specific calibration index.

        :param int index:
            The index of the calibration to read from.
        :return:
            Recalibration conditions.
        :rtype:
            ~sensirion_shdlc_sfc5xxx.types.Sfc5xxxCalibrationConditions
        """
        company, operator, year, month, day, hour, minute, temperature, \
            inlet_pressure, differential_pressure, is_real_gas_calibration, \
            accuracy_setpoint, accuracy_fullscale = self.execute(
                Sfc5xxxCmdGetCalibrationRecalibrationConditions(index))
        return Sfc5xxxCalibrationConditions(
            company=company,
            operator=operator,
            datetime=datetime(year, month, day, hour, minute),
            temperature=temperature,
            inlet_pressure=inlet_pressure,
            differential_pressure=differential_pressure,
            is_real_gas_calibration=is_real_gas_calibration,
            accuracy_setpoint=accuracy_setpoint,
            accuracy_fullscale=accuracy_fullscale,
        )

    def get_calibration_thermal_conductivity_reference(self, index):
        """
        Get the thermal conductivity reference value of a specific
        calibration index.

        :param int index:
            The index of the calibration to read from.
        :return:
            Thermal conductivity reference value ticks.
        :rtype:
            int
        """
        return self.execute(
            Sfc5xxxCmdGetCalibrationThermalConductivityReference(index))

    def get_current_gas_description(self):
        """
        Get the gas description of the currently active calibration.

        :return:
            Gas description string.
        :rtype:
            str
        """
        return self.execute(Sfc5xxxCmdGetCurrentGasDescription())

    def get_current_gas_id(self):
        """
        Get the gas ID of the currently active calibration.

        :return:
            Gas ID.
        :rtype:
            int
        """
        return self.execute(Sfc5xxxCmdGetCurrentGasId())

    def get_current_gas_unit(self):
        """
        Get the gas unit of the currently active calibration.

        :return:
            Gas unit.
        :rtype:
            ~sensirion_shdlc_sfc5xxx.units.Sfc5xxxMediumUnit
        """
        raw_prefix, raw_unit, raw_timebase = \
            self.execute(Sfc5xxxCmdGetCurrentGasUnit())
        return Sfc5xxxMediumUnit(
            prefix=Sfc5xxxUnitPrefix.from_int(raw_prefix),
            unit=Sfc5xxxUnit.from_int(raw_unit),
            timebase=Sfc5xxxUnitTimeBase.from_int(raw_timebase),
        )

    def get_current_fullscale(self):
        """
        Get the fullscale flow of the currently active calibration.

        :return:
            Fullscale flow in the unit of the calibration.
        :rtype:
            float
        """
        return self.execute(Sfc5xxxCmdGetCurrentFullscale())

    def get_current_initial_calibration_conditions(self):
        """
        Get the initial calibration conditions of the currently active
        calibration.

        :return:
            Initial calibration conditions.
        :rtype:
            ~sensirion_shdlc_sfc5xxx.types.Sfc5xxxCalibrationConditions
        """
        company, operator, year, month, day, hour, minute, temperature, \
            inlet_pressure, differential_pressure, is_real_gas_calibration, \
            accuracy_setpoint, accuracy_fullscale = self.execute(
                Sfc5xxxCmdGetCurrentInitialCalibrationConditions())
        return Sfc5xxxCalibrationConditions(
            company=company,
            operator=operator,
            datetime=datetime(year, month, day, hour, minute),
            temperature=temperature,
            inlet_pressure=inlet_pressure,
            differential_pressure=differential_pressure,
            is_real_gas_calibration=is_real_gas_calibration,
            accuracy_setpoint=accuracy_setpoint,
            accuracy_fullscale=accuracy_fullscale,
        )

    def get_current_recalibration_conditions(self):
        """
        Get the recalibration conditions of the currently active calibration.

        :return:
            Recalibration conditions.
        :rtype:
            ~sensirion_shdlc_sfc5xxx.types.Sfc5xxxCalibrationConditions
        """
        company, operator, year, month, day, hour, minute, temperature, \
            inlet_pressure, differential_pressure, is_real_gas_calibration, \
            accuracy_setpoint, accuracy_fullscale = self.execute(
                Sfc5xxxCmdGetCurrentRecalibrationConditions())
        return Sfc5xxxCalibrationConditions(
            company=company,
            operator=operator,
            datetime=datetime(year, month, day, hour, minute),
            temperature=temperature,
            inlet_pressure=inlet_pressure,
            differential_pressure=differential_pressure,
            is_real_gas_calibration=is_real_gas_calibration,
            accuracy_setpoint=accuracy_setpoint,
            accuracy_fullscale=accuracy_fullscale,
        )

    def get_current_thermal_conductivity_reference(self):
        """
        Get the thermal conductivity reference value of the currently active
        calibration.

        :return:
            Thermal conductivity reference value ticks.
        :rtype:
            int
        """
        return self.execute(Sfc5xxxCmdGetCurrentThermalConductivityReference())

    def activate_calibration(self, index):
        """
        Activate a specific gas calibration block and run the flow controller.

        :param int index:
            The  index of the calibration to activate.
        """
        self.execute(Sfc5xxxCmdActivateCalibration(index))

    def read_user_memory(self, address, length):
        """
        Read data from the user memory.

        :param int address:
            The address to read from.
        :param int length:
            Number of bytes to read.
        :return:
            The read data.
        :rtype:
            bytes
        """
        return self.execute(Sfc5xxxCmdReadUserMemory(address, length))

    def write_user_memory(self, address, data):
        """
        Write data to the user memory.

        :param int address:
            The address to write to.
        :param bytes-like data:
            Data to write.
        """
        self.execute(Sfc5xxxCmdWriteUserMemory(address, len(data), data))

    def update_firmware(self, image, emergency=False, status_callback=None,
                        progress_callback=None):
        """Update the firmware on the device.

        This method allows you to download a new firmware (provided as a
        \\*.hex file) to the device. A device reset is performed after the
        firmware update.

        .. note:: This can take several minutes, don't abort it! If aborted,
                  the device stays in the bootloader and you need to restart
                  the update with ``emergency=True`` to recover.

        .. warning:: If the Sfc5xxx is connected through RS485
                     together with other SHDLC devices on the same bus, make
                     sure that no other device has the slave address 0 and
                     baudrate 115200! These connection settings are used by
                     the bootloader and thus two devices would respond to the
                     bootloader commands. If an update fails because of this,
                     you will have to disconnect the other device with address
                     0 and do an emergency update to recover this device.

        :param image:
            The image to flash, either as a
            :py::class:`~sensirion_shdlc_sfc5xxx.firmware_image.Sfc5xxxFirmwareImage`
            object, a file-like object, or the filename (``str``) to the
            \\*.hex file.
        :param bool emergency:
            Must be set to ``True`` if the device is already in bootloader
            mode, ``False`` otherwise.
        :param callable status_callback:
            Optional callback for status report, taking a string as parameter.
        :param callable progress_callback:
            Optional callback for progress report, taking a float as parameter
            (progress in percent).
        :raises ~sensirion_shdlc_driver.errors.ShdlcFirmwareImageIncompatibilityError:
            If the image is not compatible with the connected device.
        :raises Exception:
            On other errors.
        """  # noqa: E501
        if not isinstance(image, Sfc5xxxFirmwareImage):
            image = Sfc5xxxFirmwareImage(image)
        update = ShdlcFirmwareUpdate(self, image,
                                     status_callback=status_callback,
                                     progress_callback=progress_callback)
        update.execute(emergency=emergency)
