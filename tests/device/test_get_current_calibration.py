# -*- coding: utf-8 -*-
# (c) Copyright 2020 Sensirion AG, Switzerland

from __future__ import absolute_import, division, print_function

import pytest

from sensirion_shdlc_sfc5xxx import Sfc5xxxMediumUnit
from sensirion_shdlc_sfc5xxx.types import Sfc5xxxCalibrationConditions


@pytest.mark.needs_device
def test(device):
    """
    Test if the get_current_*() methods work as expected.
    """
    result = device.get_current_gas_description()
    assert isinstance(result, str)
    result = device.get_current_gas_id()
    assert isinstance(result, int)
    result = device.get_current_gas_unit()
    assert isinstance(result, Sfc5xxxMediumUnit)
    result = device.get_current_fullscale()
    assert isinstance(result, float)
    result = device.get_current_initial_calibration_conditions()
    assert isinstance(result, Sfc5xxxCalibrationConditions)
    result = device.get_current_recalibration_conditions()
    assert isinstance(result, Sfc5xxxCalibrationConditions)
    result = device.get_current_thermal_conductivity_reference()
    assert isinstance(result, int)
