# Copyright 2019 PandoraGo Co.,LTD.
# All Rights Reserved.
#
# Tony 2019/2/3: Add predict taskflow.  

import taskflow.engines
from taskflow.patterns import linear_flow

from cosmos.common import flow_utils

ACTION = 'model:predict'


class PredictTask(flow_utils.CosmosTask):
    """Model Predict."""

    def __init__(self, driver):
        requires = ['context']
        super(PredictTask, self).__init__(addons=[ACTION],
                                          requires=requires)
        self.driver = driver

    def execute(self, context):
        self.driver.predict(context)

    def revert(self, context):
        pass


def get_flow(context, manager, predict, request_spec):
    """Constructs and returns the manager entrypoint flow."""

    fow_name = ACTION.replace(":", "_") + "_manager"
    predict_flow = linear_flow.Flow(flow_name)

    predict_what = {
        'context': context,
        'request_spec': request_spec,
        'predict': predict
    }

    predict_flow.add(PredictTask(manager.driver))

    # Now load (but do not run) the flow using the provided initial data.
    return taskflow.engines.load(predict_flow, store=predict_what)
