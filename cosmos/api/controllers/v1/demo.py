# Copyright 2019 PandoraGo Co.,LTD.
# All Rights Reserved.
#
# Tony 2019/2/4: Add controller demo.

from pecan import rest
from six.moves import http_client
from wsme import types as wtypes

from cosmos.api import expose
from cosmos.api.controllers.v1.schemas import demos as demo_schemas
from cosmos.api import validation


class DemoController(rest.RestController):

    @expose.expose(wtypes.text, body=wtypes.text,
                   status_code=http_client.CREATED)
    def post(self, demo):
        """Create a new demo.

        :param demo: a demo within the request body.
        """
        validation.check_schema(demo, demo_schemas.create_demo) 
        demo = demo.get("demo", {})
        return 1
