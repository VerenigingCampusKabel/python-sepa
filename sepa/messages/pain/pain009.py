from sepa.definitions.mandate import mandate_group_header, mandate

# PAIN.009.001.05 - Mandate Initiation Request v5
standard = 'pain.009.001.05'
name = 'mandate_initiation_request'
definition = {
    '_namespaces': {
        None: 'urn:iso:std:iso:20022:tech:xsd:pain.009.001.05',
        'xs': 'http://www.w3.org/2001/XMLSchema'
    },
    '_self': 'MndtInitnReq',
    '_sorting': ['GrpHdr', 'Mndt', 'SplmtryData'],
    'group_header': mandate_group_header('GrpHdr'),
    'mandate': [mandate('Mndt')],
    'supplementary_data': ['SplmtryData']
}
