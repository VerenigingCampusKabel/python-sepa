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
