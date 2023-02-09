# -*- coding: utf-8 -*-

"""
There is an email client class named `EmailClient` which can send email using
different email providers (it's a fake email client and does not actually send
any emails).

implement an app which have the following features using the mentioned `EmailClient`:

1. Read email senders from a file named `senders.txt`.
2. Read email targets from a file named `targets.txt`.
3. Read email subject and body from a file named `mail.txt`.
4. Read different email server configs from a file named `settings.py`.
5. Sending emails from single/multiple senders to single/multiple targets.
6. Adding support for any email provider just by adding its respective
   configs into `settings.py`.
7. Sending emails from senders with different email providers in a single operation.
8. Automatically removing duplicate senders or targets.

**NOTE**

- you should read about file operations to find out how to read files.
- your code should be implemented using object-oriented design.
- the template of `senders.txt`, `targets.txt` and `mail.txt` files are
  clarified inside each of them.
"""
