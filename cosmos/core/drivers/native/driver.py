# Copyright 2019 PandoraGo Co.,LTD.
# All Rights Reserved.
#
# Tony 2019/3/16: Add native driver.  

from cosmos.core import driver
from cosmos.core.drivers.native import adapter

class NativeDriver(driver.DeepDriver):

    def __init__(self):
        self.adapter = adapter.NativeAdapter()

    def predict(self, model, data):
        return self.adapter.predict(model, data)

    def classify(self, model, data):
        return self.adapter.classify(model, data)

    def regress(self, model, data):
        return self.adapter.regress(model, data)
