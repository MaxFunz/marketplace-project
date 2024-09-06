import smtplib
from email.mime.text import MIMEText
from email.header import Header
import os

def send_email(subject: str, message: str, to_address: str):
    smtp_server = os.getenv('SMTP_SERVER', 'smtp.yandex.ru')
    smtp_port = int(os.getenv('SMTP_PORT', 587))
    smtp_user = os.getenv('SMTP_USER', 'kurn0sovm@yandex.ru')
    smtp_password = os.getenv('SMTP_PASSWORD', 'xTOYS?eY/K2U9nJ?')
    email_from = os.getenv('EMAIL_FROM', 'kurn0sovm@yandex.ru')

    msg = MIMEText(message, 'plain', 'utf-8')
    msg['Subject'] = Header(subject, 'utf-8')
    msg['From'] = email_from
    msg['To'] = to_address

    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(smtp_user, smtp_password)
            server.sendmail(email_from, [to_address], msg.as_string())
        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")

if __name__ == "__main__":
    recipient_email = 'recipient@example.com'
    send_email('Test Subject', 'This is a test message.', recipient_email)
