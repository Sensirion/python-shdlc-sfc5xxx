# -*- coding: utf-8 -*-
# (c) Copyright 2020 Sensirion AG, Switzerland

from __future__ import absolute_import, division, print_function
import pytest


@pytest.mark.needs_device
def test(device):
    """
    Test if get_product_subtype() returns the expected value.
    """
    product_subtype = device.get_product_subtype()
    assert type(product_subtype) is int
    assert 0 <= product_subtype <= 30
