import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

sender = os.getenv("EMAIL_USER")
password = os.getenv("EMAIL_PASS")
recipient = os.getenv("EMAIL_TO")

subject = "Monthly Report"
body = "Hello! This is your monthly email report."

# Create the email
msg = MIMEMultipart()
msg['From'] = sender
msg['To'] = recipient
msg['Subject'] = subject
msg.attach(MIMEText(body, 'plain'))

# Send the email via Gmail SMTP server
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
    server.login(sender, password)
    server.send_message(msg)

print("Email sent successfully.")
