# -*- coding: utf-8 -*-
# (c) Copyright 2020 Sensirion AG, Switzerland

from __future__ import absolute_import, division, print_function
from enum import Enum

import logging
log = logging.getLogger(__name__)


class Sfc5xxxUnitPrefix(Enum):
    """
    An enum containing all available medium unit prefixes with their
    corresponding byte values how they are transmitted over SHDLC.
    """

    YOCTO = (-24, "Yocto (10^-24)", "y")  #: Yocto (10^-24).
    ZEPTO = (-21, "Zepto (10^-21)", "z")  #: Zepto (10^-21).
    ATTO = (-18, "Atto (10^-18)", "a")  #: Atto (10^-18).
    FEMTO = (-15, "Femto (10^-15)", "f")  #: Femto (10^-15).
    PICO = (-12, "Pico (10^-12)", "p")  #: Pico (10^-12).
    NANO = (-9, "Nano (10^-9)", "n")  #: Nano (10^-9).
    MICRO = (-6, "Micro (10^-6)", "µ")  #: Micro (10^-6).
    MILLI = (-3, "Milli (10^-3)", "m")  #: Milli (10^-3).
    CENTI = (-2, "Centi (10^-2)", "c")  #: Centi (10^-2).
    DECI = (-1, "Deci (10^-1)", "d")  #: Deci (10^-1).
    ONE = (0, "1", "")  #: No prefix (10^0).
    DECA = (1, "Deca (10^1)", "da")  #: Deca (10^1).
    HECTO = (2, "Hecto (10^2)", "h")  #: Hecto (10^2).
    KILO = (3, "Kilo (10^3)", "k")  #: Kilo (10^3).
    MEGA = (6, "Mega (10^6)", "M")  #: Mega (10^6).
    GIGA = (9, "Giga (10^9)", "G")  #: Giga (10^9).
    TERA = (12, "Tera (10^12)", "T")  #: Tera (10^12).
    PETA = (15, "Peta (10^15)", "P")  #: Peta (10^15).
    EXA = (18, "Exa (10^18)", "E")  #: Exa (10^18).
    ZETTA = (21, "Zetta (10^21)", "Z")  #: Zetta (10^21).
    YOTTA = (24, "Yotta (10^24)", "Y")  #: Yotta (10^24).
    UNDEFINED = (127, "Undefined", "")  #: Undefined.

    def __init__(self, value, description, symbol):
        """
        Constructor

        :param int value:
            The integer value.
        :param str description:
            The prefix description.
        :param str symbol:
            The prefix symbol.
        """
        self._value_ = value
        self.description = description  #: The prefix description (str).
        self.symbol = symbol  #: The prefix symbol (str).

    @staticmethod
    def from_int(value):
        """
        Create the enum value from a given integer value.

        :param int value:
            The integer representation of the unit prefix.
        :raises ValueError:
            If the enum does not contain an entry for the given value.
        :return:
            An enum object.
        :rtype:
            ~sensirion_shdlc_sfc5xxx.units.Sfc5xxxUnitPrefix
        """
        for item in Sfc5xxxUnitPrefix:
            if item.value == value:
                return item
        raise ValueError("Invalid unit prefix value: {}!".format(value))


class Sfc5xxxUnit(Enum):
    """
    An enum containing all available medium units with their
    corresponding byte values how they are transmitted over SHDLC.
    """

    #: Norm Liter (0°C, 1013hPa)
    NORM_LITER = (0, "Norm Liter (0°C, 1013hPa)", "ln")
    #: Standard Liter (20°C, 1013hPa)
    STANDARD_LITER = (1, "Standard Liter (20°C, 1013hPa)", "ls")
    #: Standard Liter (15°C, 1013hPa)
    STANDARD_LITER_15C = (2, "Standard Liter (15°C, 1013hPa)", "ls")
    #: Standard Liter (25°C, 1013hPa)
    STANDARD_LITER_25C = (3, "Standard Liter (25°C, 1013hPa)", "ls")
    #: Standard Liter (70°F, 1013hPa)
    STANDARD_LITER_70F = (4, "Standard Liter (70°F, 1013hPa)", "ls")
    #: Liter (liqui).
    LITER_LIQUI = (8, "Liter (liqui)", "l")
    #: Gram (g).
    GRAM = (9, "Gram", "g")
    #: Pascal (Pa).
    PASCAL = (16, "Pascal", "Pa")
    #: Bar.
    BAR = (17, "Bar", "bar")
    #: Meter H2O (mH2O).
    METER_H2O = (18, "Meter H2O", "mH2O")
    #: Inch H2O (iH2O).
    INCH_H2O = (19, "Inch H2O", "iH2O")
    #: Percent (%).
    PERCENT = (250, "Percent", "%")
    #: Permil (‰).
    PERMIL = (251, "Permil", "‰")
    #: 8-Bit Signed Integer.
    INT8 = (252, "8-Bit Signed Integer", "ticks")
    #: 16-Bit Signed Integer.
    INT16 = (253, "16-Bit Signed Integer", "ticks")
    #: 32-Bit Signed Integer.
    INT32 = (254, "32-Bit Signed Integer", "ticks")
    #: Undefined.
    UNDEFINED = (255, "Undefined", "")

    def __init__(self, value, description, symbol):
        """
        Constructor

        :param int value:
            The integer value.
        :param str description:
            The unit description.
        :param str symbol:
            The unit symbol.
        """
        self._value_ = value
        self.description = description
        self.symbol = symbol

    @staticmethod
    def from_int(value):
        """
        Create the enum value from a given integer value.

        :param int value:
            The integer representation of the unit.
        :raises ValueError:
            If the enum does not contain an entry for the given value.
        :return:
            An enum object.
        :rtype:
            ~sensirion_shdlc_sfc5xxx.units.Sfc5xxxUnit
        """
        for item in Sfc5xxxUnit:
            if item.value == value:
                return item
        raise ValueError("Invalid unit value: {}!".format(value))


class Sfc5xxxUnitTimeBase(Enum):
    """
    An enum containing all available medium unit time bases with their
    corresponding byte values how they are transmitted over SHDLC.
    """

    NONE = (0, "No Time Base", "")  #: No Time Base.
    MICROSECOND = (1, "Microsecond", "µs")  #: Microsecond (µs).
    MILLISECOND = (2, "Millisecond", "ms")  #: Millisecond (ms).
    SECOND = (3, "Second", "s")  #: Second (s).
    MINUTE = (4, "Minute", "min")  #: Minute (min).
    HOUR = (5, "Hour", "h")  #: Hour (h).
    DAY = (6, "Day", "day")  #: Day.
    UNDEFINED = (255, "Undefined", "")  #: Undefined.

    def __init__(self, value, description, symbol):
        """
        Constructor

        :param int value:
            The integer value.
        :param str description:
            The timebase description.
        :param str symbol:
            The timebase symbol.
        """
        self._value_ = value
        self.description = description
        self.symbol = symbol

    @staticmethod
    def from_int(value):
        """
        Create the enum value from a given integer value.

        :param int value:
            The integer representation of the timebase.
        :raises ValueError:
            If the enum does not contain an entry for the given value.
        :return:
            An enum object.
        :rtype:
            ~sensirion_shdlc_sfc5xxx.units.Sfc5xxxUnitTimeBase
        """
        for item in Sfc5xxxUnitTimeBase:
            if item.value == value:
                return item
        raise ValueError("Invalid unit time base: {}!".format(value))


class Sfc5xxxMediumUnit(object):
    """
    A class representing the medium unit specification used by various SHDLC
    commands. It consists of three members:

      * Prefix (:py:class:`~sensirion_shdlc_sfc5xxx.units.Sfc5xxxUnitPrefix`)
      * Physical Unit (:py:class:`~sensirion_shdlc_sfc5xxx.units.Sfc5xxxUnit`)
      * Unit Timebase
        (:py:class:`~sensirion_shdlc_sfc5xxx.units.Sfc5xxxUnitTimeBase`)
    """

    def __init__(self, prefix, unit, timebase):
        """
        Constructor.

        :param ~sensirion_shdlc_sfc5xxx.units.Sfc5xxxUnitPrefix prefix:
            The unit prefix.
        :param ~sensirion_shdlc_sfc5xxx.units.Sfc5xxxUnit unit:
            The physical unit.
        :param ~sensirion_shdlc_sfc5xxx.units.Sfc5xxxUnitTimeBase timebase:
            The unit time base.
        """
        super(Sfc5xxxMediumUnit, self).__init__()
        #: Unit prefix
        #: (:py:class:`~sensirion_shdlc_sfc5xxx.units.Sfc5xxxUnitPrefix`).
        self.prefix = prefix
        #: Physical unit
        #: (:py:class:`~sensirion_shdlc_sfc5xxx.units.Sfc5xxxUnit`).
        self.unit = unit
        #: Unit timebase
        #: (:py:class:`~sensirion_shdlc_sfc5xxx.units.Sfc5xxxUnitTimeBase`).
        self.timebase = timebase

    def __str__(self):
        """
        Pretty-print the unit represented by this object (e.g. "mln/min").

        .. note:: Basically this method just appends the ``symbol`` property
                  of the unit prefix, physical unit and the timebase. But
                  there is some additional logic to get more readable strings
                  in some cases. For example "mls/min" is converted to "sccm"
                  to be consistent with the unit printed on the label of the
                  MFC. And for standard liter units of special temperatures,
                  the temperature is appended to the returned string to
                  distinguish between them.

        :return:
            Short string representation of prefix, unit and timebase.
        :rtype:
            str
        """
        s = self.prefix.symbol
        s += self.unit.symbol
        if len(self.timebase.symbol) > 0:
            s += '/' + self.timebase.symbol
        if s == 'mls/min':
            s = 'sccm'
        elif s == 'ls/min':
            s = 'slm'
        if self.unit == Sfc5xxxUnit.STANDARD_LITER_15C:
            s += ' (15°C)'
        elif self.unit == Sfc5xxxUnit.STANDARD_LITER_25C:
            s += ' (25°C)'
        elif self.unit == Sfc5xxxUnit.STANDARD_LITER_70F:
            s += ' (70°F)'
        return s

    def __eq__(self, other):
        """
        Equal-operator overload.

        :param other:
            The other object to compare with.
        :return:
            ``True`` if both objects return the same unit, ``False`` otherwise.
        """
        return (self.prefix == other.prefix) and \
               (self.unit == other.unit) and \
               (self.timebase == other.timebase)
