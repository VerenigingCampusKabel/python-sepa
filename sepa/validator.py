import os
from lxml import etree

bank_to_customer_account_report = 'camt.052.001.06.xsd'
bank_to_customer_statement = 'camt.053.001.06.xsd'
bank_to_customer_debit_credit_notification = 'camt.054.001.06.xsd'
account_reporting_request = 'camt.060.001.03.xsd'

customer_credit_transfer_initiation = 'pain.001.001.08.xsd'
customer_payment_status_report = 'pain.002.001.08.xsd'
customer_payment_reversal = 'pain.007.001.07.xsd'
customer_direct_debit_initiation = 'pain.008.001.07.xsd'
mandate_initiation_request = 'pain.009.001.05.xsd'
mandate_amendment_request = 'pain.010.001.05.xsd'
mandate_cancellation_request = 'pain.011.001.05.xsd'
mandate_acceptance_report = 'pain.012.001.05.xsd'
mandate_copy_request = 'pain.017.001.01.xsd'
mandate_suspension_request = 'pain.018.001.01.xsd'

def get_schema(schema_name):
    return etree.XMLSchema(etree.parse(os.path.join(os.path.dirname(__file__), 'schemas', schema_name)))

def validate(schema_name, tree):
    return get_schema(schema_name).validate(tree)

def validate_or_error(schema_name, tree):
    return get_schema(schema_name).assertValid(tree)
