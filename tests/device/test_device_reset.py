# -*- coding: utf-8 -*-
# (c) Copyright 2020 Sensirion AG, Switzerland

from __future__ import absolute_import, division, print_function
import pytest


@pytest.mark.needs_device
def test(device):
    """
    Test if device_reset() works as expected by chaning a volatile setting,
    perform the reset, and then verifying that the setting was reset to its
    default value.
    """
    device.set_user_defined_valve_value(0.1337)
    device.device_reset()
    assert device.get_user_defined_valve_value() == 0.0
