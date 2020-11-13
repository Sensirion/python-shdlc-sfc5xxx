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
    Test if get_setpoint() returns the value previously set with
    set_setpoint().
    """
    result = device.set_setpoint(0.123, scaling)
    assert result is None
    result = device.get_setpoint(scaling)
    assert type(result) is float
    assert result == pytest.approx(0.123, abs=0.001)

    result = device.set_setpoint(0, scaling)
    assert result is None
    result = device.get_setpoint(scaling)
    assert type(result) is float
    assert result == 0
