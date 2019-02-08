# Copyright 2019 PandoraGo Co.,LTD.
# All Rights Reserved.
#
# Tony 2019/2/4: Add pecan controller link.

import pecan
from wsme import types as wtypes

from cosmos.api.controllers import base


def build_url(resource, resource_args, bookmark=False, base_url=None):
    if base_url is None:
        base_url = pecan.request.public_url

    template = '%(url)s/%(res)s' if bookmark else '%(url)s/v1/%(res)s'
    # FIXME(Tony): I'm getting a 404 when doing a GET on
    # a nested resource that the URL ends with a  '/'.
    # https://groups.google.com/forum/#!topic/pecan-dev/QfSeviLg5qs
    template += '%(args)s' if resource_args.startswith('?') else '/%(args)s'
    return template % {'url': base_url, 'res': resource, 'args': resource_args}


class Link(base.APIBase):
    """A link representation."""

    href = wtypes.text
    """The url of a link."""

    rel = wtypes.text
    """The name of a link."""

    type = wtypes.text
    """Indicates the type of document/link."""

    @staticmethod
    def make_link(rel_name, url, resource, resource_args,
                  bookmark=False, type=wtypes.Unset):
        href = build_url(resource, resource_args,
                         bookmark=bookmark, base_url=url)
        return Link(href=href, rel=rel_name, type=type)

    @classmethod
    def sample(cls):
        sample = cls(href="http://localhost:8888/types/"
                          "135e9fec-499d-41ec-981d-6f01e3b13074",
                     rel="bookmark")
        return sample
