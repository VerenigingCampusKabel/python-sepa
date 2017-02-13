from lxml import etree
from group_header import GroupHeader

header = GroupHeader(message_id='123456', creation_datetime='now', instructing_party='MyVCK')

# doc = etree.ElementTree(header.build())

print(etree.tostring(header.build()))
