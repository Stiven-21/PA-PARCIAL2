from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from smtplib import SMTP
from config import settings
import re

def send_email(user,title,body):
    message = MIMEMultipart()
    message['subject'] = title
    message['from'] = 'soporte@imagenes-daes.com'#emisor
    message['To'] = user
    message_html = MIMEText(body, 'html')
    message.attach(message_html)
    
    username = settings.SMTP_USERNAME
    password = settings.SMTP_PASSWORD

    server = SMTP(settings.SMTP_HOSTNAME)
    server.starttls()
    server.login(username, password)
    server.sendmail(username, user, message.as_string())

    server.quit()
