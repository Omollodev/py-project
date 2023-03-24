from email.message import EmailMessage
from app2 import password
import ssl
import smtplib

email_sender = "devoxotieno78@gmail.com"
email_password = password

email_receiver = "vivos49748@loongwin.com"

subject = "Please don't to subscribe and like"

body = """
When you receive this email please don't forget to subscribe and like my python project.
Indeed i need all your support to be a guru in programing and hacking.

Thank you.
 
"""

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())
