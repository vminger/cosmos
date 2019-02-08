# Copyright 2019 PandoraGo Co.,LTD.
# All Rights Reserved.
#
# Tony 2019/2/5: Add api config.  

from oslo_config import cfg

from cosmos.conf import api
from cosmos.conf import default

CONF = cfg.CONF

api.register_opts(CONF)
default.register_opts(CONF)
