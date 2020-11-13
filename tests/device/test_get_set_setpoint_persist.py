# -*- coding: utf-8 -*-
# (c) Copyright 2020 Sensirion AG, Switzerland

from __future__ import absolute_import, division, print_function
import pytest


@pytest.mark.needs_device
def test(device):
    """
    Test if get_setpoint_persist() returns the value previously set with
    set_setpoint_persist().
    """
    result = device.set_setpoint_persist(True)
    assert result is None
    result = device.get_setpoint_persist()
    assert type(result) is bool
    assert result is True

    result = device.set_setpoint_persist(False)
    assert result is None
    result = device.get_setpoint_persist()
    assert type(result) is bool
    assert result is False
