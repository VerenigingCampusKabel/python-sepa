from sepa.definitions.payment import payment_group_header, payment

# PAIN.008.001.07 - Customer Direct Debit Initiation v7
standard = 'pain.008.001.07'
name = 'customer_direct_debit_initiation'
definition = {
    '_namespaces': {
        None: 'urn:iso:std:iso:20022:tech:xsd:pain.008.001.07',
        'xs': 'http://www.w3.org/2001/XMLSchema'
    },
    '_self': 'CstmrDrctDbtInitn',
    '_sorting': ['GrpHdr', 'PmtInf', 'SplmtryData'],
    'group_header': payment_group_header('GrpHdr'),
    'payments': [payment('PmtInf')],
    'supplementary_data': ['SplmtryData']
}
