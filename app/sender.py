import os
from email.message import EmailMessage
from typing import NamedTuple
from aiosmtplib import send
from pydecora import singleton

@singleton
class SMTPConfigs(NamedTuple):
    smtp_host: str = os.getenv("SMTP_HOST")
    smtp_port: int = os.getenv("SMTP_PORT")
    smtp_user: str = os.getenv("SMTP_USER")
    smtp_pass: str = os.getenv("SMTP_PASS")
    to_email: str = os.getenv("TO_EMAIL")



async def send_email(name: str, email: str, message: str) -> None:
    configs = SMTPConfigs()
    
    email_subject = f"Form submitted by {name}"
    email_body = message + "\n\n" + f"Author: {email}"
    msg = EmailMessage()
    msg["From"] = configs.smtp_user
    msg["To"] = configs.to_email
    msg["Subject"] = email_subject
    msg.set_content(email_body)
    
    print(configs)

    await send(
        msg,
        hostname=configs.smtp_host,
        port=configs.smtp_port,
        username=configs.smtp_user,
        password=configs.smtp_pass
    )
