from lxml import etree
from util import code_or_proprietary

class Mandate:
    def __init__(self, request_identification, tracking_indicator, creditor, debtor, debtor_agent, identification = None, authentication = None, type = None,
        occurrences = None, first_collection_amount = None, collection_amount = None, maximum_amount = None, adjustment = None, reason = None,
        creditor_scheme_identification = None, creditor_account = None, creditor_agent = None, ultimate_creditor = None,
        debtor_account = None, ultimate_debtor = None, reference = None, referred_document = None, supplementary_data = None):
        self.identification = identification
        self.request_identification = request_identification
        self.authentication = authentication
        self.type = type
        self.occurrences = occurrences
        self.tracking_indicator = tracking_indicator
        self.first_collection_amount = first_collection_amount
        self.collection_amount = collection_amount
        self.maximum_amount = maximum_amount
        self.adjustment = adjustment
        self.reason = reason
        self.creditor_scheme_identification = creditor_scheme_identification
        self.creditor = creditor
        self.creditor_account = creditor_account
        self.creditor_agent = creditor_agent
        self.ultimate_creditor = ultimate_creditor
        self.debtor = debtor
        self.debtor_account = debtor_account
        self.debtor_agent = debtor_agent
        self.ultimate_debtor = ultimate_debtor
        self.reference = reference
        self.referred_document = referred_document
        self.supplementary_data = supplementary_data

    def schema(self):
        return {
            'tag': 'Mndt',
            'children': {
                'identification': ['MndtId'],
                'request_identification': 'MndtReqId',
                'authentication': {
                    'tag': 'Authntcn',
                    'children': {
                        'message_code': 'MsgAuthntcnCd',
                        'date': 'Dt',
                        'channel': code_or_proprietary('Chanl')
                    }
                },
                'type': {
                    'tag': 'Tp',
                    'children': {
                        'service_level': code_or_proprietary('SvcLvl'),
                        'local_instrument': code_or_proprietary('LclInstm'),
                        'category_purpose': code_or_proprietary('CtgyPurp'),
                        'classification': code_or_proprietary('Clssfctn'),
                    }
                },
                'occurrences': {
                    'tag': 'Ocrncs',
                    'children': {
                        'sequence_type': 'SeqTp',
                        'frequency': 'Frqcy',
                        'duration': 'Drtn',
                        'first_collection': 'FrstColltnDt',
                        'final_collection': 'FnlColltnDt',
                    }
                },
                'tracking_indicator': 'TrckgInd',
                'first_collection_amount': 'FrstColltnAmt',
                'collection_amount': 'ColltnAmt',
                'maximum_amount': 'MaxAmt',
                'adjustment': {
                    'tag': 'Adjstmnt',
                    'children': {
                        'date_rule_indicator': 'DtAdjstmntRuleInd',
                        'category': 'Ctgy',
                        'amount': 'Amt',
                        'rate': 'Rate'
                    }
                },
                'reason':  code_or_proprietary('Rsn'),
                'creditor_scheme_identification': 'CdtrSchmeId',
                'creditor': 'Cdtr',
                'creditor_account': 'CdtrAcct',
                'creditor_agent': 'CdtrAgt',
                'ultimate_creditor': 'UltmtCdtr',
                'debtor': 'Dbtr',
                'debtor_account': 'DbtrAcct',
                'debtor_agent': 'DbtrAgt',
                'ultimate_debtor': 'UltmtDbtr',
                'reference': 'MndtRef',
                'referred_document': [{
                    'tag': 'RfrdDoc',
                    'children': {
                        'type': {
                            'tag': 'Tp',
                            'children': {
                                'data':  code_or_proprietary('CdOrPrtry'),
                                'issuer': 'Issr'
                            }
                        },
                        'number': 'Nb',
                        'creditor_reference': 'CdtrRef',
                        'related_date': 'RldtDt'
                    }
                }],
                'supplementary_data': ['SplmtryData']
            }
        }
