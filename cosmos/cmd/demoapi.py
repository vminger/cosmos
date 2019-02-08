# Copyright 2019 PandoraGo Co.,LTD.
# All Rights Reserved.
#
# Tony 2019/2/4: Add server to serve app.

"""The Mogan Service API."""

from wsgiref.simple_server import make_server

from cosmos.api import app as pecan_app

def main():
    app = pecan_app.VersionSelectorApplication()
    httpd = make_server('0.0.0.0', 8888, app)
    httpd.serve_forever()
