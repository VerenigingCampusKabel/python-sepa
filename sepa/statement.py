from .general import code_or_proprietary, address, party, account, agent

def pagination(tag):
    return {
        '_self': tag,
        '_sorting': ['PgNb', 'LastPgInd'],
        'page': 'PgNb',
        'last_page_indicator': 'LastPgInd'
    }

def statement_group_header(tag):
    return {
        '_self': tag,
        '_sorting': ['MsgId', 'CreDtTm', 'MsgRcpt', 'MsgPgntn', 'OrgnlBizQry'],
        'message_id': 'MsgId',
        'creation_date_time': 'CreDtTm',
        'message_recipient': party('MsgRcpt'),
        'message_pagination': pagination('MsgPgntn'),
        'original_business_query': {
            '_self': 'OrgnlBizQry',
            '_sorting': ['MsgId', 'MsgNmId', 'CreDtTm'],
            'message_id': 'MsgId',
            'message_name_id': 'MsgNmId',
            'creation_date_time': 'CreDtTm'
        }
    }

def from_to_date(tag):
    return {
        '_self': tag,
        '_sorting': ['FrDtTm', 'ToDtTm'],
        'from': 'FrDtTm',
        'to': 'ToDtTm'
    }

def entry(tag):
    return {
        '_self': tag,
        '_sorting': [
            'NtryRef', 'Amt', 'CdtDbtInd', 'RvslInd', 'Sts', 'BookgDt', 'ValDt', 'AcctSvcrRef', 'Avlbty', 'BkTxCd', 'ComssnWvrInd', 'AddtlInfInd', 'AmtDtls',
            'Chrgs', 'TechInptChanl', 'Intrst', 'CardTx', 'NtryDtls', 'AddtlNtryInf'
        ],
        'reference': 'NtryRef',
        'amount': 'Amt',
        # TODO
        'additional_information': ['AddtlNtryInf']
    }

def statement(tag):
    return {
        '_self': tag,
        '_sorting': [
            'Id', 'StmtPgntn', 'ElctrncSeqNb', 'LglSeqNb', 'CreDtTm', 'FrToDt', 'CpyDplctInd', 'RptgSrc', 'Acct', 'RltdAcct', 'Intrst', 'Bal', 'TxsSummry',
            'Ntry', 'AddtlStmtInf'
        ],
        'id': 'Id',
        'pagination': pagination('StmtPgntn'),
        'electronic_sequence_number': 'ElctrncSeqNb',
        'legal_sequence_number': 'LglSeqNb',
        'creation_date_time': 'CreDtTm',
        'from_to_date': from_to_date('FrToDt'),
        'copy_duplicate_indicator': 'CpyDplctInd',
        'reporting_source': code_or_proprietary('RptgSrc'),
        'account': account('Acct'),
        'related_account': account('RltdAcct'),
        'interest': [{
            '_self': 'Intrst',
            '_sorting': ['Tp', 'Rate', 'FrToDt', 'Rsn', 'Tax'],
            'type': code_or_proprietary('Tp'),
            'rate': [{
                '_self': 'Rate',
                '_sorting': ['Tp', 'VldtyRg'],
                'type': {
                    '_self': 'Tp',
                    '_sorting': ['Pctg', 'Othr'],
                    'percentage': 'Pctg',
                    'other': 'Othr'
                },
                'validity': {
                    '_self': 'VldtyRg',
                    '_sorting': ['Amt', 'CdtDbtInd', 'Ccy'],
                    'amount': 'Amt',
                    'credit_debit_indicator': 'CdtDbtInd',
                    'currency': 'Ccy'
                }
            }],
            'from_to_date': from_to_date('FrToDt'),
            'reason': 'Rsn',
            'tax': {
                '_self': 'Tax',
                '_sorting': ['Id', 'Rate', 'Amt'],
                'id': 'Id',
                'rate': 'Rate',
                'amount': 'Amt'
            }
        }],
        'balance': [{
            '_self': 'Bal',
            '_sorting': ['Tp', 'CdtLine', 'Amt', 'CdtDbtInd', 'Dt', 'Avlbty'],
            'type': {
                '_self': 'Tp',
                '_sorting': ['CdOrPrtry', 'SubTp'],
                'code_or_proprietary': code_or_proprietary('CdOrPrtry'),
                'sub_type': code_or_proprietary('SubTp')
            },
            'credit_line': {
                '_self': 'CdtLine',
                '_sorting': ['Incl', 'Amt'],
                'included': 'Incl',
                'amount': 'Amt'
            },
            'amount': 'Amt',
            'credit_debit_indicator': 'CdtDbtInd',
            'date': {
                '_self': 'Dt',
                '_sorting': ['Dt', 'DtTm'],
                'date': 'Dt',
                'date_time': 'DtTm'
            },
            'availability': [{
                '_self': 'Avlbty',
                '_sorting': ['Dt', 'Amt', 'CdtDbtInd'],
                'date': {
                    '_self': 'Dt',
                    '_sorting': ['NbOfDays', 'ActlDt'],
                    'number_of_days': 'NbOfDays',
                    'actual_date': 'ActlDt'
                },
                'amount': 'Amt',
                'credit_debit_indicator': 'CdtDbtInd'
            }]
        }],
        'transactions_summary': {
            '_self': 'TxsSummry',
            '_sorting': []
        },
        'entries': [entry('Ntry')],
        'additional_information': ['AddtlStmtInf']
    }
