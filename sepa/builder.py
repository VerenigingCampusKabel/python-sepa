from lxml import etree
from .messages import mandate_initation_request, mandate_amendment_request, mandate_cancellation_request

def build_child(structure, data):
    if isinstance(structure, dict):
        return build_tree(structure, data)
    else:
        tag = etree.Element(structure)
        tag.text = data
        return tag

def build_tree(structure, data):
    tag = etree.Element(structure['_self'])

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

    return tag

def build(structure, data, document=True):
    tree = build_tree(structure, data)
    root = etree.Element('Document', nsmap=structure['_namespaces'])
    root.append(tree)
    return root

def build_string(structure, data, document=True):
    return etree.tostring(build(structure, data, document))
