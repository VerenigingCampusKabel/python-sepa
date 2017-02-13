from os import path
from mako.lookup import TemplateLookup

templates = TemplateLookup(directories=['templates'], strict_undefined=True)
template = templates.get_template('mandate_initiation_request.xml');

data = {
    'message_id': 123,
    'creation_datetime': 'somedate',
    'authorisation': [
        'test1',
        'test2'
    ],
    'instructing_party': 'MyVCK',
    'mandates': []
}

print(template.render(**data))
