# Copyright 2019 PandoraGo Co.,LTD.
# All Rights Reserved.
#
# Tony 2019/2/7: Add tensorflow serving driver.  

import requests

from oslo_log import log

LOG = log.getLogger(__name__)

class REST(object):

    def __init__(self, ip, port, username, password,
            tf_version, model_version):
        self.ip = ip
        self.port = port
        self.username = username
        self.password = password
        self.tf_version = tf_version
        self.model_version = model_version
        self.base_url = "http://" + ip + ":" + port

    def predict(self, model, data):
        ACTION = "predict"
        url = self.base_url + "/" + self.tf_version + "/models/" + model \
            + "/versions/" + self.model_version + ":" + ACTION
        LOG.debug("predict url: %s" % url) 
        LOG.debug("predict data: %s" % data) 
        LOG.debug(type(data))
        result = self._post(url, data)
        LOG.debug("predict result: %s" % result) 
        return result

    def _post(self, url, data):
        response = requests.post(url, json=data)
        result = response.json()
        return result
