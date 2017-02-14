class GroupHeader:
    def __init__(self, message_id, creation_datetime, authorisation = None, initiating_party = None, instructing_party = None, instructed_party = None):
        self.message_id = message_id
        self.creation_datetime = creation_datetime
        self.authorisation = authorisation
        self.initiating_party = initiating_party
        self.instructing_party = instructing_party
        self.instructed_party = instructed_party

    def schema(self):
        return {
            'tag': 'GrpHdr',
            'children': {
                'message_id': 'MsgId',
                'creation_datetime': 'CreDtTm',
                'authorisation': ['Authstn'],
                'initiating_party': 'InitgPty',
                'instructing_party': 'InstgAgt',
                'instructed_party': 'InstdAgt'
            }
        }
