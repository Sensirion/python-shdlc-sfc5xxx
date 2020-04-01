sensirion-shdlc-sfc5xxx
=======================

This package contains the SHDLC driver for the `Sensirion SFC5xxx`_ mass flow
controllers and `Sensirion SFM5xxx`_ mass flow meters which have an RS485
interface using the SHDLC protocol. MFCs and MFMs which do not have an SHDLC
interface are not supported by this driver.

The driver provides all SHDLC commands (e.g. set setpoint and read measured
flow) as Python methods and handles all the low-level things like type
conversions, checksum calculation, error handling etc.


.. _Sensirion SFC5xxx: https://www.sensirion.com/en/flow-sensors/flow-controllers-for-gases/
.. _Sensirion SFM5xxx: https://www.sensirion.com/en/flow-sensors/mass-flow-meters-for-gases/
