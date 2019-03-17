# Copyright 2019 PandoraGo Co.,LTD.
# All Rights Reserved.
#
# Tony 2019/3/17: Add native driver.  

import io
import numpy as np
from PIL import Image
import requests
import shutil

import chinese_ocr
from oslo_log import log

LOG = log.getLogger(__name__)

class OCR(object):

    def __init__(self):
        self.result_dir = '/etc/cosmos/test_results'
        if os.path.exists(self.result_dir):
            shutil.rmtree(self.result_dir)
        os.mkdir(self.result_dir)

    def predict(self, model, img_base64):
        img_bytes = io.BytesIO(img_base64)
        img = np.array(Image.open(img_bytes).convert('RGB'))
        result, img_framed = chinese_ocr.model(img)
        output_file = os.path.join(self.result_dir, 'result.jpg')
        Image.fromarray(img_framed).save(output_file)
        LOG.info(result)
        return result
