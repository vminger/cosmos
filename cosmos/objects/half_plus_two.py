# Copyright 2019 PandoraGo Co.,LTD.
# All Rights Reserved.
#
# Tony 2019/2/10: Add half_plus_two object.  

from oslo_db import exception as db_exc
from oslo_log import log as logging
from oslo_versionedobjects import base as object_base

from cosmos.db import api as dbapi
from cosmos import objects
from cosmos.objects import base
from cosmos.objects import fields as object_fields

OPTIONAL_ATTRS = ['fault']


LOG = logging.getLogger(__name__)


@base.CosmosObjectRegistry.register
class HalfPlusTwo(base.CosmosObject, object_base.VersionedObjectDictCompat):
    # Version 1.0: Initial version
    VERSION = '1.0'

    dbapi = dbapi.get_instance()

    fields = {
        'id': object_fields.IntegerField(),
        'uuid': object_fields.UUIDField(nullable=False),
        'name': object_fields.StringField(nullable=False),
        'description': object_fields.StringField(nullable=True),
        'project_id': object_fields.UUIDField(nullable=True),
        'user_id': object_fields.UUIDField(nullable=True),
        'status': object_fields.StringField(nullable=True),
        'metadata': object_fields.FlexibleDictField(nullable=True),
        'system_metadata': object_fields.FlexibleDictField(nullable=True),
    }

    def __init__(self, context=None, **kwargs):
        super(HalfPlusTwo, self).__init__(context=context, **kwargs)

    @staticmethod
    def _from_db_object(hpt, db_hpt, expected_attrs=None):
        """Method to help with migration to objects.

        Converts a database entity to a formal object.

        :param hpt: An object of the HalfPlusTwo class.
        :param db_hpt: A DB HalfPlusTwo model of the object
        :return: The object of the class with the database entity added
        """
        for field in set(hpt.fields) - set(OPTIONAL_ATTRS):
            if field == 'metadata':
                hpt[field] = db_hpt['extra']
            else:
                hpt[field] = db_hpt[field]

        if expected_attrs is None:
            expected_attrs = []

        hpt.obj_reset_changes()
        return hpt

    @staticmethod
    def _from_db_object_list(db_objects, cls, context):
        """Converts a list of database entities to a list of formal objects."""
        hpts = []
        for obj in db_objects:
            expected_attrs = ['fault']
            hpts.append(HalfPlusTwo._from_db_object(cls(context),
                                                    obj,
                                                    expected_attrs))
        return hpts

    @classmethod
    def list(cls, context, limit=None, marker=None, sort_key=None,
             sort_dir=None, project_only=False,
             filters=None):
        """Return a list of HalfPlusTwo objects."""
        db_HPTs = cls.dbapi.hpt_get_all(context,
                                        project_only=project_only,
                                        limit=limit,
                                        marker=marker,
                                        sort_key=sort_key,
                                        sort_dir=sort_dir,
                                        filters=filters)
        return HalfPlusTwo._from_db_object_list(db_HPTs, cls, context)

    @classmethod
    def get(cls, context, uuid):
        """Find a HalfPlusTwo and return a HalfPlusTwo object."""
        expected_attrs = ['fault']
        db_HPT = cls.dbapi.hpt_get(context, uuid)
        hpt = HalfPlusTwo._from_db_object(cls(context), db_hpt,
                                          expected_attrs)
        return hpt

    def create(self, context=None):
        """Create a HalfPlusTwo record in the DB."""
        values = self.obj_get_changes()
        metadata = values.pop('metadata', None)
        if metadata is not None:
            values['extra'] = metadata
        db_hpt = self.dbapi.hpt_create(context, values)
        expected_attrs = None
        self._from_db_object(self, db_hpt, expected_attrs)

    def destroy(self, context=None):
        """Delete the HalfPlusTwo from the DB."""
        self.dbapi.hpt_destroy(context, self.uuid)
        self.obj_reset_changes()

    def save(self, context=None):
        """Save updates to this HalfPlusTwo."""
        updates = self.obj_get_changes()
        for field in list(updates):
            if (self.obj_attr_is_set(field) and
                    isinstance(self.fields[field], object_fields.ObjectField)
                    and getattr(self, field, None) is not None):
                try:
                    getattr(self, '_save_%s' % field)(context)
                except AttributeError:
                    LOG.exception('No save handler for %s', field, hpt=self)
                except db_exc.DBReferenceError as exp:
                    if exp.key != 'hpt_uuid':
                        raise
                updates.pop(field)

        metadata = updates.pop('metadata', None)
        if metadata is not None:
            updates['extra'] = metadata
        self.dbapi.hpt_update(context, self.uuid, updates)
        self.obj_reset_changes()

    def refresh(self, context=None):
        """Refresh the object by re-fetching from the DB."""
        current = self.__class__.get(context, self.uuid)
        self.obj_refresh(current)
        self.obj_reset_changes()
