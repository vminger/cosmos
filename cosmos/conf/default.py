# Copyright 2019 PandoraGo Co.,LTD.
# All Rights Reserved.
#
# Tony 2019/2/8: Add default config.  

import os
import socket
import tempfile

from oslo_config import cfg

from cosmos.common.i18n import _

api_opts = [
    cfg.BoolOpt('debug_tracebacks_in_api',
                default=False,
                help=_('Return server tracebacks in the API response for any '
                       'error responses. WARNING: this is insecure '
                       'and should not be used in a production environment.')),
    cfg.IntOpt('password_length',
               default=12,
               min=0,
               help='Length of generated server admin passwords.'),
]

exc_log_opts = [
    cfg.BoolOpt('fatal_exception_format_errors',
                default=False,
                help=_('Used if there is a formatting error when generating '
                       'an exception message (a programming error). If True, '
                       'raise an exception; if False, use the unformatted '
                       'message.')),
]

path_opts = [
    cfg.StrOpt('pybasedir',
               default=os.path.abspath(os.path.join(os.path.dirname(__file__),
                                                    '../')),
               sample_default='/usr/lib/python/site-packages/mogan/mogan',
               help=_('Directory where the mogan python module is '
                      'installed.')),
    cfg.StrOpt('bindir',
               default='$pybasedir/bin',
               help=_('Directory where mogan binaries are installed.')),
    cfg.StrOpt('state_path',
               default='$pybasedir',
               help=_("Top-level directory for maintaining mogan's state.")),
]

service_opts = [
    cfg.IntOpt('periodic_interval',
               default=60,
               help=_('Default interval (in seconds) for running periodic '
                      'tasks.')),
    cfg.HostAddressOpt('host',
                       default=socket.getfqdn(),
                       sample_default='localhost',
                       help=_('Name of this node. This can be an opaque '
                              'identifier. It is not necessarily a hostname, '
                              'FQDN, or IP address. However, the node name '
                              'must be valid within an AMQP key, and if using '
                              'ZeroMQ, a valid hostname, FQDN, or IP address.')
                       ),
]

utils_opts = [
    cfg.StrOpt('tempdir',
               default=tempfile.gettempdir(),
               sample_default='/tmp',
               help=_('Temporary working directory, default is Python temp '
                      'dir.')),
]


def register_opts(conf):
    conf.register_opts(api_opts)
    conf.register_opts(exc_log_opts)
    conf.register_opts(service_opts)
    conf.register_opts(path_opts)
    conf.register_opts(utils_opts)
