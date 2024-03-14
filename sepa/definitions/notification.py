from .general import code_or_proprietary, amount_field, address, party, account, agent, charges
from .statement import pagination, from_to_date, interest_record, transactions_summary, entry

def notification(tag):
    return {
        '_self': tag,
        '_sorting': [
            'Id', 'NtfctnPgntn', 'ElctrncSeqNb', 'LglSeqNb', 'CreDtTm', 'FrToDt', 'CpyDplctInd', 'RptgSrc', 'Acct', 'RltdAcct', 'Intrst', 'TxsSummry',
            'Ntry', 'AddtlNtfctnInf'
        ],
        'id': 'Id',
        'pagination': pagination('NtfctnPgntn'),
        'electronic_sequence_number': 'ElctrncSeqNb',
        'legal_sequence_number': 'LglSeqNb',
        'creation_date_time': 'CreDtTm',
        'from_to_date': from_to_date('FrToDt'),
        'copy_duplicate_indicator': 'CpyDplctInd',
        'reporting_source': code_or_proprietary('RptgSrc'),
        'account': account('Acct'),
        'related_account': account('RltdAcct'),
        'interest': [interest_record('Intrst')],
        'transactions_summary': transactions_summary('TxsSummry'),
        'entries': [entry('Ntry')],
        'additional_information': ['AddtlNtfctnInf']
    }
