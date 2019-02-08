# Copyright 2019 PandoraGo Co.,LTD.
# All Rights Reserved.
#
# Tony 2019/2/5: Add controller ocr.

from pecan import rest
from six.moves import http_client
from wsme import types as wtypes

from cosmos.api import expose
from cosmos.api.controllers.v1.schemas import ocr as ocr_schemas
from cosmos.api.cotrollers.v1 import types
from cosmos.api import validation


class DemoController(rest.RestController):

    @expose.expose(wtypes.text, body=types.jsontype,
                   status_code=http_client.CREATED)
    def post(self, demo):
        """Create a new demo.

        :param demo: a demo within the request body.
        """
        validation.check_schema(demo, demo_schemas.create_demo) 
        demo = demo.get("demo", {})
        return demo
