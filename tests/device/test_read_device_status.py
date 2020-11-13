# -*- coding: utf-8 -*-
# (c) Copyright 2020 Sensirion AG, Switzerland

from __future__ import absolute_import, division, print_function
from sensirion_shdlc_driver.errors import ShdlcDeviceError
import pytest


@pytest.mark.needs_device
def test_without_arguments(device):
    """
    Test if read_device_status() returns the expected value when passing no
    arguments.
    """
    status, error = device.read_device_status()
    assert type(status) is int
    assert type(error) is int


@pytest.mark.needs_device
def test_with_arguments(device):
    """
    Test if read_device_status() returns the expected value when passing both
    arguments.
    """
    status, error = device.read_device_status(False, True)
    assert type(status) is int
    assert (error is None) or isinstance(error, ShdlcDeviceError)
