# -*- coding: utf-8 -*-
# (c) Copyright 2020 Sensirion AG, Switzerland

from __future__ import absolute_import, division, print_function
import pytest


@pytest.mark.needs_device
def test(device):
    """
    Test if get_inlet_gas_temperature_for_compensation() returns the value
    previously set with set_inlet_gas_temperature_for_compensation().
    """
    result = device.set_inlet_gas_temperature_for_compensation(0.1234)
    assert result is None
    result = device.get_inlet_gas_temperature_for_compensation()
    assert type(result) is float
    assert result == pytest.approx(0.1234, abs=0.0001)

    result = device.set_inlet_gas_temperature_for_compensation(0)
    assert result is None
    result = device.get_inlet_gas_temperature_for_compensation()
    assert type(result) is float
    assert result == 0.0
