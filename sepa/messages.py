from general import code_or_proprietary, group_header, party
from mandate import mandate

def original_message(tag):
    return {
        '_self': tag,
        'message_id': 'MsgId',
        'message_name_id': 'MsgNmId',
        'creation_date_time': 'CreDtTm'
    }

mandate_initation_request = {
    '_self': 'MndtInitnReq',
    'group_header': group_header('GrpHdr'),
    'mandate': [mandate('Mndt')],
    'supplementary_data': ['SplmtryData']
}

mandate_amendment_request = {
    '_self': 'MndtAmdmntReq',
    'group_header': group_header('GrpHdr'),
    'amendment': [{
        '_self': 'UndrlygAmdmntDtls',
        'original_message': original_message('OrgnlMsgInf'),
        'reason': {
            '_self': 'AmdmntRsn',
            'originator': party('Orgtr'),
            'reason': code_or_proprietary('Rsn'),
            'additional_information': ['AddtInf']
        },
        'mandate': mandate('Mndt'),
        'original_mandate': {
            'id': 'OrgnlMndtId',
            'mandate': mandate(' OrgnMndt')
        },
        'supplementary_data': ['SplmtryData']
    }],
    'supplementary_data': ['SplmtryData']
}

mandate_cancellation_request = {
    '_self': 'MndtCxlReq',
    'group_header': group_header('GrpHdr'),
    'cancellatiion': [{
        '_self': 'UndrlygCxlDtls',
        'original_message': original_message('OrgnlMsgInf'),
        'reason': {
            '_self': 'CxlRsn',
            'originator': party('Orgtr'),
            'reason': code_or_proprietary('Rsn'),
            'additional_information': ['AddtInf']
        },
        'original_mandate': {
            'id': 'OrgnlMndtId',
            'mandate': mandate(' OrgnMndt')
        },
        'supplementary_data': ['SplmtryData']
    }],
    'supplementary_data': ['SplmtryData']
}
