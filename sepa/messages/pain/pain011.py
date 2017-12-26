from sepa.definitions.general import code_or_proprietary, party
from sepa.definitions.mandate import mandate_group_header, original_message, mandate

# PAIN.011.001.05 - Mandate Cancellation Request v5
standard = 'pain.011.001.05'
name = 'mandate_cancellation_request'
definition = {
    '_namespaces': {
        None: 'urn:iso:std:iso:20022:tech:xsd:pain.011.001.05',
        'xs': 'http://www.w3.org/2001/XMLSchema'
    },
    '_self': 'MndtCxlReq',
    '_sorting': ['GrpHdr', 'UndrlygCxlDtls', 'SplmtryData'],
    'group_header': mandate_group_header('GrpHdr'),
    'cancellatiion': [{
        '_self': 'UndrlygCxlDtls',
        'original_message': original_message('OrgnlMsgInf'),
        'reason': {
            '_self': 'CxlRsn',
            'originator': party('Orgtr'),
            'reason': code_or_proprietary('Rsn'),
            'additional_information': ['AddtInf']
        },
        'original_mandate': {
            '_self': 'OrgnlMsgInf',
            'id': 'OrgnlMndtId',
            'mandate': mandate(' OrgnMndt')
        },
        'supplementary_data': ['SplmtryData']
    }],
    'supplementary_data': ['SplmtryData']
}
