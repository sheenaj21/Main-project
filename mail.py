import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(to_whom,subject,content):
    sender_mail = "sheenajmarian@gmail.com"
    sender_pass = "htddljsysrhdivys"
    reciever_mail = to_whom


    try:
        msg = MIMEMultipart()
        msg['From'] = sender_mail
        msg['To'] = reciever_mail
        msg['Subject'] = subject
        msg.attach(MIMEText(content,'plain'))

        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(sender_mail, sender_pass)
            server.sendmail(sender_mail, reciever_mail, msg.as_string())
            print("email send successfully")
    except Exception as e:
        print(f'error:{e}')
