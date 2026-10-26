Sensirion SFC5xxx/SFM5xxx Python Driver
=======================================

This package contains the SHDLC driver for the `Sensirion SFC5xxx`_ mass flow
controllers and `Sensirion SFM5xxx`_ mass flow meters which have an RS485
interface using the SHDLC protocol. MFCs and MFMs which do not have an SHDLC
interface are not supported by this driver.

The driver provides all SHDLC commands (e.g. set setpoint and read measured
flow) as Python methods and handles all the low-level things like type
conversions, checksum calculation, error handling etc.


.. toctree::
   :maxdepth: 2
   :caption: Contents:

   shdlc
   installation
   quickstart
   development
   api
.. _Sensirion SFC5xxx: https://sensirion.com/products/catalog/mass-flow-controllers?interfaces=rs485&page=1&page_size=12&series=SFC5300%2CSFC5400%2CSFC5500
.. _Sensirion SFM5xxx: https://sensirion.com/products/catalog/gas-flow-sensors?interfaces=rs485&page=1&page_size=12&series=SFM5xxx&statuses=active
