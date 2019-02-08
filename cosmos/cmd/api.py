# Copyright 2019 PandoraGo Co.,LTD.
# All Rights Reserved.
#
# Tony 2019/2/4: Add server to serve app.

"""The Mogan Service API."""

import sys

from oslo_config import cfg
from oslo_reports import guru_meditation_report as gmr
from oslo_reports import opts as gmr_opts

from cosmos import version
from cosmos.common import service as cosmos_service

CONF = cfg.CONF


def main():
    # Parse config file and command line options, then start logging.
    cosmos_service.prepare_service(sys.argv)
    gmr_opts.set_defaults(CONF)
    gmr.TextGuruMeditation.setup_autorun(version, conf=CONF)

    # Build and start the WSGI server.
    launcher = cosmos_service.process_launcher()
    server = cosmos_service.WSGIService('cosmos_api', CONF.api.enable_ssl_api)
    launcher.launch_service(server, workers=server.workers)
    launcher.wait()
