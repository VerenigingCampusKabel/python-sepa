from sepa.definitions.statement import statement_group_header
from sepa.definitions.notification import notification

# CAMT.054.001.06 - Bank To Customer Debit Credit Notification v6
standard = 'camt.054.001.06'
compatible_standards = ['camt.054.001.04','camt.054.001.08']
name = 'bank_to_customer_debit_credit_notification'
definition = {
    '_namespaces': {
        None: 'urn:iso:std:iso:20022:tech:xsd:camt.054.001.06',
        'xs': 'http://www.w3.org/2001/XMLSchema'
    },
    '_self': 'BkToCstmrDbtCdtNtfctn',
    '_sorting': ['GrpHdr', 'Ntfctn','SplmtryData'],
    'group_header': statement_group_header('GrpHdr'),
    'notifications': [notification('Ntfctn')],
    'supplementary_data': ['SplmtryData']
}
