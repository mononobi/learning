# -*- coding: utf-8 -*-
"""
I need an app to prepare sending materials then send it using EmailClient class:
- think of sending mode: show to select:
    single(s) to all provided targets (a) / s to s / a to s / s to multiple(m) / m to s / a to a
        show options to select/ multiple 2 m ??
- check EC's behavior and based on that read mail, senders and targets from files. use error handling for files.
- prepare message for each sending. REMOVE Ds. use server depending on sender
- ask Qs:
    - should this be done using OOP?
        - yes. define your ATTs or properties.
        - use access levels.
        - should program filenames be defined as ATTs?
        - should sender modes be in other subclasses?
    - some developments: on specific time.


Q: I had problem choosing which design to follow: ??
- use another class to write my app called EmailSender: I didn't choose this because it would be multiple 
    instantiations and inter object calls maybe?
- use an extension of Emailclient: I didn't choose this because there is no other version to this class by Mono.
- modifying this EmailClient: I use this because it would be simpler than extension.
"""

from homeworks.intermediate.h6_email.settings import SERVERS


class EmailClient:
    """Prepares and sends messages from files using EmailClient class."""

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

        self._sending_mode = '1'  # 1 means from single sender to single target.
        self._targets = []
        self._senders = []
        self._mail_content = ''
        self.prepared_messages = []
        self._selected_senders = []
        self._selected_targets = []

    def _get_server(self, sender_address):
        if not sender_address:
            raise ValueError('Invalid sender address.')

        parts = sender_address.split('@')
        if len(parts) != 2:
            raise ValueError(f'Invalid sender address [{sender_address}]')

        # Q: not better to raise error silently??

        server = parts[1]
        if not server:
            raise ValueError(f'Invalid sender address [{sender_address}]')

        config = SERVERS.get(server)
        if not config:
            raise ValueError(f'There is no configuration defined for [{server}]')

        return config

    def read_targets(self):
        try:
            with open('files/targets.txt') as targets_file:
                content_lines = targets_file.readlines()
        except FileNotFoundError:
            print('Targets file not found.')
        # Remove duplicate targets:
        content_lines = sorted(list(set(content_lines)))
        self._targets = []
        for line in content_lines:
            self._targets.append(line.split('[***]'))
        # targets emails as list of lists:
        return self._targets

    def read_senders(self):
        try:
            with open('files/senders.txt') as senders_file:
                content_lines = senders_file.readlines()
        except FileNotFoundError:
            print('Senders file not found.')
        # Remove duplicate senders:
        content_lines = sorted(list(set(content_lines)))
        self._senders = []
        for line in content_lines:
            self._senders.append(line.split('[***]'))
        # targets emails as list of lists:
        return self._senders

    def read_mail(self):
        # Q: is it good? self._mail_content =''
        try:
            with open('files/mail.txt') as mail_file:
                self._mail_content = mail_file.read()
        except FileNotFoundError:
            print('Mail content file not found.')
        return self._mail_content

    def _select_sending_mode(self):
        print('*' * 150)
        repeat = True
        message = ('How do you want to send emails? Please select the number of your option '
                   '(i.e. 1 for single to single):\n'
                   '\t1. from a single sender to a single target.\n'
                   '\t2. from all available senders to all available targets in the files.\n')
        while repeat:
            self._sending_mode = input(message)
            if self._sending_mode == '1':
                repeat = False
                i = 1
                for email in self.read_senders():
                    print(i, email[0])
                    i += 1
                # Another repeat can be added:
                self._single_sender = input("Please choose the sender's email:")
                i = 1
                for email in self.read_targets():
                    print(i, email[0])
                    i += 1
                self._single_target = input("Please choose the target's email:")
            if self._sending_mode == '2':
                repeat = False
            # return self._sending_mode

    def _prepare_sending(self):
        """based on sending mode, prepares and passes the messages to send method as list of tuples."""

        # what is final sending material? list of tuple or others???

        if self._sending_mode == '1':
            self._selected_senders.append(self._senders[int(self._single_sender) - 1])
            self._selected_targets.append(self._targets[int(self._single_target) - 1])
        elif self._sending_mode == '2':
            self._selected_senders = self.read_senders()
            self._selected_targets = self.read_targets()

        self.number_of_mail = 0

        # Q: Is it better to assign senders and targets to a tuple and then loop through?
        for sender in self._selected_senders:
            for target in self._selected_targets:
                self.prepared_messages.append([])
                self.prepared_messages[self.number_of_mail].append(sender[0])
                self.prepared_messages[self.number_of_mail].append(sender[1])
                self.prepared_messages[self.number_of_mail].append(target[0])
                self.prepared_messages[self.number_of_mail].append('Invitation for conference')
                message = self._mail_content.replace('Title888', f'Dear {target[1]},')
                self.prepared_messages[self.number_of_mail].append(message)
                self.number_of_mail += 1

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

    def run_email_app(self):
        self._select_sending_mode()
        self._prepare_sending()
        for message in self.prepared_messages:
            message = tuple(message)
            self.send(*message)


sender = EmailClient()
# print(sender.read_targets())
# tar = ('sender_email_1@gmail.com', '123', 'tt', 'ss', 'mm')
# sender.send(*tar)
# sender.send('sender_email_1@gmail.com', '123', 'tt', 'ss', 'mm')
# sender._select_sending_mode()

sender.run_email_app()
