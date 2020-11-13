# -*- coding: utf-8 -*-
# (c) Copyright 2020 Sensirion AG, Switzerland

from __future__ import absolute_import, division, print_function
import pytest


@pytest.mark.needs_device
def test(device):
    """
    Test if get_inlet_pressure_for_gain_correction() returns the value
    previously set with set_inlet_pressure_for_gain_correction().
    """
    result = device.set_inlet_pressure_for_gain_correction(2.345)
    assert result is None
    result = device.get_inlet_pressure_for_gain_correction()
    assert type(result) is float
    assert result == pytest.approx(2.345, abs=0.0001)

    result = device.set_inlet_pressure_for_gain_correction(1)
    assert result is None
    result = device.get_inlet_pressure_for_gain_correction()
    assert type(result) is float
    assert result == 1.0
