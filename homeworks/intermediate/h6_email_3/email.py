"""
I need an app to prepare sending materials then send it using EmailClient class.
In this third version, I use a given class called Email. I write another module for this,
consisting of some distinct classes to follow OOP paradigm. features:
- no sending mode
- check EC's behavior and based on that, read mail, senders and targets from files. use error handling for files.
- prepare message for each sending. REMOVE Ds.
- use more dicts for direct access, instead of indexes.
- process is done __init__() if it won't be changed during the program. THIS IS UNDERLINED in this version.
- USE VALIDATION WHEREVER YOU DON'T KNOW DATA. EMPTY LINES, NON-EMAILS, INPUTS, ...
"""

from homeworks.intermediate.h6_email_3.client import EmailClient


class PathException(Exception):
    pass


class Extractor:
    """Some basic job in reading email list from file."""

    def __init__(self, path):
        # validate path and show errors when needed, using PathException
        self._path = path
        self._content_lines = []
        self.read_file()

    def read_file(self):
        """Returns the body of file path in list of lines."""
        with open(self._path) as file:
            self._content_lines = file.readlines()


class SendersExtractor(Extractor):
    """Using Extractor class it processes email list from file."""
    def __init__(self, path):
        super().__init__(path)
        # Q: Is it better to use super(SendersExtractor, self).__init__()??
        self._noduplicate_emails = []
        self.read_file()
        self.get_emails()

    def get_emails(self):
        """Changes lines to a list of dictionaries for readability, Also Removes duplicate emails:"""
        added_emails = []
        for line in self._content_lines:
            split_line = dict()
            try:
                split_line['email'], split_line['password'] = line.split('[***]')
            except ValueError:
                print('At least one line not having valid email format.')
                continue

            if split_line['email'] not in added_emails:
                self._noduplicate_emails.append(split_line)
                added_emails.append(split_line['email'])

    @property
    def noduplicate_emails(self):
        return self._noduplicate_emails


class TargetsExtractor(SendersExtractor):
    """It overrides SendersExtractor to change dict key from password to title to represent it provides target
    detail."""
    def get_emails(self):
        """Changes lines to a list of dictionaries for readability, Also Removes duplicate emails:"""
        added_emails = []
        for line in self._content_lines:
            split_line = dict()
            try:
                split_line['email'], split_line['title'] = line.split('[***]')
            except ValueError:
                print('At least one line not having valid email format.')
                continue

            if split_line['email'] not in added_emails:
                self._noduplicate_emails.append(split_line)
                added_emails.append(split_line['email'])


class EmailBodyExtractor(Extractor):
    """using Extractor class we concat lines as one string. cant replace Subject because Title is \
    a must change (I think), and Target should be replaced with distinct target name."""

    def __init__(self, path):
        super().__init__(path)
        self._email_body = ''
        self.mail_subject = self._content_lines[0]
        self.prepare_body()

    def prepare_body(self):
        self._email_body = ''.join(self._content_lines)
        self._email_body = self._email_body.format(Subject=self.mail_subject, Title='Dear {Title}')

    @property
    def email_body(self):
        return self._email_body


class Email:
    """Prepares and sends email, using EmailClient class and Extractor classes."""

    def __init__(self):
        try:
            self.senders = SendersExtractor('files/senders.txt')
            self.targets = TargetsExtractor('files/targets.txt')
            self.mail_body = EmailBodyExtractor('files/mail.txt')
            self.send_email()
        except FileNotFoundError:
            print("Please provide targets and senders files in the path.")
        except (ValueError, PathException, KeyError) as error_msg:
            print(error_msg)

    def send_email(self):
        try:
            # Q: is it better to use object's attribute instead of local assignment?
            email1 = EmailClient()
            for sender in self.senders.noduplicate_emails:
                for target in self.targets.noduplicate_emails:
                    email1.send(sender['email'],
                                sender['password'],
                                target['email'],
                                self.mail_body.mail_subject,
                                self.mail_body.email_body.format(Title=target['title']))

        # Q: If we have multiple ValueErrors, how can we distinguish on catches?
        except (ValueError, PathException, KeyError) as error_msg:
            print(error_msg)


email = Email()

