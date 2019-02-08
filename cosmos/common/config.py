# Copyright 2019 PandoraGo Co.,LTD.
# All Rights Reserved.
#
# Tony 2019/2/5: Add config framework.  

from oslo_config import cfg

from cosmos import version


def parse_args(argv, default_config_files=None):
    cfg.CONF(argv[1:],
             project='cosmos',
             version=version.version_info.release_string(),
             default_config_files=default_config_files)
