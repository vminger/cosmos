# Copyright 2019 PandoraGo Co.,LTD.
# All Rights Reserved.
#
# Tony 2019/2/9: Add db framework.  

"""
Database setup and migration commands.
"""

from oslo_config import cfg
from oslo_db import options
from stevedore import driver


options.set_defaults(cfg.CONF)

_IMPL = None


def get_backend():
    global _IMPL
    if not _IMPL:
        cfg.CONF.import_opt('backend', 'oslo_db.options', group='database')
        _IMPL = driver.DriverManager("cosmos.database.migration_backend",
                                     cfg.CONF.database.backend).driver
    return _IMPL


def upgrade(version=None):
    """Migrate the database to `version` or the most recent version."""
    return get_backend().upgrade(version)


def version():
    return get_backend().version()


def stamp(version):
    return get_backend().stamp(version)


def revision(message, autogenerate):
    return get_backend().revision(message, autogenerate)


def create_schema():
    return get_backend().create_schema()
