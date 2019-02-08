# Copyright 2019 PandoraGo Co.,LTD.
# All Rights Reserved.
#
# Tony 2019/2/7: Add half_plus_two view.  

from cosmos.api import common

class ViewBuilder(common.ViewBuilder):
    """Model a half_plus_two API response as a python dictonary."""

    _collection_name = "half_plus_two"

    def __init__(self):
        """Initialize view builder."""
        super(ViewBuilder, self).__init__()

    def detail(self, result): 
        """Detailed view of result."""
        result_ref = {
            'half_plus_two': result
        }
        return result_ref
