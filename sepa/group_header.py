from lxml import etree

class GroupHeader:
    def __init__(self, message_id, creation_datetime, authorisation = None, initiating_party = None, instructing_party = None, instructed_party = None):
        self.message_id = message_id
        self.creation_datetime = creation_datetime
        self.authorisation = authorisation
        self.initiating_party = initiating_party
        self.instructing_party = instructing_party
        self.instructed_party = instructed_party

    def build(self):
        header = etree.Element('GrpHdr')
        etree.SubElement(header, 'MsgId').text = self.message_id
        etree.SubElement(header, 'CreDtTm').text = self.creation_datetime

        if self.authorisation is not None:
            if isinstance(self.authorisation, []):
                for element in self.authorisation:
                    etree.SubElement(header, 'Authstn').text = element
            else:
                etree.SubElement(header, 'Authstn').text = self.authorisation

        if self.initiating_party is not None:
            etree.SubElement(header, 'InitgPty').text = self.initiating_party

        if self.instructing_party is not None:
            etree.SubElement(header, 'InstgAgt').text = self.instructing_party

        if self.instructed_party is not None:
            etree.SubElement(header, 'InstdAgt').text = self.instructed_party

        return header
