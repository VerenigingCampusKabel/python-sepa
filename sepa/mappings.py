code_or_proprietary = {
    'code': 'Cd',
    'proprietary': 'Prtry'
}

mappings = {
    'mandates': [
        'id': 'MndtId',
        'request_id': 'MndtReqId',

        'authentication': [{
            '_self': 'Authntcn',
            'date': 'Dt',
            'channel': code_or_proprietary
        }],

        'initiating_party': {
            '_self': 'InitgPty',
            'name': 'Nm',
            'postal_address': address,
            'id': {
                'organisation': {
                    '_self': 'OrgId'
                },
                'private': {
                    '_self': 'PrvtId'
                }
            }
        },

        'type': {
            '_self': 'Tp',
            'service_level': {
                '_self': 'SvcLvl',
                'code': 'Cd',
                'proprietary': 'Prpty'
            }
        }
    ]
}
