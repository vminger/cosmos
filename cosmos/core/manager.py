# Copyright 2019 PandoraGo Co.,LTD.
# All Rights Reserved.
#
# Tony 2019/2/7: Add core manager.  

from oslo_log import log
from oslo_utils import excutils
from oslo_utils import importutils
from oslo_utils import uuidutils

from cosmos.common.i18n import _
from cosmos.common import flow_utils
from cosmos.core.flows import half_plus_two_flow
from cosmos import objects

LOG = log.getLogger(__name__)


class CoreManager(object):
    """Cosmos Core manager main class."""

    def __init__(self, driver=None, *args, **kwargs):
        # FIXME
        #driver = "cosmos.core.drivers.tfserving.driver.TFServingDriver"
        driver = "cosmos.core.drivers.native.driver.NativeDriver"
        self.driver = importutils.import_object(driver)

    def _create_hpt(self, context, request_spec):
        base_options = {
            'metadata': request_spec
        }

        hpt = objects.HalfPlusTwo(context=context)
        hpt.update(base_options)
        hpt.uuid = uuidutils.generate_uuid()
        hpt.name = hpt.uuid
        hpt.create()

    def half_plus_two_predict(self, context, request_spec):
        LOG.debug("Model Predict") 

        self._create_hpt(context, request_spec)

        try:
            taskflow = half_plus_two_flow.get_flow(
                context,
                self,
                request_spec
            )
        except Exception as e:
            with excutils.save_and_reraise_exception():
                msg = _("Create manager half_plus_two flow failed.")
                LOG.exception(msg) 

        def _run_flow():
            # This code executes half_plus_two flow. If something goes wrong,
            # flow reverts all job that was done and reraises an exception.
            # Otherwise, generate result.
            with flow_utils.DynamicLogListener(taskflow, logger=LOG):
                taskflow.run()

        try:
            _run_flow()
        except Exception as e:
            with excutils.save_and_reraise_exception():
                msg = _("Create manager half_plus_two flow failed.")
                LOG.exception(msg) 

        result = taskflow.storage.fetch('demo_result')

        return result

    def _create_ocr_entity(self, context, request_spec):
        base_options = {
            'metadata': request_spec
        }

        hpt = objects.HalfPlusTwo(context=context)
        hpt.update(base_options)
        hpt.uuid = uuidutils.generate_uuid()
        hpt.name = hpt.uuid
        hpt.create()

    def ocr_general(self, context, request_spec):
        LOG.debug("Model Predict") 

        #TODO:
        #self._create_ocr_entity(context, request_spec)

        try:
            taskflow = ocr_general.get_flow(
                context,
                self,
                request_spec
            )
        except Exception as e:
            with excutils.save_and_reraise_exception():
                msg = _("Create manager half_plus_two flow failed.")
                LOG.exception(msg) 

        def _run_flow():
            # This code executes half_plus_two flow. If something goes wrong,
            # flow reverts all job that was done and reraises an exception.
            # Otherwise, generate result.
            with flow_utils.DynamicLogListener(taskflow, logger=LOG):
                taskflow.run()

        try:
            _run_flow()
        except Exception as e:
            with excutils.save_and_reraise_exception():
                msg = _("Create manager ocr_general flow failed.")
                LOG.exception(msg) 

        result = taskflow.storage.fetch('demo_result')

        return result
