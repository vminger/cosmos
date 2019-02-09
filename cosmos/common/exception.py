# Copyright 2019 PandoraGo Co.,LTD.
# All Rights Reserved.
#
# Tony 2019/2/5: Add config framework.  

from oslo_log import log as logging
import six
from six.moves import http_client

from cosmos.common.i18n import _
from cosmos.conf import CONF

LOG = logging.getLogger(__name__)


class CosmosException(Exception):
    """Base Cosmos Exception

    To correctly use this class, inherit from it and define
    a '_msg_fmt' property. That message will get printf'd
    with the keyword arguments provided to the constructor.

    If you need to access the message from an exception you should use
    six.text_type(exc).

    """
    _msg_fmt = _("An unknown exception occurred.")
    code = http_client.INTERNAL_SERVER_ERROR
    headers = {}
    safe = False

    def __init__(self, message=None, **kwargs):
        self.kwargs = kwargs

        if 'code' not in self.kwargs:
            try:
                self.kwargs['code'] = self.code
            except AttributeError:
                pass

        if not message:
            try:
                message = self._msg_fmt % kwargs
            except Exception: 
                # kwargs doesn't match a variable in self._msg_fmt
                # log the issue and the kwargs
                LOG.exception("Exception in string format operation")
                for name, value in kwargs.items():
                    LOG.error("%s: %s" % (name, value))

                if CONF.fatal_exception_format_errors:
                    raise
                else:
                    # At least get the core self._msg_fmt out if something
                    # happened.
                    message = self._msg_fmt

        super(CosmosException, self).__init__(message)

    def __str__(self):
        """Encode to utf-8 then wsme api can consume it as well."""
        if not six.PY3:
            return unicode(self.args[0]).encode('utf-8')

        return self.args[0]

    def __unicode__(self):
        """Return a unicode representation of the exception message."""
        return unicode(self.args[0])


class Conflict(CosmosException):
    _msg_fmt = _('Conflict.')
    code = http_client.CONFLICT


class ServerAlreadyExists(Conflict):
    _msg_fmt = _("HalfPlusTwo with name %(name)s already exists.")


class ConfigInvalid(CosmosException):
    _msg_fmt = _("Invalid configuration file. %(error_msg)s")


class Invalid(CosmosException):
    _msg_fmt = _("Unacceptable parameters.")
    code = http_client.BAD_REQUEST


class InvalidParameterValue(Invalid):
    _msg_fmt = _("%(err)s")
