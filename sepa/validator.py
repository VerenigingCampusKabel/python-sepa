import os
from lxml import etree

mandate_initation_request = 'pain.009.001.05.xsd'
mandate_amendment_request = 'pain.010.001.05.xsd'
mandate_cancellation_request = 'pain.011.001.05.xsd'

def get_schema(schema_name):
    return etree.XMLSchema(etree.parse(os.path.join(os.path.dirname(__file__), 'schemas', schema_name)))

def validate(schema_name, tree):
    return get_schema(schema_name).validate(tree)

def validate_or_error(schema_name, tree):
    return get_schema(schema_name).assertValid(tree)
