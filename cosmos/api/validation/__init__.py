# Copyright 2019 PandoraGo Co.,LTD.
# All Rights Reserved.
#
# Tony 2019/2/5: Add json schema validation.  

"""
Request Body validating middleware.

"""

import jsonschema

from cosmos.common import exception
from cosmos.common.i18n import _


def check_schema(body, schema):
    """Ensure all necessary keys are present and correct in create body.

    Check that the user-specified create body is in the expected format and
    include the required information.

    :param body: create body
    :param schema: create schema
    :raises InvalidParameterValue: if validation of create body fails.
    """
    validator = jsonschema.Draft4Validator(
        schema, format_checker=jsonschema.FormatChecker())
    try:
        validator.validate(body)
    except jsonschema.ValidationError as exc:
        raise exception.InvalidParameterValue(_('Invalid create body: %s') %
                                              exc)
