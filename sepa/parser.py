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
        if child.tag not in structure:
            print('Unknown tag: "' + child.tag + '", parent: "' + tag + '"')
        else:
            substructure = structure[child.tag]

            if isinstance(substructure, list):
                # print(substructure[0])
                if isinstance(substructure[0], dict):
                    key = substructure[0]['_self']
                    value = parse_tree(substructure[0], child)
                else:
                    # print('NOPENOPENOPE', type(substructure[0]))
                    key = substructure[0]
                    value = child.text

                # print(child.tag, key)
                if not key in data:
                    data[key] = []
                data[key].append(value)
            elif isinstance(substructure, dict):
                data[substructure['_self']] = parse(substructure, child)
            else:
                data[substructure] = child.text

    return data

def parse(structure, tree):
    if tree.tag == 'Document':
        return parse_tree(structure, tree[0])
    return parse_tree(structure, tree)

def parse_string(structure, tree, **kwargs):
    return parse(structure, etree.fromstring(tree, **kwargs))
