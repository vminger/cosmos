# Copyright 2019 PandoraGo Co.,LTD.
# All Rights Reserved.
#
# Tony 2019/2/8: Add microversions.  

from cosmos.common import utils


class VersionedMethod(utils.ComparableMixin):

    def __init__(self, name, start_version, end_version, experimental, func):
        """Versioning information for a single method.

        Minimum and maximums are inclusive.

        :param name: Name of the method
        :param start_version: Minimum acceptable version
        :param end_version: Maximum acceptable_version
        :param func: Method to call
        """
        self.name = name
        self.start_version = start_version
        self.end_version = end_version
        self.experimental = experimental
        self.func = func

    def __str__(self):
        args = {
            'name': self.name,
            'start': self.start_version,
            'end': self.end_version
        }
        return ("Version Method %(name)s: min: %(start)s, max: %(end)s" % args)

    def _cmpkey(self):
        """Return the value used by ComparableMixin for rich comparisons."""
        return self.start_version
