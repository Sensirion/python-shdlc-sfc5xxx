# -*- coding: utf-8 -*-
# (c) Copyright 2020 Sensirion AG, Switzerland

from __future__ import absolute_import, division, print_function
import pytest


@pytest.mark.needs_device
def test(device):
    """
    Test if measure_temperature() works as expected.
    """
    result = device.measure_temperature()
    assert type(result) is float
    assert 0.0 <= result <= 50.0
