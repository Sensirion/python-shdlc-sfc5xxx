# -*- coding: utf-8 -*-
# (c) Copyright 2020 Sensirion AG, Switzerland

from __future__ import absolute_import, division, print_function
import pytest


@pytest.mark.needs_device
def test(device):
    """
    Test if get_user_defined_valve_value() returns the value previously set
    with set_user_defined_valve_value().
    """
    result = device.set_user_defined_valve_value(0.1234)
    assert result is None
    result = device.get_user_defined_valve_value()
    assert type(result) is float
    assert result == pytest.approx(0.1234, abs=0.0001)

    result = device.set_user_defined_valve_value(0)
    assert result is None
    result = device.get_user_defined_valve_value()
    assert type(result) is float
    assert result == 0.0
