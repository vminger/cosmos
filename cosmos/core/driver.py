# Copyright 2019 PandoraGo Co.,LTD.
# All Rights Reserved.
#
# Tony 2019/2/7: Add core driver interface.  


class DeepDriver(object):

    def predict(self, model, data):
        raise NotImplementedError

    def classify(self, model, data):
        raise NotImplementedError

    def regress(self, model, data):
        raise NotImplementedError
