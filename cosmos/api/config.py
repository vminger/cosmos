# Copyright 2019 PandoraGo Co.,LTD.
# All Rights Reserved.
#
# Tony 2019/2/3: Add pecan config.


# Server Specific Configurations
# See https://pecan.readthedocs.org/en/latest/configuration.html#server-configuration # noqa
server = {
    'port': '8888',
    'host': '0.0.0.0'
}

# Pecan Application Configurations
# See https://pecan.readthedocs.org/en/latest/configuration.html#application-configuration # noqa
app = {
    'root': 'cosmos.api.controllers.root.RootController',
    'modules': ['cosmos.api'],
    'static_root': '%(confdir)s/public',
    'template_path' : '%(confdir)s/project/templates',
    'debug': True,
    'acl_public_routes': [
        '/',
        '/v1',
    ],
}

# WSME Configurations
# See https://wsme.readthedocs.org/en/latest/integrate.html#configuration
wsme = {
    'debug': True,
}
