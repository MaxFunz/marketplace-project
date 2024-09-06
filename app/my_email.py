import os
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from fastapi import BackgroundTasks

def send_email_sync(subject: str, body: str, to_email: str):
    login = os.getenv('SMTP_USER', 'kurn0sovm@yandex.ru')
    password = os.getenv('SMTP_PASSWORD', 'xTOYS?eY/K2U9nJ?')  # Use environment variable
    smtp_server = 'smtp.yandex.ru'
    smtp_port = 587

    msg = MIMEText(body, 'plain', 'utf-8')
    msg['Subject'] = Header(subject, 'utf-8')
    msg['From'] = login
    msg['To'] = to_email

    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(login, password)
            server.sendmail(login, [to_email], msg.as_string())
        print("Email отправлен успешно")
    except Exception as ex:
        print(f"Ошибка при отправке email: {ex}")

async def send_email_async(subject: str, body: str, to_email: str, background_tasks: BackgroundTasks):
    background_tasks.add_task(send_email_sync, subject, body, to_email)
