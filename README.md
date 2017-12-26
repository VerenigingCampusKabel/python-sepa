# Python SEPA library

Python library for parsing and building SEPA Direct Debit and SEPA eMandate schemas.

The ultimate goal of this library is to support all [ISO 20022 Payments messages](https://www.iso20022.org/payments_messages.page), however in practice SEPA only uses a subset of these messages.

## Supported messages
- Cash Management (CAMT)
  - [ ] Bank To Customer Account Report v6 (camt.052.001.06)
  - [ ] Bank To Customer Statement v6 (camt.053.001.06)
  - [ ] Bank To Customer Debit Credit Notification v6 (camt.054.001.06)
  - [ ] Account Reporting Request v3 (camt.060.001.03)
- Payments Initiation (PAIN)
  - [ ] Customer Credit Transfer Initiation v8 (pain.001.001.08)
  - [ ] Customer Payment Status Report v8 (pain.002.001.08)
  - [ ] Customer Payment Reversal v7 (pain.007.001.07)
  - [x] Customer Direct Debit Initiation v7 (pain.008.001.07)
  - [x] Mandate Initiation Request v5 (pain.009.001.05)
  - [x] Mandate Amendment Request v5 (pain.010.001.05)
  - [x] Mandate Cancellation Request v5 (pain.011.001.05)
  - [ ] Mandate Acceptance Report v5 (pain.012.001.05)
  - [ ] Creditor Payment Activation Request v6 (pain.013.001.06)
  - [ ] Creditor Payment Activation Request Status Report v6 (pain.014.001.06)
  - [ ] Mandate Copy Request v1 (pain.017.001.01)
  - [ ] Mandate Suspension Request v1 (pain.018.001.01)

## Usage
### Building messages
```python
from sepa import builder

data_in = {
    'group_header': {},
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

# Returns an lxml etree object
data_out = builder.build(builder.mandate_initiation_request, data_in)

# Returns a byte string
str_data_out = builder.build_string(builder.mandate_initiation_request, data_in)
print(str_data_out)
```

### Parsing messages
```python
from sepa import parser

data_in = ('<MndtInitnReq>'
    '<GrpHdr></GrpHdr>'
    '<Mndt>'
        '<MndtId>78904536</MndtdId>'
        '<MndtReqId>9823701</MndtReqId>'
        '<Authntcn>'
            '<Dt>2017-03-05</Dt>'
            '<Chanl><Cd>ABC</Cd></Chanl>'
        '</Authntcn>'
    '</Mndt>'
'</MndtInitnReq>')

data_out = parser.parse_string(parser.mandate_initiation_request, data_in)
print(data_out)
```

### Verifying messages
*This feature is still work in progress.*

### Signing messages
*This feature is still work in progress.*
