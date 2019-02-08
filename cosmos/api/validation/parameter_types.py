# Copyright 2019 PandoraGo Co.,LTD.
# All Rights Reserved.
#
# Tony 2019/2/5: Add json schema validation.  

"""
Common parameter types for validating request Body.

"""


positive_integer = {
    'type': ['integer', 'string'],
    'pattern': '^[0-9]*$', 'minimum': 1, 'minLength': 1
}


non_negative_integer = {
    'type': ['integer', 'string'],
    'pattern': '^[0-9]*$', 'minimum': 0, 'minLength': 1
}


name = {
    'type': 'string', 'minLength': 1, 'maxLength': 255,
}


description = {
    'type': ['string', 'null'], 'minLength': 0, 'maxLength': 255,
}


admin_password = {
    # NOTE: admin_password is the admin password of a server
    # instance, and it is not stored into mogan's data base.
    # In addition, users set sometimes long/strange string
    # as password. It is unnecessary to limit string length
    # and string pattern.
    'type': 'string',
}


node_uuid = {
    'type': 'string', 'format': 'uuid'
}


metadata = {
    'type': 'object',
    'patternProperties': {
        '^[a-zA-Z0-9-_:. ]{1,255}$': {
            'type': 'string', 'maxLength': 255
        }
    },
    'additionalProperties': False
}


resources = {
    'type': 'object',
    'patternProperties': {
        '^[a-zA-Z0-9-_:.]{1,255}$': positive_integer
    },
    'additionalProperties': False
}


mac_address = {
    'type': 'string',
    'pattern': '^([0-9a-fA-F]{2})(:[0-9a-fA-F]{2}){5}$'
}


ip_address = {
    'type': 'string',
    'oneOf': [
        {'format': 'ipv4'},
        {'format': 'ipv6'}
    ]
}

personality = {
    'type': 'array',
    'items': {
        'type': 'object',
        'properties': {
            'path': {'type': 'string'},
            'contents': {
                'type': 'string',
                'format': 'base64'
            }
        },
        'additionalProperties': False,
    }
}


boolean = {
    'type': ['boolean', 'string'],
    'enum': [True, 'True', 'TRUE', 'true', '1', 'ON', 'On', 'on',
             'YES', 'Yes', 'yes',
             False, 'False', 'FALSE', 'false', '0', 'OFF', 'Off', 'off',
             'NO', 'No', 'no'],
}
