import smtplib
from email.message import EmailMessage
 
msg = EmailMessage()
msg['Subject'] = "Automated mail from python"
msg["From"] = 'kiran@gmail.com'
msg['To'] = 'varun.vjd@gmail.com'
msg.set_content('Hi, this is a automated mail from python')

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login('kiran@gmail.com', 'app_password_from_google')

    smtp.send_message(msg)