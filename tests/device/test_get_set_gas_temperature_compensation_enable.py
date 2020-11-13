# -*- coding: utf-8 -*-
# (c) Copyright 2020 Sensirion AG, Switzerland

from __future__ import absolute_import, division, print_function
import pytest


@pytest.mark.needs_device
def test(device):
    """
    Test if get_gas_temperature_compensation_enable() returns the value
    previously set with set_gas_temperature_compensation_enable().
    """
    result = device.set_gas_temperature_compensation_enable(True)
    assert result is None
    result = device.get_gas_temperature_compensation_enable()
    assert type(result) is bool
    assert result is True

    result = device.set_gas_temperature_compensation_enable(False)
    assert result is None
    result = device.get_gas_temperature_compensation_enable()
    assert type(result) is bool
    assert result is False
