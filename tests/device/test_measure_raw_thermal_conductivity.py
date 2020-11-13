# -*- coding: utf-8 -*-
# (c) Copyright 2020 Sensirion AG, Switzerland

from __future__ import absolute_import, division, print_function
import pytest


@pytest.mark.needs_device
def test_without_argument(device):
    """
    Test if measure_raw_thermal_conductivity() works as expected when passing
    no argument.
    """
    result = device.measure_raw_thermal_conductivity()
    assert type(result) is int
    assert 0 <= result <= 65535


@pytest.mark.needs_device
def test_with_argument(device):
    """
    Test if measure_raw_thermal_conductivity() works as expected when passing
    an argument.
    """
    result = device.measure_raw_thermal_conductivity(False)
    assert type(result) is int
    assert 0 <= result <= 65535
