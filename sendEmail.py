import email, smtplib, ssl
import os
from dotenv import load_dotenv

def send_email(
    message: str,
    subject: str = "New Listing on CoffeeSnobs - Pay it Forward",
    smtp_server: str = "smtp.gmail.com",
    smtp_port: int = 465,
):
    
    # loads the values in the env file
    load_dotenv()
    receiver_email = os.getenv('receiver_email')
    sender_email = os.getenv('sender_email')
    sender_password = os.getenv('sender_password')

    email_message = f"Subject:{subject}\nTo:{receiver_email}\n{message}"

    with smtplib.SMTP_SSL(
        smtp_server, smtp_port, context=ssl.create_default_context()
    ) as email:
        email.login(sender_email, sender_password)
        email.sendmail(sender_email, receiver_email, email_message)