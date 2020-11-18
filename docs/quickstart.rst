Quick Start
===========

Following example code shows how the driver is intended to use:

.. sourcecode:: python

    # -*- coding: utf-8 -*-
    import time
    from sensirion_shdlc_driver import ShdlcSerialPort, ShdlcConnection
    from sensirion_shdlc_sfc5xxx import Sfc5xxxShdlcDevice, Sfc5xxxScaling, \
        Sfc5xxxValveInputSource, Sfc5xxxUnitPrefix, Sfc5xxxUnit, \
        Sfc5xxxUnitTimeBase, Sfc5xxxMediumUnit

    # Connect to the device with default settings:
    #  - baudrate:      115200
    #  - slave address: 0
    with ShdlcSerialPort(port='COM1', baudrate=115200) as port:
        device = Sfc5xxxShdlcDevice(ShdlcConnection(port), slave_address=0)

        # Print some device information
        print("Version: {}".format(device.get_version()))
        print("Product Name: {}".format(device.get_product_name()))
        print("Article Code: {}".format(device.get_article_code()))
        print("Serial Number: {}".format(device.get_serial_number()))

        # List all available calibration blocks
        print("Available gas calibration blocks:")
        for i in range(device.get_number_of_calibrations()):
            if device.get_calibration_validity(i):
                gas = device.get_calibration_gas_description(i)
                fullscale = device.get_calibration_fullscale(i)
                unit = device.get_calibration_gas_unit(i)
                print(" - {}: {:.2f} {} {}".format(i, fullscale, unit, gas))

        # Select gas calibration 0 (usually there is a calibration at index 0)
        device.activate_calibration(0)

        # Get some information about the currently active gas calibration
        print("Calibration Gas: {}".format(device.get_current_gas_description()))
        print("Calibration Fullscale: {}".format(device.get_current_fullscale()))
        print("Calibration Unit: {}".format(device.get_current_gas_unit()))

        # Set user defined flow unit to sccm so we don't have to care about
        # the actual calibration unit of the connected MFC
        unit = Sfc5xxxMediumUnit(
            Sfc5xxxUnitPrefix.MILLI,
            Sfc5xxxUnit.STANDARD_LITER,
            Sfc5xxxUnitTimeBase.MINUTE
        )
        device.set_user_defined_medium_unit(unit)

        # Get the flow fullscale in the user defined medium unit (i.e. sccm)
        fullscale = device.get_user_defined_fullscale()
        print("Fullscale: {:.2f} {}".format(fullscale, unit))

        # Set flow setpoint to 100sccm
        device.set_setpoint(100, Sfc5xxxScaling.USER_DEFINED)

        # Read single flow value
        flow = device.read_measured_value(Sfc5xxxScaling.USER_DEFINED)
        print("Measured Flow: {:.2f} {}".format(flow, unit))

        # Read single temperature value
        temperature = device.measure_temperature()
        print("Measured Temperature: {:.2f} °C".format(temperature))

        # Read whole flow value buffer
        buffer = device.read_measured_value_buffer(Sfc5xxxScaling.USER_DEFINED)
        print("Lost Values (Buffer Overrun): {}".format(buffer.lost_values))
        print("Sampling Time of Values: {:.3f} s".format(buffer.sampling_time))
        print("Buffered Flow Values: {}".format(buffer.values))

        # Purge system by fully opening the valve for 1s
        device.set_valve_input_source(Sfc5xxxValveInputSource.FORCE_OPEN)
        time.sleep(1.0)
        device.set_valve_input_source(Sfc5xxxValveInputSource.CONTROLLER)

        # Perform a device reset (reboot firmware)
        device.device_reset()
