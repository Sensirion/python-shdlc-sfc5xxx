# -*- coding: utf-8 -*-
# (c) Copyright 2020 Sensirion AG, Switzerland

from __future__ import absolute_import, division, print_function
import pytest


@pytest.mark.needs_device
def test_bytes(device):
    """
    Test if read_user_memory() returns the data previously written with
    write_user_memory(), passed as bytes object.
    """
    result = device.write_user_memory(0, b"\x00\x11\x22\x33")
    assert result is None
    result = device.read_user_memory(0, 4)
    assert type(result) is bytes
    assert result == b"\x00\x11\x22\x33"


@pytest.mark.needs_device
def test_bytearray(device):
    """
    Test if read_user_memory() returns the data previously written with
    write_user_memory(), passed as bytearray object.
    """
    result = device.write_user_memory(10, bytearray([0x12, 0x34, 0x56]))
    assert result is None
    result = device.read_user_memory(10, 3)
    assert type(result) is bytes
    assert result == b"\x12\x34\x56"


@pytest.mark.needs_device
def test_list(device):
    """
    Test if read_user_memory() returns the data previously written with
    write_user_memory(), passed as list object.
    """
    result = device.write_user_memory(20, [0x55, 0x66])
    assert result is None
    result = device.read_user_memory(20, 2)
    assert type(result) is bytes
    assert result == b"\x55\x66"
