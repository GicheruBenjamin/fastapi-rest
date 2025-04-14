



'''
Email functions
'''

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from email.utils import parseaddr, formataddr
import os
import configparser

def send_email(to, subject, text, files=None):
    # Load config
    config = configparser.ConfigParser()
    config.read('config.ini')
    
    # Setup email data
    sender = config['EMAIL']['SENDER']
    password = config['EMAIL']['PASSWORD']
    smtp_server = config['EMAIL']['SMTP_SERVER']
    port = config['EMAIL']['PORT']
    message = MIMEMultipart()
    message['From'] = sender
    message['To'] = to
    message['Subject'] = subject
    message.attach(MIMEText(text, 'plain'))
    if files:
        for file in files:
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(open(file, 'rb').read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', 'attachment; filename="%s"' % os.path.basename(file))
            message.attach(part)
    
    # Send email
    try:
        server = smtplib.SMTP(smtp_server, port)
        server.starttls()
        server.login(sender, password)
        text = message.as_string()
        server.sendmail(sender, to, text)
        server.quit()
        return True
    except Exception as e:
        print(e)
        return False