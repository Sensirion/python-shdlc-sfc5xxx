# -*- coding: utf-8 -*-
# (c) Copyright 2020 Sensirion AG, Switzerland

from __future__ import absolute_import, division, print_function
import pytest


@pytest.mark.needs_device
def test(device, serial_bitrate):
    """
    Test if get_baudrate() returns the value previously set with
    set_baudrate().
    """
    result = device.set_baudrate(19200)
    assert result is None

    result = device.get_baudrate()
    assert type(result) is int
    assert result == 19200

    # restore original address
    device.set_baudrate(serial_bitrate)
    assert device.get_baudrate() == serial_bitrate
