# Copyright 2019 PandoraGo Co.,LTD.
# All Rights Reserved.
#
# Tony 2019/2/9: Add ocr controller.

"""
Version 1 of the Cosmos API

Specification can be found at doc/source/webapi/v1.rst
"""

import pecan
from pecan import rest
from wsme import types as wtypes

from cosmos.api.controllers import base
from cosmos.api.controllers import link
from cosmos.api.controllers.v1.ocr import general
from cosmos.api import expose


class OCR(base.APIBase):
    """The representation of OCR of the API."""

    id = wtypes.text
    """The ID of the version, also acts as the release number"""

    url = [link.Link]
    """Links to the demo resource"""

    @staticmethod
    def convert():
        ocr = OCR()
        ocr.id = "ocr"
        base_url = "http://0.0.0.0:8888/v1/ocr"
        ocr.url = [link.Link.make_link('self', base_url, 'ocr', '')]
        return ocr


class OCRController(rest.RestController):
    """OCR controller."""

    # Ocr general controller.
    general = general.OCRGeneralController()

    @expose.expose(OCR)
    def get(self):
        return OCR.convert()


__all__ = ('OCRController',)
