import smtplib, ssl
from getCalendarDay import *



def sendEmail(emailContext, receiver_email):
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"


    sender_email = "EvergreenAlertSystem@gmail.com"
    password = ('jblqnyqhztdicgkn')

    emailContext = 'Subject: ECS Schedule Alert\n' + emailContext

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, emailContext)
    print('Email sent to, ' + receiver_email)