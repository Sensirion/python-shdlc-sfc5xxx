# -*- coding: utf-8 -*-
# (c) Copyright 2020 Sensirion AG, Switzerland

from __future__ import absolute_import, division, print_function
from sensirion_shdlc_sfc5xxx import Sfc5xxxScaling
import pytest


@pytest.mark.needs_device
@pytest.mark.parametrize("scaling", [
    (Sfc5xxxScaling.NORMALIZED),
    (Sfc5xxxScaling.PHYSICAL),
    (Sfc5xxxScaling.USER_DEFINED),
])
def test(device, scaling):
    """
    Test if set_setpoint_and_read_measured_value() works as expected.
    """
    result = device.set_setpoint_and_read_measured_value(0.123, scaling)
    assert type(result) is float
    result = device.get_setpoint(scaling)
    assert result == pytest.approx(0.123, abs=0.001)

    result = device.set_setpoint_and_read_measured_value(0, scaling)
    assert type(result) is float
    result = device.get_setpoint(scaling)
    assert type(result) is float
    assert result == 0
