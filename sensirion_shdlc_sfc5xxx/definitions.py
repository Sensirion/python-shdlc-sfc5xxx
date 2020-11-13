# -*- coding: utf-8 -*-
# (c) Copyright 2020 Sensirion AG, Switzerland

from __future__ import absolute_import, division, print_function
from enum import IntEnum

import logging
log = logging.getLogger(__name__)


class Sfc5xxxScaling(IntEnum):
    """
    An enum containing all available scaling variants with their corresponding
    byte values how they are transmitted over SHDLC.
    """

    NORMALIZED = 0x00  #: Normalized to range [0...1].
    PHYSICAL = 0x01  #: Physical value with unit and fullscale of calibration.
    USER_DEFINED = 0x02  #: User defined unit and scaling as configured.


class Sfc5xxxValveInputSource(IntEnum):
    """
    An enum containing all available valve input sources with their
    corresponding byte values how they are transmitted over SHDLC.
    """

    CONTROLLER = 0x00  #: Driven by the flow controller (default).
    FORCE_CLOSED = 0x01  #: Force closed (valve remains fully closed).
    FORCE_OPEN = 0x02  #: Force open (valve remains fully open).
    HOLD = 0x03  #: Hold the voltage on the valve.
    USER_DEFINED = 0x10  #: Apply user defined value (needs to be configured!).
