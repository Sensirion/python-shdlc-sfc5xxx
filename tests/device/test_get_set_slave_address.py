# -*- coding: utf-8 -*-
# (c) Copyright 2020 Sensirion AG, Switzerland

from __future__ import absolute_import, division, print_function
import pytest


@pytest.mark.needs_device
def test(device, slave_address):
    """
    Test if get_slave_address() returns the value previously set with
    set_slave_address().
    """
    result = device.set_slave_address(slave_address + 10)
    assert result is None

    result = device.get_slave_address()
    assert type(result) is int
    assert result == slave_address + 10

    # restore original address
    device.set_slave_address(slave_address)
    assert device.get_slave_address() == slave_address
