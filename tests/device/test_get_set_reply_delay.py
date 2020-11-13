# -*- coding: utf-8 -*-
# (c) Copyright 2020 Sensirion AG, Switzerland

from __future__ import absolute_import, division, print_function
import pytest


@pytest.mark.needs_device
def test(device):
    """
    Test if get_reply_delay() returns the value previously set with
    set_reply_delay().
    """
    old_value = device.get_reply_delay()
    assert type(old_value) is int

    result = device.set_reply_delay(old_value + 100)
    assert result is None

    result = device.get_reply_delay()
    assert type(result) is int
    assert result == old_value + 100

    # restore old value
    device.set_reply_delay(old_value)
