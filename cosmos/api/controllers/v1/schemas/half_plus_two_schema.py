# Copyright 2019 PandoraGo Co.,LTD.
# All Rights Reserved.
#
# Tony 2019/2/4: Add half_plus_two schema.

from cosmos.api.validation import parameter_types

# {'instances': [1.0, 2.0, 5.0]}
predict = {
    'type': 'object',
    'properties': {
        'instances': {
            'type': 'array',
            'minItems': 1,
            'items': {
                'type': 'integer',
            }
        },
    },
    'required': ['instances'],
    'additionalProperties': False,
}
