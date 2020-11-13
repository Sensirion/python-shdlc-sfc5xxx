# -*- coding: utf-8 -*-
# (c) Copyright 2020 Sensirion AG, Switzerland

from __future__ import absolute_import, division, print_function
from sensirion_shdlc_sfc5xxx import Sfc5xxxMediumUnit
from sensirion_shdlc_sfc5xxx.types import Sfc5xxxCalibrationConditions
import pytest


@pytest.mark.needs_device
def test(device):
    """
    Test if the get_current_*() methods work as expected.
    """
    result = device.get_current_gas_description()
    assert type(result) is str
    result = device.get_current_gas_id()
    assert type(result) is int
    result = device.get_current_gas_unit()
    assert type(result) is Sfc5xxxMediumUnit
    result = device.get_current_fullscale()
    assert type(result) is float
    result = device.get_current_initial_calibration_conditions()
    assert type(result) == Sfc5xxxCalibrationConditions
    result = device.get_current_recalibration_conditions()
    assert type(result) == Sfc5xxxCalibrationConditions
    result = device.get_current_thermal_conductivity_reference()
    assert type(result) is int
