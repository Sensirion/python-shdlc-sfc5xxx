# -*- coding: utf-8 -*-
# (c) Copyright 2020 Sensirion AG, Switzerland

from __future__ import absolute_import, division, print_function
from sensirion_shdlc_sfc5xxx import Sfc5xxxUnitPrefix, Sfc5xxxUnit, \
    Sfc5xxxUnitTimeBase, Sfc5xxxMediumUnit
import pytest


@pytest.mark.needs_device
@pytest.mark.parametrize("unit", [
    (Sfc5xxxMediumUnit(Sfc5xxxUnitPrefix.ZEPTO, Sfc5xxxUnit.STANDARD_LITER_25C,
                       Sfc5xxxUnitTimeBase.DAY)),
    (Sfc5xxxMediumUnit(Sfc5xxxUnitPrefix.ONE, Sfc5xxxUnit.NORM_LITER,
                       Sfc5xxxUnitTimeBase.SECOND)),
    (Sfc5xxxMediumUnit(Sfc5xxxUnitPrefix.UNDEFINED, Sfc5xxxUnit.UNDEFINED,
                       Sfc5xxxUnitTimeBase.UNDEFINED)),
])
def test_get_set(device, unit):
    """
    Test if get_user_defined_medium_unit() returns the value previously set
    with set_user_defined_medium_unit().
    """
    result = device.set_user_defined_medium_unit(unit)
    assert result is None
    result = device.get_user_defined_medium_unit()
    assert type(result) is Sfc5xxxMediumUnit
    assert result == unit


@pytest.mark.needs_device
def test_substitute_wildcards(device):
    """
    Test if get_user_defined_medium_unit() returns the calibration unit if
    substitute_wildcards=True is passed and the user defined medium unit is
    undefined.
    """
    calib_unit = device.get_current_gas_unit()
    device.set_user_defined_medium_unit(Sfc5xxxMediumUnit(
        Sfc5xxxUnitPrefix.UNDEFINED, Sfc5xxxUnit.UNDEFINED,
        Sfc5xxxUnitTimeBase.UNDEFINED))
    result = device.get_user_defined_medium_unit(True)
    assert result == calib_unit
