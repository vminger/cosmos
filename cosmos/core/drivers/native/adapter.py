# Copyright 2019 PandoraGo Co.,LTD.
# All Rights Reserved.
#
# Tony 2019/3/16: Add native driver.  

from cosmos.core.drivers.native import ocr


class NativeAdapter(object):

    def __init__(self):
        self.ocr = ocr.OCR

    def predict(self, model, data):
        return self.ocr.predict(model, data)

    def classify(self, data):
        return self.ocr.classify(data)

    def regress(self, data):
        return self.ocr.regress(data)
