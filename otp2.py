"""
All-in-one Gmail OTP Sender
---------------------------------
• Prompts for the recipient's email
• Generates a 6-digit random OTP
• Sends it securely using Gmail SMTP
• Prints the OTP to console for testing
"""

import smtplib
import ssl
import random
from email.message import EmailMessage

# ==== 1. Your Gmail details ====
# Use your Gmail address and the 16-character App Password you generated
SENDER_EMAIL = "minakshi.dekate777@gmail.com"        # <-- put your Gmail here
APP_PASSWORD = "Unnati@13227"    # <-- paste the App Password

# ==== 2. Ask user for recipient email ====
receiver_email = input("Enter the recipient's email address: ").strip()

# ==== 3. Generate a random 6-digit OTP ====
otp = str(random.randint(100000, 999999))
print(f"[Debug] Generated OTP: {otp}")  # remove this line in production

# ==== 4. Compose the email ====
msg = EmailMessage()
msg["From"] = SENDER_EMAIL
msg["To"] = receiver_email
msg["Subject"] = "Your One-Time Password (OTP)"
msg.set_content(
    f"Your verification code is: {otp}\n"
    "This code is valid for 5 minutes."
)

# ==== 5. Send the email securely ====
context = ssl.create_default_context()
try:
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(SENDER_EMAIL, APP_PASSWORD)
        server.send_message(msg)
    print(f"✅ OTP sent to {receiver_email}")
except Exception as e:
    print("Email error:", e)