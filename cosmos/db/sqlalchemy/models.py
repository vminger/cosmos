# Copyright 2019 PandoraGo Co.,LTD.
# All Rights Reserved.
#
# Tony 2019/2/9: Add database framework.  

"""
SQLAlchemy models for cosmos service.
"""

from os import path

from oslo_db import options as db_options
from oslo_db.sqlalchemy import models
from oslo_db.sqlalchemy import types as db_types
import six.moves.urllib.parse as urlparse
from sqlalchemy import (Boolean, Column, DateTime, Enum, ForeignKey,
                        Index, Text)
from sqlalchemy import orm
from sqlalchemy import schema, String, Integer
from sqlalchemy.dialects.mysql import MEDIUMTEXT
from sqlalchemy.ext.declarative import declarative_base

from cosmos.conf import CONF

_DEFAULT_SQL_CONNECTION = 'sqlite:///' + path.join('$state_path',
                                                   'cosmos.sqlite')


db_options.set_defaults(CONF, connection=_DEFAULT_SQL_CONNECTION)


def MediumText():
    return Text().with_variant(MEDIUMTEXT(), 'mysql')


def table_args():
    engine_name = urlparse.urlparse(CONF.database.connection).scheme
    if engine_name == 'mysql':
        return {'mysql_engine': 'InnoDB',
                'mysql_charset': "utf8"}
    return None


class CosmosBase(models.TimestampMixin,
                models.ModelBase):

    metadata = None

    def as_dict(self):
        d = {}
        for c in self.__table__.columns:
            d[c.name] = self[c.name]
        return d


Base = declarative_base(cls=CosmosBase)


class HalfPlusTwo(Base):
    """Represents possible types for servers."""

    __tablename__ = 'half_plus_two_t'
    __table_args__ = (
        Index('half_plus_tow_project_id_idx', 'project_id'),
        schema.UniqueConstraint('uuid', name='uniq_halfplustwo0uuid'),
        table_args()
    )
    id = Column(Integer, primary_key=True)
    uuid = Column(String(36), nullable=False)
    name = Column(String(255), nullable=False)
    description = Column(String(255), nullable=True)
    project_id = Column(String(36), nullable=True)
    user_id = Column(String(36), nullable=True)
    status = Column(String(255), nullable=True)
    extra = Column(db_types.JsonEncodedDict)
    system_metadata = Column(db_types.JsonEncodedDict, nullable=True)


class OcrGeneral(Base):
    """Represents possible types for servers."""

    __tablename__ = 'ocr_general_t'
    __table_args__ = (
        Index('ocr_general_id_idx', 'project_id'),
        schema.UniqueConstraint('uuid', name='uniq_halfplustwo0uuid'),
        table_args()
    )
    id = Column(Integer, primary_key=True)
    uuid = Column(String(36), nullable=False)
    name = Column(String(255), nullable=False)
    description = Column(String(255), nullable=True)
    project_id = Column(String(36), nullable=True)
    user_id = Column(String(36), nullable=True)
    status = Column(String(255), nullable=True)
    extra = Column(db_types.JsonEncodedDict)
    system_metadata = Column(db_types.JsonEncodedDict, nullable=True)
