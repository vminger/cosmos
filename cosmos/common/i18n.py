# Copyright 2019 PandoraGo Co.,LTD.
# All Rights Reserved.
#
# Tony 2019/2/5: Add i18n.  

import oslo_i18n as i18n

_translators = i18n.TranslatorFactory(domain='cosmos')

# The primary translation function using the well-known name "_"
_ = _translators.primary
