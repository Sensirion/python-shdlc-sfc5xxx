# -*- coding: utf-8 -*-
# (c) Copyright 2020 Sensirion AG, Switzerland

from __future__ import absolute_import, division, print_function
from sensirion_shdlc_sfc5xxx import Sfc5xxxUnitPrefix, Sfc5xxxUnit, \
    Sfc5xxxUnitTimeBase, Sfc5xxxMediumUnit
import pytest


@pytest.mark.needs_device
@pytest.mark.parametrize("unit,fullscale", [
    (Sfc5xxxMediumUnit(Sfc5xxxUnitPrefix.ONE, Sfc5xxxUnit.PERCENT,
                       Sfc5xxxUnitTimeBase.NONE), 100.0),
    (Sfc5xxxMediumUnit(Sfc5xxxUnitPrefix.ONE, Sfc5xxxUnit.PERMIL,
                       Sfc5xxxUnitTimeBase.NONE), 1000.0),
    (Sfc5xxxMediumUnit(Sfc5xxxUnitPrefix.ONE, Sfc5xxxUnit.INT16,
                       Sfc5xxxUnitTimeBase.NONE), 32767.0),
])
def test(device, unit, fullscale):
    """
    Test if get_user_defined_fullscale() returns the expected value.
    """
    device.set_user_defined_medium_unit(unit)
    result = device.get_user_defined_fullscale()
    assert type(result) is float
    assert result == pytest.approx(fullscale, abs=0.01)
