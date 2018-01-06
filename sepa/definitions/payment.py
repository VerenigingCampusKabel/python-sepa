from .general import code_or_proprietary, amount_field, address, party, account, agent

def payment_group_header(tag):
    return {
        '_self': tag,
        '_sorting': ['MsgId', 'CreDtTm', 'Authstn', 'NbOfTxs', 'CtrlSum', 'InitgPty', 'FwdgAgt'],
        'message_id': 'MsgId',
        'creation_date_time': 'CreDtTm',
        'authorisation': code_or_proprietary('Authstn'),
        'transaction_count': 'NbOfTxs',
        'control_sum': 'CtrlSum',
        'initiating_party': party('InitgPty'),
        'forwarding_agent': agent('FwdgAgt')
    }

def type_information(tag):
    return {
        '_self': tag,
        '_sorting': ['InstrPrty', 'ClrChanl', 'SvcLvl', 'LclInstrm', 'SeqTp', 'CtgyPurp'],
        'priority': 'InstrPrty',
        'clearing_channel': 'ClrChanl',
        'service_level': code_or_proprietary('SvcLvl'),
        'local_instrument': code_or_proprietary('LclInstrm'),
        'sequence_type': 'SeqTp',
        'category_purpose': code_or_proprietary('CtgyPurp')
    }

def transaction(tag):
    return {
        '_self': tag,
        '_sorting': [
            'PmtId', 'PmtTpInf', 'InstdAmt', 'ChrgBr', 'DrctDbtTx', 'UltmtCdtr', 'DbtrAgt', 'DbtrAgtAcct', 'Dbtr', 'DbtrAcct', 'UltmtDbtr', 'InstrForCdtrAgt',
            'Purp', 'RgltryRptg', 'Tax', 'RltdRmtInf', 'RmtInf'
        ],
        'id': {
            '_self': 'PmtId',
            '_sorting': ['InstrId', 'EndToEndId'],
            'instruction': 'InstrId',
            'end_to_end': 'EndToEndId'
        },
        'type': type_information('PmtTpInf'),
        'amount': amount_field('InstdAmt'),
        'charge_bearer': 'ChrgsBr',
        'transaction': {
            '_self': 'DrctDbtTx',
            '_sorting': ['MndtRltdInf', 'CdtrSchmeId', 'PreNtfctnId', 'PreNtfctnDt'],
            'mandate': {
                '_self': 'MndtRltdInf',
                '_sorting': ['MndtId', 'DtOfSgntr', 'AmdmntInd', 'AmdmntInfDtls', 'ElctmcSgntr', 'FrstColltnDt', 'FnlColltnDt', 'Frqcy', 'Rsn', 'TrckgDays'],
                'id': 'MndtId',
                'date': 'DtOfSgntr',
                'amendment_indicator': 'AmdmntInd',
                'amendment': {
                    '_self': 'AmdmntInfDtls',
                    '_sorting': None
                    # TODO: amendment
                },
                'signature': 'ElctmcSgntr',
                'first_collection': 'FrstColltnDt',
                'final_collection': 'FnlColltnDt',
                'frequency': {
                    '_self': 'Frqcy',
                    '_sorting': ['Tp', 'Prd', 'PtInTm'],
                    'type': 'Tp',
                    'period': {
                        '_self': 'Prd',
                        '_sorting': ['Tp', 'CntPerPrd'],
                        'type': 'Tp',
                        'count': 'CntPerPrd'
                    },
                    'point': {
                        '_self': 'PtInTm',
                        '_sorting': ['Tp', 'PtInTm'],
                        'type': 'Tp',
                        'point': 'PtInTm'
                    }
                },
                'reason': code_or_proprietary('Rsn'),
                'tracking_days': 'TrckgDays'
            },
            'creditor_scheme_identification': party('CdtrSchmeId'),
            'pre_notification_id': 'PreNtfctnId',
            'pre_notification_date': 'PreNtfctnDt'
        },
        'ultimate_creditor': party('UltmtCdtr'),
        'debtor': party('Dbtr'),
        'debtor_account': account('DbtrAcct'),
        'debtor_agent': agent('DbtrAgt'),
        'debtor_agent_account': account('DbtrAgtAcct'),
        'ultimate_debtor': party('UltmtDbtr'),
        'instruction_for_creditor_agent': 'InstrForCdtrAgt',
        'purpose': code_or_proprietary('Purp'),
        'regulatory_reporting': [{
            '_self': 'RgltryRptg',
            '_sorting': ['DbtCdtRptgInd', 'Authrty', 'Dtls'],
            'indicator': 'DbtCdtRptgInd',
            'authority': {
                '_self': 'Authrty',
                '_sorting': ['Nm', 'Ctry'],
                'name': 'Nm',
                'country': 'Ctry'
            },
            'details': {
                '_self': 'Dtls',
                '_sorting': ['Tp', 'Dt', 'Ctry', 'Cd', 'Amt', 'Inf'],
                'type': 'Tp',
                'date': 'Dt',
                'country': 'Ctry',
                'code': 'Cd',
                'amount': 'Amt',
                'information': ['Inf']
            }
        }],
        'tax': {
            '_self': 'Tax',
            '_sorting': None
            # TODO: tax object
        },
        'related_remittance_information': [{
            '_self': 'RltdRmtInf',
            '_sorting': ['RmtId', 'RmtLctnDtls', 'ElctrncAdr', 'PstlAdr'],
            'id': 'RmtId',
            'location': [{
                '_self': 'RmtLctnDtls',
                '_sorting': ['Mtd', 'ElctrncAdr', 'PstlAdr'],
                'method': 'Mtd',
                'electronic_address': 'ElctrncAdr',
                'postal_address': {
                    '_self': 'PstlAdr',
                    '_sorting': ['Nm', 'Adr'],
                    'name': 'Nm',
                    'address': address('Adr')
                }
            }]
        }],
        'remittance_information': {
            '_self': 'RmtInf',
            '_sorting': ['Ustrd', 'Strd'],
            'unstructured': 'Ustrd',
            'structured': {
                '_self': 'Strd',
                '_sorting': ['AddtlRmtInf'],
                # TODO: structured remittance information object,
                'additional_information': ['AddtlRmtInf']
            }
        }
    }

def payment(tag):
    return {
        '_self': tag,
        '_sorting': [
            'PmtInfId', 'PmtMtd', 'BtchBookg', 'NbOfTxs', 'CtrlSum', 'PmtTpInf', 'ReqdColltnDt', 'Cdtr', 'CdtrAcct', 'CdtrAgt', 'CdtrAgtAcct', 'UltmtCdtr',
            'ChrgBr', 'ChrgsAcct', 'ChrgsAcctAgt', 'CdtrSchmeId', 'DrctDbtTxInf', 'SplmtryData'
        ],
        'id': 'PmtInfId',
        'method': 'PmtMtd',
        'batch_booking': 'BtchBookg',
        'transaction_count': 'NbOfTxs',
        'control_sum': 'CtrlSum',
        'type': type_information('PmtTpInf'),
        'collection_date': 'ReqdColltnDt',
        'creditor': party('Cdtr'),
        'creditor_account': account('CdtrAcct'),
        'creditor_agent': agent('CdtrAgt'),
        'creditor_agent_account': account('CdtrAgtAcct'),
        'ultimate_creditor': party('UltmtCdtr'),
        'charge_bearer': 'ChrgBr',
        'charges_account': account('ChrgsAcct'),
        'charges_account_agent': agent('ChrgsAcctAgt'),
        'creditor_scheme_identification': party('CdtrSchmeId'),
        'transactions': [transaction('DrctDbtTxInf')],
        'supplementary_data': ['SplmtryData']
    }
