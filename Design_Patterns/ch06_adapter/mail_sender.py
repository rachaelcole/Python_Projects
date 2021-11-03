# A simple email-sending script that reads recipients from a .csv file
import csv
import smtplib
from email.mime.text import MIMEText
from logger import Logger


# Email sender
class Mailer(object):
    def send(sender, subject, message, *recipients):
        msg = MIMEText(message)
        msg['Subject'] = subject
        msg['From'] = sender
        msg['To'] = recipients
        mail_sender = smtplib.SMTP('localhost')
        mail_sender.send_message(recipients)
        mail_sender.quit()

# AdapterObject type class
class LoggerAdapter(object):
    def __init__(self, what_i_have):
        self.what_i_have = what_i_have
    def send(self, sender, subject, message, *recipients):
        log_message = f"From: {sender}\nTo: {recipients}\nSubject: {subject}\nMessage: {message}"
        self.what_i_have.output(log_message)
    def __getattr__(self, attr):
        return getattr(self.what_i_have, attr)

# Separating the retrieval of user information into its own class
class UserFetcher(object):
    def __init__(self, source):
        self.source = source
    def fetch_users(self):
        with open(self.source, 'r') as csv_file:
            reader = csv.DictReader(csv_file)
            users = [row for row in reader]
        return users


if __name__ == "__main__":
    
    user_fetcher = UserFetcher('users.csv')

    mailer = Mailer()
    mailer.send(
        'me@example.com',
        "This is your message subject", 
        "Have a good day",
        [user['email'] for user in user_fetcher.fetch_users()]
    )




# Reference: 
# Badenhurst, Wessel. "Chapter 6: Adapter Pattern". Practical Python Design Patterns: Pythonic Solutions to Common Problems, Apress, October 20, 2017, pp. 91-103,
# DOI: https://doi.org/10.1007/978-1-4842-2680-3_6.