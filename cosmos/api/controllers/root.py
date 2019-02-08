# Copyright 2019 PandoraGo Co.,LTD.
# All Rights Reserved.
#
# Tony 2019/2/4: Add pecan controller root.

import pecan
from pecan import rest
from wsme import types as wtypes

from cosmos.api.controllers import base
from cosmos.api.controllers import v1
from cosmos.api import expose

ID_VERSION1 = 'v1'


class Root(base.APIBase):

    name = wtypes.text
    """The name of the API"""

    description = wtypes.text
    """Some information about this API"""

    @staticmethod
    def convert():
        root = Root()
        root.name = "PandoraGo Cosmos API"
        root.description = ("Cosmos is an PandoraGo project which aims to "
                            "facilitate AI framework.")
        return root


class RootController(rest.RestController):

    _versions = [ID_VERSION1]
    """All supported API versions"""

    _default_version = ID_VERSION1
    """The default API version"""

    v1 = v1.Controller()

    @expose.expose(Root)
    def get(self):
        return Root.convert()

    @pecan.expose()
    def _route(self, args):
        """Overrides the default routing behavior.

        It redirects the request to the default version of the cosmos API
        if the version number is not specified in the url.
        """

        if args[0] and args[0] not in self._versions:
            args = [self._default_version] + args
        return super(RootController, self)._route(args)
