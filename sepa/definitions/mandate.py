from .general import code_or_proprietary, party, account, agent

def mandate_group_header(tag):
    return {
        '_self': tag,
        '_sorting': ['MsgId', 'CreDtTm', 'Authstn', 'InitgPty', 'InstgAgt', 'InstdAgt'],
        'message_id': 'MsgId',
        'creation_date_time': 'CreDtTm',
        'authorisation': code_or_proprietary('Authstn'),
        'initiating_party': party('InitgPty'),
        'instructing_agent': agent('InstgAgt'),
        'instructed_agent': agent('InstdAgt')
    }

def original_message(tag):
    return {
        '_self': tag,
        '_sorting': ['MsgId', 'MsgNmId', 'CreDtTm'],
        'message_id': 'MsgId',
        'message_name_id': 'MsgNmId',
        'creation_date_time': 'CreDtTm'
    }

def mandate(tag):
    return {
        '_self': tag,
        'id': 'MndtId',
        'request_id': 'MndtReqId',
        'authentication': [{
            '_self': 'Authntcn',
            'date': 'Dt',
            'channel': code_or_proprietary('Chanl')
        }],
        'type': {
            '_self': 'Tp',
            'service_level': code_or_proprietary('SvcLvl'),
            'local_instrument': code_or_proprietary('LclInstrm'),
            'category_purpose': code_or_proprietary('CtgyPurp'),
            'classification': code_or_proprietary('Clssfctn'),
        },
        'occurrences': {
            '_self': 'Ocrncs',
            'sequence_type': 'SeqTp',
            'frequency': {
                '_self': 'Frqcy',
                'type': 'Tp',
                'period': {
                    '_self': 'Prd',
                    'type': 'Tp',
                    'count': 'CntPerPrd'
                },
                'point': {
                    '_self': 'PtInTm',
                    'type': 'Tp',
                    'point': 'PtInTm'
                }
            },
            'duration': {
                '_self': 'Drtn',
                'from': 'FrDt',
                'to': 'ToDt'
            },
            'first_collection': 'FrstColltnDt',
            'final_collection': 'FnlColltnDt'
        },
        'tracking_indicator': 'TrckgInd',
        'first_collection_amount': 'FrstColltnAmnt',
        'collection_amount': 'ColltnAmt',
        'maximum_amount': 'MaxAmt',
        'adjustment': {
            '_self': 'Adjstmnt',
            'rule_indicator': 'DtAdjstmntRuleInd',
            'category': code_or_proprietary('Ctgy'),
            'amount': 'Amt',
            'rate': 'Rate'
        },
        'reason': code_or_proprietary('Rsn'),
        'creditor_scheme_identification': party('CdtrSchmeId'),
        'creditor': party('Cdtr'),
        'creditor_account': account('CdtrAcct'),
        'creditor_agent': agent('CdtrAgt'),
        'ultimate_creditor': party('UltmtCdtr'),
        'debtor': party('Dbtr'),
        'debtor_account': account('DbtrAcct'),
        'debtor_agent': agent('DbtrAgt'),
        'ultimate_debtor': party('UltmtDbtr'),
        'reference': 'MndtRef',
        'referred_document': {
            '_self': 'RfrdDoc',
            'type': {
                '_self': 'Tp',
                'code_or_proprietary': code_or_proprietary('CdOrPrtry'),
                'issuer': 'Issr'
            },
            'number': 'Nb',
            'creditor_reference': 'CdtrRef',
            'related_date': 'RltdDt'
        },
        'supplementary_data': ['SplmtryData']
    }
