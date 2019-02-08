# Copyright 2019 PandoraGo Co.,LTD.
# All Rights Reserved.
#
# Tony 2019/2/3: Add pecan app.wsgi.

"""Use this file for deploying the API under uwsgi.

See http://pecan.readthedocs.org/en/latest/deployment.html for details.
"""

from cosmos.api import app

application = app.build_wsgi_app()
