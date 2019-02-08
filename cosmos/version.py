# Copyright 2019 PandoraGo Co.,LTD.
# All Rights Reserved.
#
# Tony 2019/2/3: Add pecan app & gmr.  

import pbr.version

COSMOS_PRODUCT = "PandoraGo Cosmos"

version_info = pbr.version.VersionInfo('cosmos')
version_string = version_info.version_string


def product_string():
    return COSMOS_PRODUCT


def version_string_with_package():
    return version_info.version_string()
