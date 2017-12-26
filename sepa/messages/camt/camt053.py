from sepa.definitions.statement import statement_group_header, statement

# CAMT.053.001.06 - Bank To Customer Statement v6
standard = 'camt.053.001.06'
name = 'bank_to_customer_statement'
definition = {
    '_namespaces': {
        None: 'urn:iso:std:iso:20022:tech:xsd:camt.053.001.06',
        'xs': 'http://www.w3.org/2001/XMLSchema'
    },
    '_self': 'BkToCstmrStmt',
    '_sorting': ['GrpHdr', 'Stmt', 'SplmtryData'],
    'group_header': statement_group_header('GrpHdr'),
    'statements': [statement('Stmt')],
    'supplementary_data': ['SplmtryData']
}
