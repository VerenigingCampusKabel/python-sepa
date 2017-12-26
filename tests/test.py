import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from lxml import etree
from sepa import builder, parser, validator, signer
from .util import xml_compare

data_object = {
    'group_header': {
        'message_id': '1234567890',
        'creation_date_time': '2017-03-05T13:45:00',
        'authorisation': {
            'code': 'ILEV'
        }
    },
    'mandate': [{
        'id': '78904536',
        'request_id': '9823701',
        'authentication': [{
            'date': '2017-03-05',
            'channel': {
                'code': 'ABC'
            }
        }]
    }]
}

data_xml = ('<MndtInitnReq>'
    '<Mndt>'
        '<Authntcn>'
            '<Dt>2017-03-05</Dt>'
            '<Chanl>'
                '<Cd>ABC</Cd>'
            '</Chanl>'
        '</Authntcn>'
        '<MndtId>78904536</MndtId>'
        '<MndtReqId>9823701</MndtReqId>'
    '</Mndt>'
    '<GrpHdr>'
        '<CreDtTm>2017-03-05T13:45:00</CreDtTm>'
        '<Authstn>'
            '<Cd>ILEV</Cd>'
        '</Authstn>'
        '<MsgId>1234567890</MsgId>'
    '</GrpHdr>'
'</MndtInitnReq>')

class TestSuite(unittest.TestSuite):
    def test_builder(self):
        # Build XML
        data_out = builder.build(builder.mandate_initiation_request, data_object, document=False)

        # Compare generated data to expected output
        assert xml_compare(data_out, etree.fromstring(data_xml))

    def test_validator(self):
        # Build XML
        data_out = builder.build(builder.mandate_initiation_request, data_object)

        # TODO: remove debug print
        print(etree.tostring(data_out))

        # TODO: uncomment this
        # Validate using XML Schema Definition (XSD)
        assert not validator.validate_or_error(validator.mandate_initiation_request, data_out)

    def test_signer(self):
        # Build XML
        data_out = builder.build(builder.mandate_initiation_request, data_object)

        # Sign XML
        with open(os.path.join(os.path.dirname(__file__), 'privkey.pem'), 'rb') as f:
            key = f.read()
        with open(os.path.join(os.path.dirname(__file__), 'cert.pem'), 'rb') as f:
            cert = f.read()
        data_signed = signer.sign(data_out, key=key, cert=cert)

        # TODO: remove debug print
        print(etree.tostring(data_signed))

        # TODO: uncomment this
        # Verify XML
        # assert signer.verify(data_signed)

    def test_parser(self):
        # Parse XML
        data_out = parser.parse(parser.mandate_initiation_request, etree.fromstring(data_xml))

        # Compare generated data to expected output
        assert data_out == data_object

if __name__ == '__main__':
    unittest.main()
