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
    Test if read_measured_value() works as expected.
    """
    result = device.read_measured_value(scaling)
    assert type(result) is float
