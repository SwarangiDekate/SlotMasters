import smtplib
import ssl
import random
import os
from email.message import EmailMessage
from dotenv import load_dotenv   # only if using .env file

load_dotenv()  # reads .env if present

# --- 1. Generate a random 6-digit OTP ---
otp = str(random.randint(100000, 999999))
print(f"Generated OTP (for testing): {otp}")

# --- 2. Email details ---
sender_email = os.getenv("SENDER_EMAIL")      # e.g. your Gmail address
app_password = os.getenv("APP_PASSWORD")      # Gmail App Password
receiver_email = "recipient@example.com"      # change to the target email

subject = "Your One-Time Password (OTP)"
body = f"Your verification code is: {otp}\nThis code is valid for 5 minutes."

# --- 3. Compose email ---
msg = EmailMessage()
msg["From"] = sender_email
msg["To"] = receiver_email
msg["Subject"] = subject
msg.set_content(body)

# --- 4. Send email securely ---
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, app_password)
    server.send_message(msg)

print("✅ OTP email sent successfully!")