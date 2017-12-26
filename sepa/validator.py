import os
from lxml import etree
from .messages import sepa_messages

# Export validator message types
for group_name, group in sepa_messages.items():
    for name, message in group.items():
        schema_name = message.standard + '.xsd'
        globals()[name] = schema_name
        globals()[message.name] = schema_name

def get_schema(schema_name):
    return etree.XMLSchema(etree.parse(os.path.join(os.path.dirname(__file__), 'schemas', schema_name)))

def validate(schema_name, tree):
    return get_schema(schema_name).validate(tree)

def validate_or_error(schema_name, tree):
    return get_schema(schema_name).assertValid(tree)
