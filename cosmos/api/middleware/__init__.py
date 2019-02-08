# Copyright 2019 PandoraGo Co.,LTD.
# All Rights Reserved.
#
# Tony 2019/2/8: Add parsable error middleware.  

from cosmos.api.middleware import parsable_error

ParsableErrorMiddleware = parsable_error.ParsableErrorMiddleware

__all__ = ('ParsableErrorMiddleware')
