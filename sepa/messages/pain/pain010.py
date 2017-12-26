from sepa.definitions.general import code_or_proprietary, party
from sepa.definitions.mandate import mandate_group_header, original_message, mandate

# PAIN.010.001.05 - Mandate Amendment Request v5
standard = 'pain.010.001.05'
name = 'mandate_amendment_request'
definition = {
    '_namespaces': {
        None: 'urn:iso:std:iso:20022:tech:xsd:pain.010.001.05',
        'xs': 'http://www.w3.org/2001/XMLSchema'
    },
    '_self': 'MndtAmdmntReq',
    '_sorting': ['GrpHdr', 'UndrlygAmdmntDtls', 'SplmtryData'],
    'group_header': mandate_group_header('GrpHdr'),
    'amendment': [{
        '_self': 'UndrlygAmdmntDtls',
        'original_message': original_message('OrgnlMsgInf'),
        'reason': {
            '_self': 'AmdmntRsn',
            'originator': party('Orgtr'),
            'reason': code_or_proprietary('Rsn'),
            'additional_information': ['AddtInf']
        },
        'mandate': mandate('Mndt'),
        'original_mandate': {
            '_self': 'OrgnlMsgInf',
            'id': 'OrgnlMndtId',
            'mandate': mandate(' OrgnMndt')
        },
        'supplementary_data': ['SplmtryData']
    }],
    'supplementary_data': ['SplmtryData']
}
