# -*- coding: utf-8 -*-
# (c) Copyright 2020 Sensirion AG, Switzerland

from __future__ import absolute_import, division, print_function
from sensirion_shdlc_sfc5xxx import Sfc5xxxValveInputSource
import pytest


@pytest.mark.needs_device
@pytest.mark.parametrize("source", [
    (Sfc5xxxValveInputSource.CONTROLLER),
    (Sfc5xxxValveInputSource.FORCE_CLOSED),
    (Sfc5xxxValveInputSource.FORCE_OPEN),
    (Sfc5xxxValveInputSource.HOLD),
    (Sfc5xxxValveInputSource.USER_DEFINED),
])
def test(device, source):
    """
    Test if get_valve_input_source() returns the value previously set with
    set_valve_input_source().
    """
    result = device.set_valve_input_source(source)
    assert result is None
    result = device.get_valve_input_source()
    assert type(result) is Sfc5xxxValveInputSource
    assert result == source

    # restore default valve input source
    result = device.set_valve_input_source(Sfc5xxxValveInputSource.CONTROLLER)
    assert result is None
    result = device.get_valve_input_source()
    assert type(result) is Sfc5xxxValveInputSource
    assert result == Sfc5xxxValveInputSource.CONTROLLER
