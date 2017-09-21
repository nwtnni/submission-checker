import smtplib
from os import environ
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class Mailer:

    EMAIL = environ['EMAIL']
    PASSWORD = environ['PASSWORD']

    def __init__(self):
        self.server = smtplib.SMTP('smtp.gmail.com', 587)
        self.server.starttls()
        self.server.login(Mailer.EMAIL, Mailer.PASSWORD)

    def send(self, to_add, subject, body):
        msg = MIMEMultipart()
        msg['From'] = Mailer.EMAIL
        msg['To'] = to_add
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))  
        self.server.sendmail(Mailer.EMAIL, to_add, msg.as_string())

    def quit(self):
        self.server.quit()
