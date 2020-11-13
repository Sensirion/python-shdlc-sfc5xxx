# -*- coding: utf-8 -*-
# (c) Copyright 2020 Sensirion AG, Switzerland

from __future__ import absolute_import, division, print_function
import pytest


@pytest.mark.needs_device
def test(device):
    """
    Test if get_pressure_dependent_gain_enable() returns the value previously
    set with set_pressure_dependent_gain_enable().
    """
    result = device.set_pressure_dependent_gain_enable(True)
    assert result is None
    result = device.get_pressure_dependent_gain_enable()
    assert type(result) is bool
    assert result is True

    result = device.set_pressure_dependent_gain_enable(False)
    assert result is None
    result = device.get_pressure_dependent_gain_enable()
    assert type(result) is bool
    assert result is False
