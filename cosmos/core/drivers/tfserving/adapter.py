# Copyright 2019 PandoraGo Co.,LTD.
# All Rights Reserved.
#
# Tony 2019/2/7: Add tensorflow serving driver.  

from cosmos.core.drivers.tfserving import grpc as tf_grpc
from cosmos.core.drivers.tfserving import rest as tf_rest


class RESTAdapter(object):

    ip = "0.0.0.0"
    port = "8501"
    username = "admin"
    password = "pwd"
    tf_version = "v1"
    model_version = "00000123"

    def __init__(self):
        self.rest = tf_rest.REST(self.ip, self.port, self.username,
            self.password, self.tf_version, self.model_version)

    def predict(self, model, data):
        return self.rest.predict(model, data)

    def classify(self, data):
        return self.rest.classify(data)

    def regress(self, data):
        return self.rest.regress(data)


class GRPCAdapter(object):

    def __init__(self):
        self.grpc = tf_grpc.GRPC()

    def predict(self, data):
        return self.grpc.predict(data)

    def classify(self, data):
        return self.grpc.classify(data)

    def regress(self, data):
        return self.grpc.regress(data)
