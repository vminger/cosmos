# Copyright 2019 PandoraGo Co.,LTD.
# All Rights Reserved.
#
# Tony 2019/2/10: Add OCR general view.  

from cosmos.api import common

class ViewBuilder(common.ViewBuilder):
    """Model a OCR general API response as a python dictonary."""

    _collection_name = "ocr_general"

    def __init__(self):
        """Initialize view builder."""
        super(ViewBuilder, self).__init__()

    def detail(self, result): 
        """Detailed view of result."""
        result_ref = {
            'ocr': result
        }
        return result_ref
