import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(subject, body, to_email):
    smtp_server = 'smtp.yandex.ru'
    smtp_port = 587
    smtp_user = 'kurn0sovm@yandex.ru'
    smtp_password = 'xTOYS?eY/K2U9nJ?'

    msg = MIMEMultipart()
    msg['From'] = smtp_user
    msg['To'] = to_email
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Устанавливаем TLS
            server.login(smtp_user, smtp_password)
            server.sendmail(smtp_user, to_email, msg.as_string())
        print('Email sent successfully')
    except Exception as e:
        print(f'Failed to send email: {e}')

send_email('Test Subject', 'This is a test email body.', 'recipient@example.com')
