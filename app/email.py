from flask_mail import Message
from flask import render_template
from . import mail
import smtplib


def mail_message(subject, template, to, **kwargs):
    sender_email='morinegitonga@gmail.com'
    retcode = 0

    email = Message(subject, sender=sender_email, recipients=[to])
    email.body= render_template(template + ".txt",**kwargs)
    email.html= render_template(template + ".html",**kwargs)
    # mail.send(email)

    try:
        mail.send(email)
    except SMTPAuthenticationError as e:
        print("SMTPAuthenticationError", e)
        retcode = 2
    except SMTPServerDisconnected as e:
        print("SMTPServerDisconnected", e)
        retcode = 3
    except SMTPException as e:
        print("SMTPException", e)
        retcode = 1

    if retcode:
        print("retcode", retcode)