import logging

from lxml import etree
from .messages import sepa_messages

def reverse(structure, name = ''):
    new_structure = {
        '_self': name
    }

    for child in structure:
        if not child.startswith('_'):
            sub = structure[child]

            if isinstance(sub, list):
                if isinstance(sub[0], dict):
                    new_structure[sub[0]['_self']] = [reverse(sub[0], child)]
                else:
                    new_structure[sub[0]] = [child]
            elif isinstance(sub, dict):
                new_structure[sub['_self']] = reverse(sub, child)
            else:
                new_structure[sub] = child
        elif child != '_self':
            new_structure[child] = structure[child]

    return new_structure

# Export parser message types
for group_name, group in sepa_messages.items():
    for name, message in group.items():
        reverse_definition = reverse(message.definition)
        globals()[name] = reverse_definition
        globals()[message.name] = reverse_definition

def parse_tree(structure, tag):
    data = {}

    for child in tag:
        child.tag = etree.QName(child).localname
        if child.tag not in structure:
            logging.debug('Unknown tag: "' + child.tag + '", parent: "' + tag.tag + '"')
        else:
            substructure = structure[child.tag]

            if isinstance(substructure, list):
                if isinstance(substructure[0], dict):
                    key = substructure[0]['_self']
                    value = parse_tree(substructure[0], child)
                else:
                    key = substructure[0]
                    value = child.text

                if key not in data:
                    data[key] = []
                data[key].append(value)
            elif isinstance(substructure, dict):
                data[substructure['_self']] = parse(substructure, child)

                if '_nochildren' in substructure and substructure['_nochildren']:
                     data[substructure['_self']]['_value'] = child.text

                     if '_attribs' in substructure:
                         for attrib_key, attrib_value in substructure['_attribs'].items():
                             if attrib_value in child.attrib:
                                 data[substructure['_self']][attrib_key] = child.attrib[attrib_value]
            else:
                data[substructure] = child.text

    return data

class UnsupportedDocumentType(Exception):
    pass

def get_structure(tree):
    """Returns the correct data structure for the document type found in the xmlns attribute."""
    doctype = tree.tag
    if etree.QName(tree).localname == "Document":
        #e.g. urn:iso:std:iso:20022:tech:xsd:camt.054.001.04
        xmlns = etree.QName(tree).namespace.split(':')
        #e.g. camt.054.001.04
        doctype = xmlns[-1]
        for group_name, group in sepa_messages.items():
            for name, message in group.items():
                if doctype == message.standard or doctype in getattr(message,'compatible_standards',[]):
                    return globals()[message.name]
    raise UnsupportedDocumentType(doctype)

def parse(structure, tree):
    if not structure:
        structure = get_structure(tree)
    if etree.QName(tree).localname == 'Document':
        data = parse_tree(structure, tree[0])
        data['document_type'] = etree.QName(tree).namespace.split(':')[-1]
        return data
    return parse_tree(structure, tree)

def parse_string(structure, tree, **kwargs):
    return parse(structure, etree.fromstring(tree, **kwargs))
