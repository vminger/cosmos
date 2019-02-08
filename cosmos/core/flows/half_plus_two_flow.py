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

    default_provides = set(['demo_result'])

    def __init__(self, driver):
        requires = ['context']
        super(PredictTask, self).__init__(addons=[ACTION],
                                          requires=requires)
        self.driver = driver

    def execute(self, context, request_spec, *args, **kwargs):
        demo_result = self.driver.predict("half_plus_two", request_spec)
        return {'demo_result': demo_result}

    def revert(self, result, *args, **kwargs):
        pass


def get_flow(context, manager, request_spec):
    """Constructs and returns the manager entrypoint flow."""

    flow_name = ACTION.replace(":", "_") + "_manager"
    predict_flow = linear_flow.Flow(flow_name)

    predict_what = {
        'context': context,
        'request_spec': request_spec,
    }

    predict_flow.add(PredictTask(manager.driver))

    # Now load (but do not run) the flow using the provided initial data.
    return taskflow.engines.load(predict_flow, store=predict_what)
