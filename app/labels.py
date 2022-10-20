BUTTON_LABELS = {
    'status': '/status',
    'switch': '/switch',
    'help': '/help'
}

RESPONSE_TEXT = {
    'help': \
        '/switch - there are two available translation modes: ' \
        'synchronous translation (*sync*) and selective (*selective*). '\
        'Selective mode translates messages if they are marked by {0} '\
        'in any place in the text. '\
        'Synchronous translation translates all messages.\n'\
        '/status - show current state of variables\n'\
        '/help - show help message',
    'status': 'Translation mode: *{mode}*',
    'switch': 'Translation mode changed to *{mode}*',
    'translated': '🤖: {text}'
}
