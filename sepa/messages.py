class MandateInitiationRequest:
    def __init__(self, group_header, mandate, supplementary_data=None):
        self.group_header = group_header
        self.mandate = mandate
        self.supplementary_data = supplementary_data

    def schema(self):
        return {
            'tag': 'MndtInitnReq',
            'children': [
                'group_header',
                'mandate',
                [ 'supplementary_data', 'SplmtryData']
            ]
        }
