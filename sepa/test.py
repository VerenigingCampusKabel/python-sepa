from lxml import etree
from group_header import GroupHeader
from mandate import Mandate

def single(element, schema, data):
    # Check if it's a subschema
    if isinstance(schema, dict):
        element.appened(build(data, schema))
    else:
        etree.SubElement(element, schema).text = data

def multiple(element, schema, data):
    # Check if the data actually is a list
    if isinstance(data, list):
        for d in data:
            single(element, schema, d)
    else:
        single(element, schema, data)

def build(schema, instance):
    # Create root element
    element = etree.Element(schema['tag'])

    # Loop over all schema children
    for key, value in schema['children'].iteritems():
        data = getattr(instance, key)
        if data is not None:
            # Check if the schema allows lists
            if isinstance(value, list):
                multiple(element, value[0], data)
            else:
                single(element, value, data)

    return element

def builder(instance):
    return build(instance.schema(), instance)

def xml_to_string(xml):
    return etree.tostring(xml)

header = GroupHeader(message_id='123456', creation_datetime='now', instructing_party='MyVCK', authorisation=['test1', 'test2'])
mandate = Mandate(request_identification='req', tracking_indicator='track', creditor='me', debtor='not me', debtor_agent='some agent')

print(xml_to_string(builder(header)))
print(xml_to_string(builder(mandate)))
