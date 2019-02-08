# Copyright 2019 PandoraGo Co.,LTD.
# All Rights Reserved.
#
# Tony 2019/2/4: Add controller demo.

from cosmos.api.validation import parameter_types

create_demo = {
    "type": "object",
    "properties": {
        "demo": {
            "type": "object",
            "properties": {
                "name": parameter_types.name,
                "description": parameter_types.description,
            },
        },
    },
    "required": ['demo'],
    "additionalProperties": False,
}
