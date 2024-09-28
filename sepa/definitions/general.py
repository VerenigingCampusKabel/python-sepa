def code_or_proprietary(tag):
    return {
        '_self': tag,
        '_sorting': ['Cd', 'Prtry'],
        'code': 'Cd',
        'proprietary': 'Prtry'
    }

def amount_field(tag):
    return {
        '_self': tag,
        '_attribs': {
            'currency': 'Ccy'
        },
        '_nochildren': True
    }

def other(tag):
    return [{
        '_self': tag,
        '_sorting': ['Id', 'SchmeNm', 'Issr'],
        'id': 'Id',
        'scheme_name': code_or_proprietary('SchmeNm'),
        'issuer': 'Issr'
    }]

def address(tag):
    return {
        '_self': tag,
        '_sorting': ['AdrTp', 'Dept', 'SubDept', 'StrtNm', 'BldgNb', 'PstCd', 'TwnNm', 'CtrySubDvsn', 'Ctry', 'AdrLine'],
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

def party_compat(tag):
    ## Since version 2019 there is always a new subelement <Pty> after Debtor/Ultimate Deptor and Creditor/Ultimate Creditor.
    ## Here we try to be compatible with the old and new standards, until we have a better handling of different standards.
    party_struct = party(tag)
    party_struct['_sorting'].append('Pty')
    party_struct['party'] = party('Pty')
    return party_struct

def party(tag):
    return {
        '_self': tag,
        '_sorting': ['Nm', 'PstlAdr', 'Id', 'CtryOfRes', 'CtctDtls'],
        'name': 'Nm',
        'postal_address': address('PstlAdr'),
        'id': {
            '_self': 'Id',
            '_sorting': ['OrgId', 'PrvtId'],
            'organisation': {
                '_self': 'OrgId',
                '_sorting': ['AnyBIC', 'BICOrBEI', 'Othr'],
                'any_bic': 'AnyBIC',
                'bic_or_bei': 'BICOrBEI',
                'other': other('Othr')
            },
            'private': {
                '_self': 'PrvtId',
                '_sorting': ['DtAndPlcOfBirth', 'Othr'],
                'birth': {
                    '_self': 'DtAndPlcOfBirth',
                    '_sorting': ['BirthDt', 'PrvcOfBirth', 'CityOfBirth', 'CtryOfBirth'],
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
            '_self': 'CtctDtls',
            '_sorting': ['NmPrfx', 'Nm', 'PhneNb', 'MobNb', 'FaxNb', 'EmailAdr', 'Othr'],
            'name_prefix': 'NmPrfx',
            'name': 'Nm',
            'phone_number': 'PhneNb',
            'mobile_number': 'MobNb',
            'fax_number': 'FaxNb',
            'email': 'EmailAdr',
            'other': 'Othr'
        }
    }

def agent(tag):
    return {
        '_self': tag,
        '_sorting': ['FinInstnId', 'BrnchId'],
        'financial_institution': {
            '_self': 'FinInstnId',
            '_sorting': ['BICFI', 'BIC', 'ClrSysMmbId', 'Nm', 'PstlAdr', 'Othr'],
            'bicfi': 'BICFI',
            'bic': 'BIC',
            'clearing_system_member': {
                '_self': 'ClrSysMmbId',
                '_sorting': ['ClrSysId', 'MmbId'],
                'id': code_or_proprietary('ClrSysId'),
                'membmer_id': 'MmbId'
            },
            'name': 'Nm',
            'postal_address': address('PstlAdr'),
            'other': other('Othr')
        },
        'branch': {
            '_self': 'BrnchId',
            '_sorting': ['Id', 'Nm', 'PstlAdr'],
            'id': 'Id',
            'name': 'Nm',
            'postal_address': address('PstlAdr')
        }
    }

def account(tag):
    return {
        '_self': tag,
        '_sorting': ['Id', 'Tp', 'Ccy', 'Nm', 'Svcr', 'Ownr'],
        'id': {
            '_self': 'Id',
            '_sorting': ['IBAN', 'Othr'],
            'iban': 'IBAN',
            'other': other('Othr')
        },
        'type': code_or_proprietary('Tp'),
        'currency': 'Ccy',
        'name': 'Nm',
        'servicer': agent('Svcr'),
        'owner': party('Ownr')
    }

def charges(tag):
    return {
        '_self': tag,
        '_sorting': ['TtlChrgsAndTaxAmt', 'Rcrd'],
        'total': 'TtlChrgsAndTaxAmt',
        'record': [{
            '_self': 'Rcrd',
            '_sorting': ['Amt','CdtDbtInd','ChrgInclInd','Tp','Rate','Br','Agt','Tax'],
            'amount': amount_field('Amt'),
            'credit_debit_indicator': 'CdtDbtInd',
            'charge_included_indicator': 'ChrgInclInd',
            'type': 'Tp',
            'rate': 'Rate',
            'charge_bearer_code': 'Br',
            'agent': agent('DbtrAgt'),
            'tax': {
                '_self': 'Tax',
                '_sorting': ['Id', 'Rate', 'Amt'],
                'id': 'Id',
                'rate': 'Rate',
                'amount': amount_field('Amt')
            },
        }],
    }
