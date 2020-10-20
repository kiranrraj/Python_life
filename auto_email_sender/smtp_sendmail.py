import smtplib

with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()

    smtp.login('kiranrajvjd@gmail.com', 'app_pswd')

    subject = "My first automated mail"
    body = "Hello how are you doing"
    msg = f"Subject: {subject}\n\n{body}"

    smtp.sendmail('your_email','receivers_email', msg)