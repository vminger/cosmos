# Copyright 2019 PandoraGo Co.,LTD.
# All Rights Reserved.
#
# Tony 2019/2/3: Add pecan app & gmr.  

from oslo_config import cfg
from oslo_reports import guru_meditation_report as gmr
from oslo_reports import opts as gmr_opts
import pecan

from cosmos.api import config
from cosmos.api import hooks
from cosmos.api import middleware
#from cosmos.api.middleware import auth_token
from cosmos import version


def get_pecan_config():
    filename = config.__file__.replace('.pyc', '.py')
    return pecan.configuration.conf_from_file(filename)


def setup_app(pecan_config=None, extra_hooks=None):
    if not pecan_config:
        pecan_config = get_pecan_config()
    pecan.configuration.set_config(dict(pecan_config), overwrite=True)

    gmr_opts.set_defaults(cfg.CONF)
    gmr.TextGuruMeditation.setup_autorun(version, conf=cfg.CONF)

    app_hooks = [hooks.ConfigHook(),
                 hooks.ContextHook(pecan_config.app.acl_public_routes),
                 hooks.CoreHook(),
                 hooks.DBHook(),
                 hooks.NoExceptionTracebackHook(),
                 hooks.PublicUrlHook()]

    if extra_hooks:
        app_hooks.extend(extra_hooks)

    app = pecan.make_app(
        pecan_config.app.root,
        static_root=pecan_config.app.static_root,
        debug=True,
        force_canonical=getattr(pecan_config.app, 'force_canonical', True),
        hooks=app_hooks,
        wrap_app=middleware.ParsableErrorMiddleware,
    )

#    app = pecan.make_app(
#        pecan_config.app.root,
#        debug=False,
#    )

#    app = auth_token.AuthTokenMiddleware(
#        app, dict(cfg.CONF),
#        public_api_routes=pecan_config.app.acl_public_routes)

    return app


class VersionSelectorApplication(object):
    def __init__(self):
        pc = get_pecan_config()
        self.v1 = setup_app(pecan_config=pc)

    def __call__(self, environ, start_response):
        return self.v1(environ, start_response)


def build_wsgi_app():
    from cosmos.common import service as cosmos_service
    cosmos_service.prepare_service(sys.argv)
    return setup_app()
