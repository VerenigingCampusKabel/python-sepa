import os
from lxml import etree

customer_credit_transfer_initiation = 'pain.001.001.08.xsd'
customer_payment_status_report = 'pain.002.001.08.xsd'
customer_payment_reversal = 'pain.007.001.07.xsd'
customer_direct_debit_initiation = 'pain.008.001.07.xsd'
mandate_initation_request = 'pain.009.001.05.xsd'
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
