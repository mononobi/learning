# -*- coding: utf-8 -*-

from homeworks.intermediate.h6_email.settings import SERVERS


class EmailClient:
    def __init__(self):
        for item, value in SERVERS.items():
            if not item:
                raise KeyError('Some servers do not have valid url.')

            if not value:
                raise KeyError(f'Server [{item}] does not have a valid configuration.')

            if not value.get('host'):
                raise KeyError(f'Server [{item}] does not have a valid host.')

            if not value.get('port'):
                raise KeyError(f'Server [{item}] does not have a valid port.')

    def _get_server(self, sender_address):
        if not sender_address:
            raise ValueError('Invalid sender address.')

        parts = sender_address.split('@')
        if len(parts) != 2:
            raise ValueError(f'Invalid sender address [{sender_address}]')

        server = parts[1]
        if not server:
            raise ValueError(f'Invalid sender address [{sender_address}]')

        config = SERVERS.get(server)
        if not config:
            raise ValueError(f'There is no configuration defined for [{server}]')

        return config

    def send(self, sender_address, sender_password, target_address, subject, message):
        if not sender_password:
            raise ValueError(f'Invalid sender password for [{sender_address}].')

        server = self._get_server(sender_address)
        msg = {}
        msg['Subject'] = subject
        msg['Message'] = message
        msg['From'] = sender_address
        msg['To'] = target_address
        print('*' * 150)
        print('Email Sent: ', msg)
        print('Server Used: ', server)
