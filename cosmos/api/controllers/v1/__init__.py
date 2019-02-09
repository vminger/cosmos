# Copyright 2019 PandoraGo Co.,LTD.
# All Rights Reserved.
#
# Tony 2019/2/3: Add controller init.

"""
Version 1 of the Cosmos API

Specification can be found at doc/source/webapi/v1.rst
"""

import pecan
from pecan import rest
from wsme import types as wtypes

from cosmos.api.controllers import base
from cosmos.api.controllers import link
from cosmos.api.controllers.v1 import demo
from cosmos.api.controllers.v1 import half_plus_two
from cosmos.api.controllers.v1 import ocr
from cosmos.api import expose


class V1(base.APIBase):
    """The representation of the version 1 of the API."""

    id = wtypes.text
    """The ID of the version, also acts as the release number"""

    demo = [link.Link]
    """Links to the demo resource"""

    @staticmethod
    def convert():
        v1 = V1()
        v1.id = "v1"
        pecan.request.public_url = "http://0.0.0.0:8888/v1"
        v1.demo = [link.Link.make_link('self', pecan.request.public_url,
                                        'demo', ''),
                    link.Link.make_link('bookmark',
                                        pecan.request.public_url,
                                        'demo', '',
                                        bookmark=True)
                      ]
        return v1


class Controller(rest.RestController):
    """Version 1 API controller root."""

    # Demo
    demo = demo.DemoController()
    half_plus_two = half_plus_two.HalfPlusTwoController()

    # OCR
    ocr = ocr.OCRController()

    @expose.expose(V1)
    def get(self):
        return V1.convert()


__all__ = ('Controller',)
