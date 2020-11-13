# -*- coding: utf-8 -*-
# (c) Copyright 2020 Sensirion AG, Switzerland

from __future__ import absolute_import, division, print_function
from sensirion_shdlc_driver import ShdlcFirmwareImage

import logging
log = logging.getLogger(__name__)


class Sfc5xxxFirmwareImage(ShdlcFirmwareImage):
    """
    SFC5xxx firmware image.

    This class represents a firmware image for the SFC5xxx device. It is used
    to load and verify Intel-Hex files for performing firmware updates over
    SHDLC.
    """

    def __init__(self, hexfile):
        """
        Constructor which loads and parses the firmware from a hex file.

        :param str/file hexfile:
            The filename or file-like object containing the firmware in
            Intel-Hex format (\\*.hex).
        :raise ~sensirion_shdlc_driver.errors.ShdlcFirmwareImageSignatureError:
            If the signature of the image is invalid.
        """
        super(Sfc5xxxFirmwareImage, self).__init__(
            hexfile, bl_start_addr=0x8000000, app_start_addr=0x8004000)
