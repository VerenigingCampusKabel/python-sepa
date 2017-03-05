from lxml import etree

def build_child(structure, data):
    if isinstance(structure, dict):
        return build(structure, data)
    else:
        tag = etree.Element(structure)
        tag.text = data
        return tag


def build(structure, data):
    tag = etree.Element(structure['_self'])

    for child in structure:
        if child != '_self' and child in data:
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
