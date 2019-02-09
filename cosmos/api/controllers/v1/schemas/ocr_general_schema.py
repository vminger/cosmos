# Copyright 2019 PandoraGo Co.,LTD.
# All Rights Reserved.
#
# Tony 2019/2/9: Add OCR general schema.

from cosmos.api.validation import parameter_types

create = {
    'type': 'object',
    'properties': {
        'ocr': {
            'type': 'object',
            'properties': {
                'type': 'string',
                'format': 'base64',
                'minLength': 0,
                'maxLength': 255,
            },
        },
    },
    'required': ['ocr'],
    'additionalProperties': False,
}
