"""
I need an app to prepare sending materials then send it using EmailClient class.
In this second version, I use a given class called Email. I write another module for this,
consisting of some distinct classes to follow OOP paradigm.
- no sending mode
- check EC's behavior and based on that, read mail, senders and targets from files. use error handling for files.
- prepare message for each sending. REMOVE Ds.
- Qs:
   - should program filenames be defined as ATTs?

- use more dicts for direct access, instead of indexes.
- contents should be stored in __init__() because it won't be changed during the program.
- USE VALIDATION WHEREVER YOU DON'T KNOW DATA. EMPTY LINES, NON-EMAILS, INPUTS, ...
"""

from homeworks.intermediate.h6_email_2.client import EmailClient


class PathException(Exception):
    pass


class EmailExtractor:
    """some basic job in reading and processing email list from files."""

    def __init__(self, path):
        # validate path and show errors when needed.
        self._path = path
        # self._type = type
        self._content_lines = []
        self._noduplicate_content = []

    # Q: Which approach is better? using type and setter, or searching for keyword in path?
    # # Q: cant set setter without property?
    # @property
    # def path(self):
    #     return self._path
    #
    # # Q: I want to use the same _path, but in this setting I must use path. Is this wanting normal?
    # @path.setter
    # def path(self, value):
    #     if value in ('senders', 'targets'):
    #         self._path = value
    #     else:
    #         raise ValueError('Clarify the type of email file, by passing "senders" or "targets"')

    def read_file(self):
        """"returns the body of file path in list of lines."""
        with open(self._path) as file:
            self._content_lines = file.readlines()

        #return self._content_lines

    # Q: should I make EmailExtractor and ReadFile two separate classes?
    def get_emails(self):
        """Changes lines to a list of dictionaries for readability, Also Removes duplicate emails:"""
        # Q: is it ok to call between methods?
        self.read_file()
        added_emails = []
        for line in self._content_lines:
            split_line = dict()
            try:
                if 'target' in self._path:
                    split_line['email'], split_line['title'] = line.split('[***]')
                elif 'sender' in self._path:
                    split_line['email'], split_line['password'] = line.split('[***]')
                else:
                    raise PathException('Path not containing "target" or "sender" keyword?')
            except ValueError:
                print('At least one line not having valid email format.')
                continue

            if split_line['email'] not in added_emails:
                self._noduplicate_content.append(split_line)
                added_emails.append(split_line['email'])

        return self._noduplicate_content


class EmailBodyExtractor(EmailExtractor):
    """using Extractor class we concat lines as one string. cant replace Subject because Title is \
    a must change (I think), and Target should be replaced with distinct target name."""

    def __init__(self, path):
        super().__init__(path)
        self._email_body = ''
        self.mail_subject = 'Invitation to Conference'

    def prepare_body(self):
        super().read_file()
        self._email_body = ''.join(self._content_lines)
        self._email_body = self._email_body.format(Subject=self.mail_subject, Title='{Title}')

        #return self._email_body

    @property
    def email_body(self):
        return self._email_body


class Email:
    """Prepares and sends email, using EmailClient class and Extractor classes."""

    def __init__(self):
        pass
        # self.path = 'files/targets.txt'

    def send_email(self):
        try:
            targets = EmailExtractor('files/targets.txt')
            senders = EmailExtractor('files/senders.txt')
            mail_body = EmailBodyExtractor('files/mail.txt')
            # Q: is it better to use object's attribute instead of local assignment?
            targets_list = targets.get_emails()
            senders_list = senders.get_emails()
            mail_body.prepare_body()
            email1 = EmailClient()
            for sender in senders_list:
                for target in targets_list:
                    mail_title = target['title']
                    email1.send(sender['email'],
                                sender['password'],
                                target['email'],
                                mail_body.mail_subject,
                                mail_body.email_body.format(Title=mail_title))

        # Q: If we have multiple ValueErrors, how can we distinguish on catches?
        except FileNotFoundError:
            print("Please provide targets and senders files in the path.")
        except ValueError as error_msg:
            print(error_msg)
        except PathException as error_msg:
            print(error_msg)
        except KeyError as error_msg:
            print(error_msg)


email = Email()
email.send_email()
# targets = EmailExtractor('files/targets.txt')
# print(targets.get_emails())
# mail = EmailBodyExtractor('files/mail.txt')
# mail.prepare_email()
