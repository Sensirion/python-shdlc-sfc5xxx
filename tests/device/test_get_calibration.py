# -*- coding: utf-8 -*-
# (c) Copyright 2020 Sensirion AG, Switzerland

from __future__ import absolute_import, division, print_function
from sensirion_shdlc_sfc5xxx import Sfc5xxxMediumUnit
from sensirion_shdlc_sfc5xxx.types import Sfc5xxxCalibrationConditions
from sensirion_shdlc_sfc5xxx.device_errors import \
    Sfc5xxxInvalidCalibrationIndexError
import pytest


@pytest.mark.needs_device
def test(device):
    """
    Test if the get_calibration_*() methods work as expected.
    """
    number = device.get_number_of_calibrations()
    assert type(number) is int
    assert 10 <= number <= 100

    for i in range(number):
        valid = device.get_calibration_validity(i)
        assert type(valid) is bool

        if valid:
            result = device.get_calibration_gas_description(i)
            assert type(result) is str
            result = device.get_calibration_gas_id(i)
            assert type(result) is int
            result = device.get_calibration_gas_unit(i)
            assert type(result) is Sfc5xxxMediumUnit
            result = device.get_calibration_fullscale(i)
            assert type(result) is float
            result = device.get_calibration_initial_conditions(i)
            assert type(result) == Sfc5xxxCalibrationConditions
            result = device.get_calibration_recalibration_conditions(i)
            assert type(result) == Sfc5xxxCalibrationConditions
            result = device.get_calibration_thermal_conductivity_reference(i)
            assert type(result) is int
        else:
            with pytest.raises(Sfc5xxxInvalidCalibrationIndexError):
                device.get_calibration_gas_description(i)
            with pytest.raises(Sfc5xxxInvalidCalibrationIndexError):
                device.get_calibration_gas_id(i)
            with pytest.raises(Sfc5xxxInvalidCalibrationIndexError):
                device.get_calibration_gas_unit(i)
            with pytest.raises(Sfc5xxxInvalidCalibrationIndexError):
                device.get_calibration_fullscale(i)
            with pytest.raises(Sfc5xxxInvalidCalibrationIndexError):
                device.get_calibration_initial_conditions(i)
            with pytest.raises(Sfc5xxxInvalidCalibrationIndexError):
                device.get_calibration_recalibration_conditions(i)
            with pytest.raises(Sfc5xxxInvalidCalibrationIndexError):
                device.get_calibration_thermal_conductivity_reference(i)
