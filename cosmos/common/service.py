# Copyright 2019 PandoraGo Co.,LTD.
# All Rights Reserved.
#
# Tony 2019/2/5: Add service framework.  

from oslo_concurrency import processutils
from oslo_log import log
from oslo_service import service
from oslo_service import wsgi

from cosmos.api import app
from cosmos.common import config
from cosmos.common import exception
from cosmos.common.i18n import _
from cosmos.conf import CONF
from cosmos import objects

LOG = log.getLogger(__name__)


def prepare_service(argv=None):
    argv = [] if argv is None else argv
    log.register_options(CONF)
    log.set_defaults(default_log_levels=CONF.default_log_levels + [
        'eventlet.wsgi.server=INFO', 'cosmosclient=WARNING'])
    config.parse_args(argv)
    log.setup(CONF, 'cosmos')
    objects.register_all()


def process_launcher():
    return service.ProcessLauncher(CONF)


class WSGIService(service.ServiceBase):
    """Provides ability to launch cosmos API from WSGI app."""

    def __init__(self, name, use_ssl=False):
        """Initialize, but do not start the WSGI server.

        :param name: The name of the WSGI server given to the loader.
        :param use_ssl: Wraps the socket in an SSL context if True.
        :returns: None
        """
        self.name = name
        self.app = app.VersionSelectorApplication()
        self.workers = (CONF.api.api_workers or
                        processutils.get_worker_count())
        if self.workers and self.workers < 1:
            raise exception.ConfigInvalid(
                _("api_workers value of %d is invalid, "
                  "must be greater than 0.") % self.workers)

        self.server = wsgi.Server(CONF, name, self.app,
                                  host=CONF.api.host_ip,
                                  port=CONF.api.port,
                                  use_ssl=use_ssl)

    def start(self):
        """Start WSGI server.

        :return None
        """
        self.server.start()

    def stop(self):
        """Stop WSGI server.

        :returns: None
        """
        self.server.stop()

    def wait(self):
        """Wait until WSGI server stop.

        :returns: None
        """
        self.server.wait()

    def reset(self):
        """Reset server greenpool size to default.

        :returns: None
        """
        self.server.reset()
