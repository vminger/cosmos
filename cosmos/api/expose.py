# Copyright 2019 PandoraGo Co.,LTD.
# All Rights Reserved.
#
# Tony 2019/2/4: Add pecan expose.

import wsmeext.pecan as wsme_pecan


def expose(*args, **kwargs):
    """Ensure that only JSON, and not XML, is supported."""
    if 'rest_content_types' not in kwargs:
        kwargs['rest_content_types'] = ('json',)
    return wsme_pecan.wsexpose(*args, **kwargs)
