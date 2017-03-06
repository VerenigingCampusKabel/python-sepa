from lxml import etree
from .messages import mandate_initation_request as mir, mandate_amendment_request as mar, mandate_cancellation_request as mcr

def reverse(structure, name = ''):
    new_structure = {
        '_self': name
    }

    for child in structure:
        if child != '_self':
            sub = structure[child]

            if isinstance(sub, list):
                if isinstance(sub[0], dict):
                    new_structure[sub[0]['_self']] = [reverse(sub[0], child)]
                else:
                    new_structure[sub[0]] = [child]
            elif isinstance(sub, dict):
                # if '_self' in sub:
                new_structure[sub['_self']] = reverse(sub, child)
                # else:
                    # print('WEIRD WEIRD', child, sub)
            else:
                new_structure[sub] = child

    return new_structure

# Reverse message structures
mandate_initation_request = reverse(mir)
mandate_amendment_request = reverse(mar)
mandate_cancellation_request = reverse(mcr)

def parse(structure, tag):
    data = {}

    for child in tag:
        substructure = structure[child.tag]

        if isinstance(substructure, list):
            # print(substructure[0])
            if isinstance(substructure[0], dict):
                key = substructure[0]['_self']
                value = parse(substructure[0], child)
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
