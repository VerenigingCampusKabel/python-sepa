from .general import code_or_proprietary, address, party, account, agent

def payment_group_header(tag):
    return {
        '_self': tag,
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
        'priority': 'InstrPrty',
        'service_level': code_or_proprietary('SvcLvl'),
        'local_instrument': code_or_proprietary('LclInstrm'),
        'sequence_type': 'SeqTp',
        'category_purpose': code_or_proprietary('CtgyPurp')
    }

def transaction(tag):
    return {
        '_self': tag,
        'id': {
            '_self': 'PmtId',
            'instruction': 'InstrId',
            'end_to_end': 'EndToEndId'
        },
        'type': type_information('PmtTpInf'),
        'amount': 'InstdAmt', # TODO: deal with currency attribute
        'charge_bearer': 'ChrgsBr',
        'transaction': {
            '_self': 'DrctDbtTx',
            'mandate': {
                '_self': 'MndtRltdInf',
                'id': 'MndtId',
                'date': 'DtOfSgntr',
                'amendment_indicator': 'AmdmntInd',
                'amendment': {
                    '_self': 'AmdmntInfDtls'
                },
                'signature': 'ElctmcSgntr',
                'first_collection': 'FrstColltnDt',
                'final_collection': 'FnlColltnDt',
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
            'indicator': 'DbtCdtRptgInd',
            'authority': {
                '_self': 'Authrty',
                'name': 'Nm',
                'country': 'Ctry'
            },
            'details': {
                '_self': 'Dtls',
                'type': 'Tp',
                'date': 'Dt',
                'country': 'Ctry',
                'code': 'Cd',
                'amount': 'Amt',
                'information': ['Inf']
            }
        }],
        'tax': {
            '_self': 'Tax'
            # TODO: tax object
        },
        'related_remittance_information': [{
            '_self': 'RltdRmtInf',
            'id': 'RmtId',
            'location': [{
                '_self': 'RmtLctnDtls',
                'method': 'Mtd',
                'electronic_address': 'ElctrncAdr',
                'postal_address': {
                    '_self': 'PstlAdr',
                    'name': 'Nm',
                    'address': address('Adr')
                }
            }]
        }],
        'remittance_information': {
            '_self': 'RmtInf',
            'unstructured': 'Ustrd',
            'structured': {
                '_self': 'Strd',
                # TODO: structured remittance information object,
                'additional_information': ['AddtlRmtInf']
            }
        }
    }

def payment(tag):
    return {
        '_self': tag,
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
        'charge_bearer': 'ChrgsBr',
        'charges_account': account('ChrgsAcct'),
        'charges_account_agent': agent('ChrgsAcctAgt'),
        'creditor_scheme_identification': party('CdtrSchmeId'),
        'transactions': [transaction('DrctDbtTxInf')],
        'supplementary_data': ['SplmtryData']
    }
