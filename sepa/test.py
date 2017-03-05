from lxml import etree

from messages import mandate_initation_request
from builder import build

data_in = {
    'group_header': {
        'message_id': '1234567890',
        'creation_date_time': '2017-03-05 13:45',
        'authorisation': {
            'code': 'test123'
        }
    },
    'mandate': [{
        'id': '78904536',
        'request_id': '9823701',
        'authentication': {
            'date': '2017-03-05',
            'channel': {
                'code': 'ABC'
            }
        }
    }]
}

data_out = build(mandate_initation_request, data_in)
print(etree.tostring(data_out))
