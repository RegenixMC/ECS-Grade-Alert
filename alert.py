from pushbullet import Pushbullet
import smtplib, ssl



pb = Pushbullet('o.KRoEAeCZNj5dr2JocPb68ZuKJbLLBf9u')

def sendAlert(number, textData):
    device = pb.devices[0]
    push = pb.push_sms(device, "+" + number, textData)



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