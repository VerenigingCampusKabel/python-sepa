from .general import code_or_proprietary, amount_field, address, party, account, agent

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

def date_or_date_time(tag):
    return {
        '_self': tag,
        '_sorting': ['Dt', 'DtTm'],
        'date': 'Dt',
        'date_time': 'DtTm'
    }

def availability(tag):
    return {
        '_self': tag,
        '_sorting': ['Dt', 'Amt', 'CdtDbtInd'],
        'date': {
            '_self': 'Dt',
            '_sorting': ['NbOfDays', 'ActlDt'],
            'number_of_days': 'NbOfDays',
            'actual_date': 'ActlDt'
        },
        'amount': amount_field('Amt'),
        'credit_debit_indicator': 'CdtDbtInd'
    }

def bank_transaction_code(tag):
    return {
        '_self': tag,
        '_sorting': ['Domn', 'Prtry'],
        'domain': {
            '_self': 'Domn',
            '_sorting': ['Cd', 'Fmly'],
            'code': 'Cd',
            'family': {
                '_self': 'Fmly',
                '_sorting': ['Cd', 'SubFmlyCd'],
                'code': 'Cd',
                'sub_family_code': 'SubFmlyCd'
            }
        },
        'proprietary': {
            '_self': 'Prtry',
            '_sorting': ['Cd', 'Issr'],
            'code': 'Cd',
            'issuer': 'Issr'
        }
    }

def amount(tag):
    return {
        '_self': tag,
        '_sorting': ['Tp', 'Amt', 'CccyXchg'],
        'type': 'Tp',
        'amount': amount_field('Amt'),
        'currency_exchange': {
            '_self': 'CccyXchg',
            '_sorting': ['SrcCcy', 'TrgtCcy', 'UnitCcy', 'XchgRate', 'CtrctId', 'QtnDt'],
            'source': 'SrcCcy',
            'target': 'TrgtCcy',
            'unit': 'UnitCcy',
            'exchange_rate': 'XchgRate',
            'contract_id': 'CtrctId',
            'quotation_date': 'QtnDt'
        }
    }

def amount_details(tag):
    return {
        '_self': tag,
        '_sorting': ['InstdAmt', 'TxAmt', 'CntrValAmt', 'AnncdPstngAmt', 'PrtryAmt'],
        'instructed_amount': amount('InstdAmt'),
        'transaction_amount': amount('TxAmt'),
        'counter_value_amount': amount('CntrValAmt'),
        'announced_posting_amount': amount('AnncdPstngAmt'),
        'proprietary_amount': amount('PrtryAmt')
    }

def interest_record(tag):
    return {
        '_self': tag,
        '_sorting': ['Amt', 'CdtDbtInd', 'Tp', 'Rate', 'FrToDt', 'Rsn', 'Tax'],
        'amount': amount_field('Amt'),
        'credit_debit_indicator': 'CdtDbtInd',
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
                'amount': amount_field('Amt'),
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
            'amount': amount_field('Amt')
        }
    }

def entry(tag):
    return {
        '_self': tag,
        '_sorting': [
            'NtryRef', 'Amt', 'CdtDbtInd', 'RvslInd', 'Sts', 'BookgDt', 'ValDt', 'AcctSvcrRef', 'Avlbty', 'BkTxCd', 'ComssnWvrInd', 'AddtlInfInd', 'AmtDtls',
            'Chrgs', 'TechInptChanl', 'Intrst', 'CardTx', 'NtryDtls', 'AddtlNtryInf'
        ],
        'reference': 'NtryRef',
        'amount': amount_field('Amt'),
        'credit_debit_indicator': 'CdtDbtInd',
        'reversal_indicator': 'RvslInd',
        'status': 'Sts',
        'booking_date': date_or_date_time('BookgDt'),
        'value_date': date_or_date_time('ValDt'),
        'account_servicer_reference': 'AcctSvcrRef',
        'availability': [availability('Avlbty')],
        'bank_transaction_code': bank_transaction_code('BkTxCd'),
        'commission_waiver_indicator': 'ComssnWvrInd',
        'additional_information_indicator': {
            '_self': 'AddtlInfInd',
            '_sorting': ['MsgNmId', 'MsgId'],
            'message_name_id': 'MsgNmId',
            'message_id': 'MsgId'
        },
        'amount_details': amount_details('AmtDtls'),
        'charges': {
            '_self': 'Chrgs',
            '_sorting': ['TtlChrgsAndTaxAmt', 'Rcrd'],
            'total': 'TtlChrgsAndTaxAmt',
            'record': [{
                '_self': 'Rcrd',
                '_sorting': []
                # TODO
            }]
        },
        'technical_input_channel': code_or_proprietary('TechInptChanl'),
        'interest': {
            '_self': 'Intrst',
            '_sorting': ['TtlIntrstAndTaxAmt', 'Rcrd'],
            'total': 'TtlIntrstAndTaxAmt',
            'records': [interest_record('Rcrd')]
        },
        'card_transaction': {
            '_self': 'CardTx',
            '_sorting': []
            # TODO
        },
        'entry_details': [{
            '_self': 'NtryDtls',
            '_sorting': ['Btch', 'TxDtls'],
            'batch': {
                '_self': 'Btch',
                '_sorting': ['MsgId', 'PmtInfId', 'NbOfTxs', 'TtlAmt', 'CdtDbtInd'],
                'message_id': 'MsgId',
                'payment_information_id': 'PmtInfId',
                'number_of_transactions': 'NbOfTxs',
                'total_amount': amount_field('TtlAmt'),
                'credit_debit_indicator': 'CdtDbtInd'
            },
            'transaction_details': [{
                '_self': 'TxDtls',
                '_sorting': [
                    'Refs', 'Amt', 'CdtDbtInd', 'AmtDtls', 'Avlbty', 'BkTxCd', 'Chrgs', 'Intrst', 'RltdPties', 'RltdAgts', 'Purp', 'RltdRmtInf', 'RmtInf',
                    'RltdDts', 'RltdPric', 'RltdQties', 'FinInstrmId', 'Tax', 'RtrInf', 'CorpActn', 'SfkpgAcct', 'CshDpst', 'CardTx', 'AddtTxInf',
                    'SplmtryData'
                ],
                'refs': {
                    '_self': 'Refs',
                    '_sorting': [
                        'MsgId', 'AcctSvcrRef', 'PmtInfId', 'InstrId', 'EndToEndId', 'TxId', 'MndtId', 'ChqNb', 'ClrSysRef', 'AcctOwnrTxId', 'AcctSvcrTxId',
                        'MktInfrstrctrTxId', 'PrcgId', 'Prty'
                    ],
                    'message_id': 'MsgId',
                    'account_servicer_reference': 'AcctSvcrRef',
                    'payment_information_id': 'PmtInfId',
                    'instruction_id': 'InstrId',
                    'end_to_end_id': 'EndToEndId',
                    'transaction_id': 'TxId',
                    'mandate_id': 'MndtId',
                    'cheque_number': 'ChqNb',
                    'clearing_system_reference': 'ClrSysRef',
                    'account_owner_transaction_id': 'AcctOwnrTxId',
                    'account_servicer_transaction_id': 'AcctSvcrTxId',
                    'market_infrastructure_transaction_id': 'MktInfrstrctrTxId',
                    'processing_id': 'PrcgId',
                    'proprietary': {
                        '_self': 'Prtry',
                        '_sorting': ['Tp', 'Ref'],
                        'type': 'Tp',
                        'reference': 'Ref'
                    }
                },
                'amount': amount_field('Amt'),
                'credit_debit_indicator': 'CdtDbtInd',
                'amount_details': amount_details('AmtDtls'),
                'availability': [availability('Avlbty')],
                'bank_transaction_code': bank_transaction_code('BkTxCd'),
                'charges': {
                    '_self': 'Chrgs',
                    '_sorting': ['TtlChrgsAndTaxAmt', 'Rcrd'],
                    'total': 'TtlChrgsAndTaxAmt',
                    'records': [{
                        '_self': 'Rcrd',
                        '_sorting': []
                        # TODO
                    }]
                },
                'interest': {
                    '_self': 'Intrst',
                    '_sorting': ['TtlIntrstAndTaxAmt', 'Rcrd'],
                    'total': amount_field('TtlIntrstAndTaxAmt'),
                    'records': [interest_record('Rcrd')]
                },
                'related_parties': {
                    '_self': 'RltdPties',
                    '_sorting': ['InitgPty', 'Dbtr', 'DbtrAcct', 'UltmtDbtr', 'Cdtr', 'CdtrAcct', 'UltmtCdtr', 'TradgPty', 'Prtry'],
                    'initiating_party': party('InitgPty'),
                    'debtor': party('Dbtr'),
                    'debtor_account': account('DbtrAcct'),
                    'ultimate_debtor': party('UltmtDbtr'),
                    'creditor': party('Cdtr'),
                    'creditor_account': account('CdtrAcct'),
                    'ultimate_creditor': party('UltmtCdtr'),
                    'trading_party': party('TradgPty'),
                    'proprietary': [{
                        '_self': 'Prtry',
                        '_sorting': ['Tp', 'Pty'],
                        'type': 'Tp',
                        'party': party('Pty')
                    }]
                },
                'related_agents': {
                    '_self': 'RltdAgts',
                    '_sorting': ['DbtrAgt', 'CdtrAgt', 'IntrmyAgt1', 'IntrmyAgt2', 'IntrmyAgt3', 'RcvgAgt', 'DlvrgAgt', 'IssgAgt', 'SttlmPlc', 'Prtry'],
                    'debtor_agent': agent('DbtrAgt'),
                    'creditor_agent': agent('CdtrAgt'),
                    'intermediary_agent1': agent('IntrmyAgt1'),
                    'intermediary_agent2': agent('IntrmyAgt2'),
                    'intermediary_agent3': agent('IntrmyAgt3'),
                    'receiving_agent': agent('RcvgAgt'),
                    'delivering_dagent': agent('DlvrgAgt'),
                    'issuing_agent': agent('IssgAgt'),
                    'settlement_place': agent('SttlmPlc'),
                    'proprietary': [{
                        '_self': 'Prtry',
                        '_sorting': ['Tp', 'Agt'],
                        'type': 'Tp',
                        'agent': agent('Agt')
                    }]
                },
                'purpose': code_or_proprietary('Purp'),
                'related_remittance_information': [{
                    '_self': 'RltdRmtInf',
                    '_sorting': ['RmtId', 'RmtLctnDtls'],
                    'remittance_id': 'RmtId',
                    'remittance_location_details': {
                        '_self': 'RmtLctnDtls',
                        '_sorting': ['Mtd', 'ElctrncAdr', 'PsltAdr'],
                        'method': 'Mtd',
                        'electronic_address': 'ElctrncAdr',
                        'postal_address': {
                            '_self': 'PsltAdr',
                            '_sorting': ['Nm', 'Adr'],
                            'name': 'Nm',
                            'address': address('Adr')
                        }
                    }
                }],
                'remittance_information': {
                    '_self': 'RmtInf',
                    '_sorting': ['Ustrd', 'Strd'],
                    'unstructured': ['Ustrd'],
                    'structured': [{
                        '_self': 'Strd',
                        '_sorting': []
                        # TODO
                    }]
                },
                'related_dates': {
                    '_self': 'RltdDts',
                    '_sorting': ['AccptncDtTm', 'TradActvtyCtrctlSttlmDt', 'TradDt', 'IntrBkSttlmDt', 'StartDt', 'EndDt', 'TxDtTm', 'Prtry'],
                    'acceptance_date_time': 'AccptncDtTm',
                    'trade_activity_contractual_settlement_date': 'TradActvtyCtrctlSttlmDt',
                    'trade_date': 'TradDt',
                    'interbank_settlement_date': 'IntrBkSttlmDt',
                    'start_date': 'StartDt',
                    'end_date': 'EndDt',
                    'transaction_datetime': 'TxDtTm',
                    'proprietary': {
                        '_self': 'Prtry',
                        '_sorting': ['Tp', 'Dt'],
                        'type': 'Tp',
                        'date': date_or_date_time('Dt')
                    }
                },
                'related_price': {
                    '_self': 'RltdPric',
                    '_sorting': ['DealPric', 'Prtry'],
                    'deal_price': {
                        '_self': 'DealPric',
                        '_sorting': ['Tp', 'Val'],
                        'type': {
                            '_self': 'Tp',
                            '_sorting': ['Yldd', 'ValTp'],
                            'yielded': 'Yldd',
                            'value_type': 'ValTp'
                        },
                        'value': {
                            '_self': 'Val',
                            '_sorting': ['Rate', 'Amt'],
                            'rate': 'Rate',
                            'amount': amount_field('Amt')
                        }
                    },
                    'proprietary': {
                        '_self': 'Prtry',
                        '_sorting': ['Tp', 'Pric'],
                        'type': 'Tp',
                        'price': 'Pric'
                    }
                },
                'related_quantities': [{
                    '_self': 'RltdQties',
                    '_sorting': [],
                    # TODO
                }],
                'financial_instrument_id': {
                    '_self': 'FinInstrmId',
                    '_sorting': [],
                    # TODO
                },
                'tax': {
                    '_self': 'Tax',
                    '_sorting': [],
                    # TODO
                },
                'return_information': {
                    '_self': 'RtrInf',
                    '_sorting': ['OrgnlBkTxCd', 'Orgtr', 'Rsn', 'AddtInf'],
                    'original_bank_transaction_code': bank_transaction_code('OrgnlBkTxCd'),
                    'originator': party('Orgtr'),
                    'reason': code_or_proprietary('Rsn'),
                    'additional_information': ['AddtInf']
                },
                'coporate_action': {
                    '_self': 'CorpActn',
                    '_sorting': [],
                    # TODO
                },
                'safekeeping_account': {
                    '_self': 'SfkpgAcct',
                    '_sorting': [],
                    # TODO
                },
                'cash_deposit': [{
                    '_self': 'CshDpst',
                    '_sorting': [],
                    # TODO
                }],
                'cash_transaction': {
                    '_self': 'CardTx',
                    '_sorting': [],
                    # TODO
                },
                'additional_information': 'AddtTxInf',
                'supplementary_data': ['SplmtryData']
            }]
        }],
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
        'interest': [interest_record('Intrst')],
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
                'amount': amount_field('Amt')
            },
            'amount': amount_field('Amt'),
            'credit_debit_indicator': 'CdtDbtInd',
            'date': date_or_date_time('Dt'),
            'availability': [availability('Avlbty')]
        }],
        'transactions_summary': {
            '_self': 'TxsSummry',
            '_sorting': ['TtlNtries', 'TtlCdtNtries', 'TtlDbtNtries', 'TtlNtriesPerBkTxCd'],
            'total_entries': {
                '_self': 'TtlNtries',
                '_sorting': ['NbOfNtries', 'Sum', 'TtlNetNtry'],
                'number_of_entries': 'NbOfNtries',
                'sum': 'Sum',
                'total_net_entry': {
                    '_self': 'TtlNetNtry',
                    '_sorting': ['Amt', 'CdtDbtInd'],
                    'amount': amount_field('Amt'),
                    'credit_debit_indicator': 'CdtDbtInd'
                }
            },
            'total_credit_entries': {
                '_self': 'TtlCdtNtries',
                '_sorting': ['NbOfNtries', 'Sum'],
                'number_of_entries': 'NbOfNtries',
                'sum': 'Sum'
            },
            'total_debit_entries': {
                '_self': 'TtlDbtNtries',
                '_sorting': ['NbOfNtries', 'Sum'],
                'number_of_entries': 'NbOfNtries',
                'sum': 'Sum'
            },
            'total_entries_per_bank_transaction_code': {
                '_self': 'TtlNtriesPerBkTxCd',
                '_sorting': ['NbOfNtries', 'Sum', 'TtlNetNtry', 'FcstInd', 'BkTxCd', 'Avlbty'],
                'number_of_entries': 'NbOfNtries',
                'sum': 'Sum',
                'total_net_entry': {
                    '_self': 'TtlNetNtry',
                    '_sorting': ['Amt', 'CdtDbtInd'],
                    'amount': amount_field('Amt'),
                    'credit_debit_indicator': 'CdtDbtInd'
                },
                'forecast_indicator': 'FcstInd',
                'bank_transaction_code': 'BkTxCd',
                'availability': availability('Avlbty')
            }
        },
        'entries': [entry('Ntry')],
        'additional_information': ['AddtlStmtInf']
    }
