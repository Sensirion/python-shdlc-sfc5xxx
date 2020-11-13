# -*- coding: utf-8 -*-
# (c) Copyright 2020 Sensirion AG, Switzerland

from __future__ import absolute_import, division, print_function
import pytest


@pytest.mark.needs_device
def test(device):
    """
    Test if measure_raw_flow() works as expected.
    """
    result = device.measure_raw_flow()
    assert type(result) is int
    assert 0 <= result <= 65535
