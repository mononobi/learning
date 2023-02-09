# -*- coding: utf-8 -*-

# smtp with tls remote servers.
# the host and port values could be fake:

_GOOGLE = {
    'host': 'smtp.gmail.com',
    'port': 587
}

_YAHOO = {
    'host': 'smtp.mail.yahoo.com',
    'port': 587
}

# you should add each email provider you want to support in this variable.
# the key of each entry should be the url after the `@` in email address:

SERVERS = {
    'gmail.com': _GOOGLE,
    'yahoo.com': _YAHOO,
    'ymail.com': _YAHOO
}

# separator between email and name or password in senders and targets files:

SEP = '[***]'
