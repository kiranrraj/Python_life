import smtplib

with smtplib.SMTP('localhost', 1025) as smtp:

    subject = "Mail to local Server"
    body = "Hello how are you doing local server"
    msg = f"Subject: {subject}\n\n{body}"
    smtp.sendmail('kiran@gmail','you@gmail', msg)
