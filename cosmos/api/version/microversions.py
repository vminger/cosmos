# Copyright 2019 PandoraGo Co.,LTD.
# All Rights Reserved.
#
# Tony 2019/2/8: Add microversions.  

"""API Microversion definitions.

All new microversions should have a constant added here to be used throughout
the code instead of the specific version number. Until patches land, it's
common to end up with merge conflicts with other microversion changes. Merge
conflicts will be easier to handle via the microversion constants defined here
as the version number will only need to be changed in a single location.

Actual version numbers should be used:

  * In this file
  * In cosmos/api/version/rest_api_version_history.rst
  * In cosmos/api/version/api_version_request.py
  * In release notes describing the new functionality
  * In updates to api-ref

Nearly all microversion changes should include changes to all of those
locations. Make sure to add relevant documentation, and make sure that
documentation includes the final version number used.
"""

from cosmos.api.version import api_version_request as api_version
from cosmos.common import exception


# Add new constants here for each new microversion.

V1_BASE_VERSION = '1.0'


def get_mv_header(version):
    """Gets a formatted HTTP microversion header.

    :param version: The microversion needed.
    :return: A tuple containing the microversion header with the
             requested version value.
    """
    return {'Cosmos-API-Version':
            'volume %s' % version}


def get_api_version(version):
    """Gets a ``APIVersionRequest`` instance.

    :param version: The microversion needed.
    :return: The ``APIVersionRequest`` instance.
    """
    return api_version.APIVersionRequest(version)


def get_prior_version(version):
    """Gets the microversion before the given version.

    Mostly useful for testing boundaries. This gets the microversion defined
    just prior to the given version.

    :param version: The version of interest.
    :return: The version just prior to the given version.
    """
    parts = version.split('.')

    if len(parts) != 2 or parts[0] != '3':
        raise exception.InvalidInput(reason='Version %s is not a valid '
                                     'microversion format.' % version)

    minor = int(parts[1]) - 1

    if minor < 0:
        # What's your problem? Are you trying to be difficult?
        minor = 0

    return '%s.%s' % (parts[0], minor)
