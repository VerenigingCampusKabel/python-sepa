from lxml import etree
from group_header import GroupHeader

def builder(instance):
    schema = instance.schema()

    # Create root element
    element = etree.Element(schema['tag'])

    # Loop over all schema children
    for key, value in schema['children'].iteritems():
        data = getattr(instance, key)
        if data is not None:
            # Check if the data can be an array according to the schema
            if isinstance(value, list):
                # Check if the data is actually an array
                if isinstance(data, list):
                    for d in data:
                        etree.SubElement(element, value[0]).text = d
                else:
                    etree.SubElement(element, value[0]).text = data
            # Else it's a plain element
            else:
                etree.SubElement(element, value).text = data

    return element

def xml_to_string(xml):
    return etree.tostring(xml)

header = GroupHeader(message_id='123456', creation_datetime='now', instructing_party='MyVCK', authorisation=['test1', 'test2'])

print(xml_to_string(builder(header)))
