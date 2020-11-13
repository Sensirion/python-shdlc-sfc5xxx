# -*- coding: utf-8 -*-
# (c) Copyright 2020 Sensirion AG, Switzerland

from __future__ import absolute_import, division, print_function
from sensirion_shdlc_sfc5xxx import Sfc5xxxScaling
from sensirion_shdlc_sfc5xxx.types import Sfc5xxxReadBufferResponse
import pytest


@pytest.mark.needs_device
@pytest.mark.parametrize("scaling", [
    (Sfc5xxxScaling.NORMALIZED),
    (Sfc5xxxScaling.PHYSICAL),
    (Sfc5xxxScaling.USER_DEFINED),
])
def test_default_max_reads(device, scaling):
    """
    Test read_measured_value_buffer() without passing the "max_reads"
    parameter.
    """
    result = device.read_measured_value_buffer(scaling)
    assert type(result) is Sfc5xxxReadBufferResponse
    assert result.scaling == scaling
    assert result.read_count >= 1
    assert result.lost_values >= 0
    assert result.remaining_values >= 0
    assert result.sampling_time >= 0.0
    assert len(result.values) >= 0


@pytest.mark.needs_device
@pytest.mark.parametrize("scaling", [
    (Sfc5xxxScaling.NORMALIZED),
    (Sfc5xxxScaling.PHYSICAL),
    (Sfc5xxxScaling.USER_DEFINED),
])
def test_explicit_max_reads(device, scaling):
    """
    Test read_measured_value_buffer() with passing the "max_reads"
    parameter.
    """
    result = device.read_measured_value_buffer(scaling, 1)
    assert type(result) is Sfc5xxxReadBufferResponse
    assert result.scaling == scaling
    assert result.read_count == 1
    assert result.lost_values >= 0
    assert result.remaining_values >= 0
    assert result.sampling_time >= 0.0
    assert len(result.values) >= 0
