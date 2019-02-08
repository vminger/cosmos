# Copyright 2019 PandoraGo Co.,LTD.
# All Rights Reserved.
#
# Tony 2019/2/7: Add version view.  

import copy
import re

from oslo_config import cfg
from six.moves import urllib


versions_opts = [
    cfg.StrOpt('public_endpoint',
               help="Public url to use for versions endpoint. The default "
                    "is None, which will use the request's host_url "
                    "attribute to populate the URL base. If Cinder is "
                    "operating behind a proxy, you will want to change "
                    "this to represent the proxy's URL."),
]

CONF = cfg.CONF
CONF.register_opts(versions_opts)


def get_view_builder(req):
    base_url = CONF.public_endpoint or req.application_url
    return ViewBuilder(base_url)


class ViewBuilder(object):
    def __init__(self, base_url):
        """Initialize ViewBuilder.

        :param base_url: url of the root wsgi application
        """
        self.base_url = base_url

    def build_versions(self, versions):
        views = [self._build_version(versions[key])
                 for key in sorted(list(versions.keys()))]
        return dict(versions=views)

    def _build_version(self, version):
        view = copy.deepcopy(version)
        view['links'] = self._build_links(version)
        return view

    def _build_links(self, version_data):
        """Generate a container of links that refer to the provided version."""
        links = copy.deepcopy(version_data.get('links', {}))
        version_num = version_data["id"].split('.')[0]
        links.append({'rel': 'self',
                      'href': self._generate_href(version=version_num)})
        return links

    def _generate_href(self, version='v1', path=None):
        """Create a URL that refers to a specific version_number."""
        base_url = self._get_base_url_without_version()
        rel_version = version.lstrip('/')
        href = urllib.parse.urljoin(base_url, rel_version).rstrip('/') + '/'
        if path:
            href += path.lstrip('/')
        return href

    def _get_base_url_without_version(self):
        """Get the base URL with out the /v1 suffix."""
        return re.sub('v[1-9]+/?$', '', self.base_url)
