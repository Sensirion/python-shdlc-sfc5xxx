# -*- coding: utf-8 -*-
# (c) Copyright 2020 Sensirion AG, Switzerland

from __future__ import absolute_import, division, print_function
from sensirion_shdlc_sfc5xxx.device_errors import \
    Sfc5xxxInvalidCalibrationIndexError
import pytest


@pytest.mark.needs_device
def test_valid_index(device):
    """
    Test if activate_calibration() works as expected when passing a valid
    calibration index.
    """
    result = device.activate_calibration(0)  # we assume 0 is valid
    assert result is None


@pytest.mark.needs_device
def test_invalid_index(device):
    """
    Test if activate_calibration() raises the expected exception when
    passing an invalid calibration index.
    """
    with pytest.raises(Sfc5xxxInvalidCalibrationIndexError):
        device.activate_calibration(25)  # we assume 25 is invalid
