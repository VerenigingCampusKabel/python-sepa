from lxml import etree
from .messages import\
    customer_direct_debit_initiation,\
    mandate_initiation_request,\
    mandate_amendment_request,\
    mandate_cancellation_request

def build_child(structure, data):
    if isinstance(structure, dict):
        return build_tree(structure, data)
    else:
        tag = etree.Element(structure)
        tag.text = data
        return tag

def build_tree(structure, data):
    tag = etree.Element(structure['_self'])

    # Add tag attributes
    if '_attribs' in structure:
        if isinstance(data, dict) and '_attribs' in data:
            for key, value in data['_attribs'].items():
                tag.attrib[structure['_attribs'][key]] = value

    # Skip adding children if it's a text element
    if '_nochildren' in structure:
        tag.text = data['_value'] if '_value' in data else ''
        return tag

    for child in structure:
        if not child.startswith('_') and child in data:
            subdata = data[child]

            if isinstance(structure[child], list):
                if isinstance(subdata, list):
                    for d in subdata:
                        tag.append(build_child(structure[child][0], d))
                else:
                    tag.append(build_child(structure[child][0], subdata))
            else:
                tag.append(build_child(structure[child], subdata))

    # Sort the child elements
    if '_sorting' in structure:
        tag[:] = sorted(tag, key=lambda element: structure['_sorting'].index(element.tag))

    return tag

def build(structure, data, document=True):
    tree = build_tree(structure, data)
    if document:
        root = etree.Element('Document', nsmap=structure['_namespaces'])
        root.append(tree)
        return root
    return tree

def build_string(structure, data, document=True, **kwargs):
    return etree.tostring(build(structure, data, document), **kwargs)
