API Reference
=============

Sfc5xxxShdlcDevice
------------------

.. automodule:: sensirion_shdlc_sfc5xxx.device


Sfc5xxxFirmwareImage
--------------------

.. automodule:: sensirion_shdlc_sfc5xxx.firmware_image


Definitions
-----------

Sfc5xxxScaling
^^^^^^^^^^^^^^

.. autoclass:: sensirion_shdlc_sfc5xxx.definitions.Sfc5xxxScaling

Sfc5xxxValveInputSource
^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: sensirion_shdlc_sfc5xxx.definitions.Sfc5xxxValveInputSource


Units
-----

Sfc5xxxUnitPrefix
^^^^^^^^^^^^^^^^^

.. autoclass:: sensirion_shdlc_sfc5xxx.units.Sfc5xxxUnitPrefix

Sfc5xxxUnit
^^^^^^^^^^^

.. autoclass:: sensirion_shdlc_sfc5xxx.units.Sfc5xxxUnit

Sfc5xxxUnitTimeBase
^^^^^^^^^^^^^^^^^^^

.. autoclass:: sensirion_shdlc_sfc5xxx.units.Sfc5xxxUnitTimeBase

Sfc5xxxMediumUnit
^^^^^^^^^^^^^^^^^

.. autoclass:: sensirion_shdlc_sfc5xxx.units.Sfc5xxxMediumUnit


Types
-----

Sfc5xxxCalibrationConditions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: sensirion_shdlc_sfc5xxx.types.Sfc5xxxCalibrationConditions

Sfc5xxxReadBufferResponse
^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: sensirion_shdlc_sfc5xxx.types.Sfc5xxxReadBufferResponse


Device Errors
-------------

.. automodule:: sensirion_shdlc_sfc5xxx.device_errors
    :exclude-members: __init__


Commands
--------

Sfc5xxxCmdActivateCalibration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: sensirion_shdlc_sfc5xxx.commands.activate_calibration.Sfc5xxxCmdActivateCalibration
    :exclude-members: __init__

Sfc5xxxCmdMeasureRawFlow
^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: sensirion_shdlc_sfc5xxx.commands.advanced_measurements.Sfc5xxxCmdMeasureRawFlow
    :exclude-members: __init__

Sfc5xxxCmdMeasureRawThermalConductivity
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: sensirion_shdlc_sfc5xxx.commands.advanced_measurements.Sfc5xxxCmdMeasureRawThermalConductivity
    :exclude-members: __init__

Sfc5xxxCmdMeasureRawThermalConductivityWithClosedValve
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: sensirion_shdlc_sfc5xxx.commands.advanced_measurements.Sfc5xxxCmdMeasureRawThermalConductivityWithClosedValve
    :exclude-members: __init__

Sfc5xxxCmdMeasureTemperature
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: sensirion_shdlc_sfc5xxx.commands.advanced_measurements.Sfc5xxxCmdMeasureTemperature
    :exclude-members: __init__

Sfc5xxxCmdGetBaudrate
^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: sensirion_shdlc_sfc5xxx.commands.baudrate.Sfc5xxxCmdGetBaudrate
    :exclude-members: __init__

Sfc5xxxCmdSetBaudrate
^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: sensirion_shdlc_sfc5xxx.commands.baudrate.Sfc5xxxCmdSetBaudrate
    :exclude-members: __init__

Sfc5xxxCmdGetUserControllerGain
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: sensirion_shdlc_sfc5xxx.commands.controller_configuration.Sfc5xxxCmdGetUserControllerGain
    :exclude-members: __init__

Sfc5xxxCmdSetUserControllerGain
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: sensirion_shdlc_sfc5xxx.commands.controller_configuration.Sfc5xxxCmdSetUserControllerGain
    :exclude-members: __init__

Sfc5xxxCmdGetPressureDependentGainEnable
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: sensirion_shdlc_sfc5xxx.commands.controller_configuration.Sfc5xxxCmdGetPressureDependentGainEnable
    :exclude-members: __init__

Sfc5xxxCmdSetPressureDependentGainEnable
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: sensirion_shdlc_sfc5xxx.commands.controller_configuration.Sfc5xxxCmdSetPressureDependentGainEnable
    :exclude-members: __init__

Sfc5xxxCmdGetInletPressureForGainCorrection
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: sensirion_shdlc_sfc5xxx.commands.controller_configuration.Sfc5xxxCmdGetInletPressureForGainCorrection
    :exclude-members: __init__

Sfc5xxxCmdSetInletPressureForGainCorrection
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: sensirion_shdlc_sfc5xxx.commands.controller_configuration.Sfc5xxxCmdSetInletPressureForGainCorrection
    :exclude-members: __init__

Sfc5xxxCmdGetGasTemperatureCompensationEnable
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: sensirion_shdlc_sfc5xxx.commands.controller_configuration.Sfc5xxxCmdGetGasTemperatureCompensationEnable
    :exclude-members: __init__

Sfc5xxxCmdSetGasTemperatureCompensationEnable
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: sensirion_shdlc_sfc5xxx.commands.controller_configuration.Sfc5xxxCmdSetGasTemperatureCompensationEnable
    :exclude-members: __init__

Sfc5xxxCmdGetInletGasTemperatureForCompensation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: sensirion_shdlc_sfc5xxx.commands.controller_configuration.Sfc5xxxCmdGetInletGasTemperatureForCompensation
    :exclude-members: __init__

Sfc5xxxCmdSetInletGasTemperatureForCompensation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: sensirion_shdlc_sfc5xxx.commands.controller_configuration.Sfc5xxxCmdSetInletGasTemperatureForCompensation
    :exclude-members: __init__

Sfc5xxxCmdGetProductType
^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: sensirion_shdlc_sfc5xxx.commands.device_information.Sfc5xxxCmdGetProductType
    :exclude-members: __init__

Sfc5xxxCmdGetProductName
^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: sensirion_shdlc_sfc5xxx.commands.device_information.Sfc5xxxCmdGetProductName
    :exclude-members: __init__

Sfc5xxxCmdGetArticleCode
^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: sensirion_shdlc_sfc5xxx.commands.device_information.Sfc5xxxCmdGetArticleCode
    :exclude-members: __init__

Sfc5xxxCmdGetSerialNumber
^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: sensirion_shdlc_sfc5xxx.commands.device_information.Sfc5xxxCmdGetSerialNumber
    :exclude-members: __init__

Sfc5xxxCmdGetProductSubtype
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: sensirion_shdlc_sfc5xxx.commands.device_information.Sfc5xxxCmdGetProductSubtype
    :exclude-members: __init__

Sfc5xxxCmdDeviceReset
^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: sensirion_shdlc_sfc5xxx.commands.device_reset.Sfc5xxxCmdDeviceReset
    :exclude-members: __init__

Sfc5xxxCmdFactoryReset
^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: sensirion_shdlc_sfc5xxx.commands.factory_reset.Sfc5xxxCmdFactoryReset
    :exclude-members: __init__

Sfc5xxxCmdGetNumberOfCalibrations
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: sensirion_shdlc_sfc5xxx.commands.get_calibration_information.Sfc5xxxCmdGetNumberOfCalibrations
    :exclude-members: __init__

Sfc5xxxCmdGetCalibrationValidity
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: sensirion_shdlc_sfc5xxx.commands.get_calibration_information.Sfc5xxxCmdGetCalibrationValidity
    :exclude-members: __init__

Sfc5xxxCmdGetCalibrationGasDescription
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: sensirion_shdlc_sfc5xxx.commands.get_calibration_information.Sfc5xxxCmdGetCalibrationGasDescription
    :exclude-members: __init__

Sfc5xxxCmdGetCalibrationGasId
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: sensirion_shdlc_sfc5xxx.commands.get_calibration_information.Sfc5xxxCmdGetCalibrationGasId
    :exclude-members: __init__

Sfc5xxxCmdGetCalibrationGasUnit
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: sensirion_shdlc_sfc5xxx.commands.get_calibration_information.Sfc5xxxCmdGetCalibrationGasUnit
    :exclude-members: __init__

Sfc5xxxCmdGetCalibrationFullscale
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: sensirion_shdlc_sfc5xxx.commands.get_calibration_information.Sfc5xxxCmdGetCalibrationFullscale
    :exclude-members: __init__

Sfc5xxxCmdGetCalibrationInitialConditions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: sensirion_shdlc_sfc5xxx.commands.get_calibration_information.Sfc5xxxCmdGetCalibrationInitialConditions
    :exclude-members: __init__

Sfc5xxxCmdGetCalibrationRecalibrationConditions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: sensirion_shdlc_sfc5xxx.commands.get_calibration_information.Sfc5xxxCmdGetCalibrationRecalibrationConditions
    :exclude-members: __init__

Sfc5xxxCmdGetCalibrationThermalConductivityReference
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: sensirion_shdlc_sfc5xxx.commands.get_calibration_information.Sfc5xxxCmdGetCalibrationThermalConductivityReference
    :exclude-members: __init__

Sfc5xxxCmdGetCurrentGasDescription
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: sensirion_shdlc_sfc5xxx.commands.get_current_calibration_information.Sfc5xxxCmdGetCurrentGasDescription
    :exclude-members: __init__

Sfc5xxxCmdGetCurrentGasId
^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: sensirion_shdlc_sfc5xxx.commands.get_current_calibration_information.Sfc5xxxCmdGetCurrentGasId
    :exclude-members: __init__

Sfc5xxxCmdGetCurrentGasUnit
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: sensirion_shdlc_sfc5xxx.commands.get_current_calibration_information.Sfc5xxxCmdGetCurrentGasUnit
    :exclude-members: __init__

Sfc5xxxCmdGetCurrentFullscale
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: sensirion_shdlc_sfc5xxx.commands.get_current_calibration_information.Sfc5xxxCmdGetCurrentFullscale
    :exclude-members: __init__

Sfc5xxxCmdGetCurrentInitialCalibrationConditions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: sensirion_shdlc_sfc5xxx.commands.get_current_calibration_information.Sfc5xxxCmdGetCurrentInitialCalibrationConditions
    :exclude-members: __init__

Sfc5xxxCmdGetCurrentRecalibrationConditions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: sensirion_shdlc_sfc5xxx.commands.get_current_calibration_information.Sfc5xxxCmdGetCurrentRecalibrationConditions
    :exclude-members: __init__

Sfc5xxxCmdGetCurrentThermalConductivityReference
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: sensirion_shdlc_sfc5xxx.commands.get_current_calibration_information.Sfc5xxxCmdGetCurrentThermalConductivityReference
    :exclude-members: __init__

Sfc5xxxCmdGetVersion
^^^^^^^^^^^^^^^^^^^^

.. autoclass:: sensirion_shdlc_sfc5xxx.commands.get_version.Sfc5xxxCmdGetVersion
    :exclude-members: __init__

Sfc5xxxCmdGetUserDefinedMediumUnit
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: sensirion_shdlc_sfc5xxx.commands.medium_unit_configuration.Sfc5xxxCmdGetUserDefinedMediumUnit
    :exclude-members: __init__

Sfc5xxxCmdSetUserDefinedMediumUnit
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: sensirion_shdlc_sfc5xxx.commands.medium_unit_configuration.Sfc5xxxCmdSetUserDefinedMediumUnit
    :exclude-members: __init__

Sfc5xxxCmdGetUserDefinedMediumUnitWithoutWildcards
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: sensirion_shdlc_sfc5xxx.commands.medium_unit_configuration.Sfc5xxxCmdGetUserDefinedMediumUnitWithoutWildcards
    :exclude-members: __init__

Sfc5xxxCmdGetUserDefinedFullscale
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: sensirion_shdlc_sfc5xxx.commands.medium_unit_configuration.Sfc5xxxCmdGetUserDefinedFullscale
    :exclude-members: __init__

Sfc5xxxCmdReadDeviceStatus
^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: sensirion_shdlc_sfc5xxx.commands.read_device_status.Sfc5xxxCmdReadDeviceStatus
    :exclude-members: __init__

Sfc5xxxCmdReadMeasuredValue
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: sensirion_shdlc_sfc5xxx.commands.read_measured_value.Sfc5xxxCmdReadMeasuredValue
    :exclude-members: __init__

Sfc5xxxCmdReadMeasuredValueBuffer
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: sensirion_shdlc_sfc5xxx.commands.read_measured_value_buffer.Sfc5xxxCmdReadMeasuredValueBuffer
    :exclude-members: __init__

Sfc5xxxCmdGetReplyDelay
^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: sensirion_shdlc_sfc5xxx.commands.reply_delay.Sfc5xxxCmdGetReplyDelay
    :exclude-members: __init__

Sfc5xxxCmdSetReplyDelay
^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: sensirion_shdlc_sfc5xxx.commands.reply_delay.Sfc5xxxCmdSetReplyDelay
    :exclude-members: __init__

Sfc5xxxCmdSetSetpointAndReadMeasuredValue
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: sensirion_shdlc_sfc5xxx.commands.set_setpoint_and_read_measured_value.Sfc5xxxCmdSetSetpointAndReadMeasuredValue
    :exclude-members: __init__

Sfc5xxxCmdGetSetpoint
^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: sensirion_shdlc_sfc5xxx.commands.setpoint.Sfc5xxxCmdGetSetpoint
    :exclude-members: __init__

Sfc5xxxCmdSetSetpoint
^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: sensirion_shdlc_sfc5xxx.commands.setpoint.Sfc5xxxCmdSetSetpoint
    :exclude-members: __init__

Sfc5xxxCmdSetSetpointPersist
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: sensirion_shdlc_sfc5xxx.commands.setpoint_persist.Sfc5xxxCmdSetSetpointPersist
    :exclude-members: __init__

Sfc5xxxCmdGetSetpointPersist
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: sensirion_shdlc_sfc5xxx.commands.setpoint_persist.Sfc5xxxCmdGetSetpointPersist
    :exclude-members: __init__

Sfc5xxxCmdGetSlaveAddress
^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: sensirion_shdlc_sfc5xxx.commands.slave_address.Sfc5xxxCmdGetSlaveAddress
    :exclude-members: __init__

Sfc5xxxCmdSetSlaveAddress
^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: sensirion_shdlc_sfc5xxx.commands.slave_address.Sfc5xxxCmdSetSlaveAddress
    :exclude-members: __init__

Sfc5xxxCmdReadUserMemory
^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: sensirion_shdlc_sfc5xxx.commands.user_memory_access.Sfc5xxxCmdReadUserMemory
    :exclude-members: __init__

Sfc5xxxCmdWriteUserMemory
^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: sensirion_shdlc_sfc5xxx.commands.user_memory_access.Sfc5xxxCmdWriteUserMemory
    :exclude-members: __init__

Sfc5xxxCmdGetValveInputSource
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: sensirion_shdlc_sfc5xxx.commands.valve_input_source_configuration.Sfc5xxxCmdGetValveInputSource
    :exclude-members: __init__

Sfc5xxxCmdSetValveInputSource
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: sensirion_shdlc_sfc5xxx.commands.valve_input_source_configuration.Sfc5xxxCmdSetValveInputSource
    :exclude-members: __init__

Sfc5xxxCmdGetUserDefinedValveValue
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: sensirion_shdlc_sfc5xxx.commands.valve_input_source_configuration.Sfc5xxxCmdGetUserDefinedValveValue
    :exclude-members: __init__

Sfc5xxxCmdSetUserDefinedValveValue
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: sensirion_shdlc_sfc5xxx.commands.valve_input_source_configuration.Sfc5xxxCmdSetUserDefinedValveValue
    :exclude-members: __init__
