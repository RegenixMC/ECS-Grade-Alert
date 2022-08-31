import smtplib, ssl



def sendEmail(message, receiver_email):
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"

    sender_email = "evergreenalertsystem@gmail.com"
    password = ('jblqnyqhztdicgkn')
    message = message

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)
    print('Email sent to, ' + receiver_email)