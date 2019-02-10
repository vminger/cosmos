# Copyright 2019 PandoraGo Co.,LTD.
# All Rights Reserved.
#
# Tony 2019/2/9: Add OCR general controller.

from pecan import rest
from six.moves import http_client
from wsme import types as wtypes

from cosmos.api import expose
from cosmos.api.controllers.v1.schemas import ocr_general_schema
from cosmos.api.controllers.v1.views import ocr_general_view
from cosmos.api.controllers.v1 import types
from cosmos.api import validation


class OCRGeneralController(rest.RestController):

    _view_builder = ocr_general_view.ViewBuilder()

    @expose.expose(wtypes.text, body=types.jsontype,
                   status_code=http_client.CREATED)
    def post(self, body):
        """OCR general.

        :param body: jsontype request body.
        """
        validation.check_schema(body, ocr_general_schema.create) 

        result = pecan.request.manager.ocr_general(data=body)

        view = self._view_builder.detail(result)

        return view
