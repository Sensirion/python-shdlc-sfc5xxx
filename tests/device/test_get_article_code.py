# -*- coding: utf-8 -*-
# (c) Copyright 2020 Sensirion AG, Switzerland

from __future__ import absolute_import, division, print_function
import pytest


@pytest.mark.needs_device
def test(device):
    """
    Test if get_article_code() returns the expected value.
    """
    article_code = device.get_article_code()
    assert type(article_code) is str
