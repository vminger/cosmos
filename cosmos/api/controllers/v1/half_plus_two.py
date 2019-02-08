# Copyright 2019 PandoraGo Co.,LTD.
# All Rights Reserved.
#
# Tony 2019/2/4: Add half_plus_two controller.

import pecan
from pecan import rest
from six.moves import http_client
from wsme import types as wtypes

from cosmos.api import expose
from cosmos.api.controllers.v1.schemas import half_plus_two_schema
from cosmos.api.controllers.v1.views import half_plus_two_view
from cosmos.api.controllers.v1 import types
from cosmos.api import validation


class HalfPlusTwoController(rest.RestController):

    _view_builder = half_plus_two_view.ViewBuilder()

    @expose.expose(types.jsontype, body=types.jsontype,
                   status_code=http_client.CREATED)
    def post(self, request_data):
        """Half_plus_two predict.

        :param request_data: a request list within the request body.
        """
        validation.check_schema(request_data, half_plus_two_schema.predict) 
        
        context = pecan.request.context
        result = pecan.request.manager.half_plus_two_predict(context,
                                                             request_data)
        view = self._view_builder.detail(result)

        return view
