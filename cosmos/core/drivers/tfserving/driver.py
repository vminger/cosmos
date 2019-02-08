# Copyright 2019 PandoraGo Co.,LTD.
# All Rights Reserved.
#
# Tony 2019/2/7: Add tensorflow serving driver.  

from cosmos.core import driver
from cosmos.core.drivers.tfserving import adapter

class TFServingDriver(driver.DeepDriver):

    def __init__(self):
        self.adapter = adapter.RESTAdapter()

    def predict(self, model, data):
        return self.adapter.predict(model, data)

    def classify(self, model, data):
        return self.adapter.classify(model, data)

    def regress(self, model, data):
        return self.adapter.regress(model, data)
