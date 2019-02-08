# Copyright 2019 PandoraGo Co.,LTD.
# All Rights Reserved.
#
# Tony 2019/2/5: Add api config.  

from oslo_config import cfg

from cosmos.common.i18n import _

opts = [
    cfg.HostAddressOpt('host_ip',
                       default='0.0.0.0',
                       help=_("The IP address on which cosmos-api listens.")),
    cfg.PortOpt('port',
                default=8888,
                help=_("The TCP port on which cosmos-api listens.")),
    cfg.IntOpt('max_limit',
                default=1000,
                help=_("The maximum number of items returned in a single "
                       "response from a collection resource.")),
    cfg.StrOpt('public_endpoint',
               help=_("Public URL to use when building the links to the API "
                      "resources (for example, \"https://cosmos.8888\"). "
                      "If None the links will be built using the request's "
                      "host URL. If the API is operating behind a proxy, you "
                      "will want to change this to represent the proxy's URL. "
                      "Defaults to None.")),
    cfg.IntOpt('api_workers',
               help=_("Number of workers for cosmos API service. "
                      "The default is equal to the number of CPUs available "
                      "if that can be determined, else a default worker "
                      "count of 1 is returned.")),
    cfg.BoolOpt('enable_ssl_api',
                default=False,
                help=_("Enable the integrated stand-alone API to service "
                       "requests via HTTPS instead of HTTP. If there is a "
                       "front-end service performing HTTPS offloading from "
                       "the service, this option should be False; note, you "
                       "will want to change public API endpoint to represent "
                       "SSL termination URL with 'public_endpoint' option.")),
]

opt_group = cfg.OptGroup(name='api',
                         title='Options for the cosmos-api service')


def register_opts(conf):
    conf.register_group(opt_group)
    conf.register_opts(opts, group=opt_group)
