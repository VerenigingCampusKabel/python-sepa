def code_or_proprietary(tag):
    return {
        '_self': tag,
        'code': 'Cd',
        'proprietary': 'Prtry'
    }

def other(tag):
    return [{
        '_self': tag,
        'id': 'Id',
        'scheme_name': code_or_proprietary('SchmeNm'),
        'issuer': 'Issr'
    }]

def address(tag):
    return {
        '_self': tag,
        'address_type': 'AdrTp',
        'department': 'Dept',
        'sub_department': 'SubDept',
        'street': 'StrtNm',
        'building_number': 'BldgNb',
        'postal_code': 'PstCd',
        'town': 'TwnNm',
        'country_sub_division': 'CtrySubDvsn',
        'country': 'Ctry',
        'address': ['AdrLine']
    }


def party(tag):
    return {
        '_self': tag,
        'name': 'Nm',
        'postal_address': address('PstlAdr'),
        'id': {
            '_self': 'Id',
            'organisation': {
                '_self': 'OrgId',
                'any_bic': 'AnyBIC',
                'other': other('Othr')
            },
            'private': {
                '_self': 'PrvtId',
                'birth': {
                    '_self': 'DtAndPlcOfBirth',
                    'date': 'BirthDt',
                    'province': 'PrvcOfBirth',
                    'city': 'CityOfBirth',
                    'country': 'CtryOfBirth'
                },
                'other': other('Othr')
            }
        },
        'country': 'CtryOfRes',
        'contact_details': {
            '_self': 'CtcDtls',
            'name_prefix': 'NmPrfx',
            'name': 'Nm',
            'phone_number': 'PhneNb',
            'mobile_number': 'MobNb',
            'fax_number': 'FaxNb',
            'email': 'EmailAdr',
            'other': 'Othr'
        }
    }

def account(tag):
    return {
        '_self': tag,
        'id': {
            '_self': 'Id',
            'iban': 'IBAN',
            'other': other('Othr')
        },
        'type': code_or_proprietary('Tp'),
        'currency': 'Ccy',
        'name': 'Nm'
    }

def agent(tag):
    return {
        '_self': tag,
        'financial_institution': {
            '_self': 'FinInstnId',
            'bicfi': 'BICFI',
            'clearing_system_member': {
                '_self': 'ClrSysMmdId',
                'id': code_or_proprietary('ClrSysId'),
                'membmer_id': 'MmbId'
            },
            'name': 'Nm',
            'postal_address': address('PstlAdr'),
            'other': other('Othr')
        },
        'branch': {
            '_self': 'BrnchId',
            'id': 'Id',
            'name': 'Nm',
            'postal_address': address('PstlAdr')
        }
    }

def group_header(tag):
    return {
        '_self': tag,
        'message_id': 'MsgId',
        'creation_date_time': 'CreDtTm',
        'authorisation': code_or_proprietary('Authstn'),
        'initiating_party': party('InitgPty'),
        'instructing_agent': agent('InstgAgt'),
        'instructed_agent': agent('InstdAgt')
    }
