# Copyright 2019 PandoraGo Co.,LTD.
# All Rights Reserved.
#
# Tony 2019/2/9: Add database framework.  

"""
Base class for database framework.
"""

import abc

from oslo_config import cfg
from oslo_db import api as db_api
import six


_BACKEND_MAPPING = {'sqlalchemy': 'cosmos.db.sqlalchemy.api'}
IMPL = db_api.DBAPI.from_config(cfg.CONF, backend_mapping=_BACKEND_MAPPING,
                                lazy=True)


def get_instance():
    """Return a DB API instance."""
    return IMPL


@six.add_metaclass(abc.ABCMeta)
class Connection(object):
    """Base class for db connections."""

    @abc.abstractmethod
    def __init__(self):
        """Constructor."""

    # Half plus two model.
    @abc.abstractmethod
    def hpt_create(self, context, values):
        """Create a new half_plus_two."""
