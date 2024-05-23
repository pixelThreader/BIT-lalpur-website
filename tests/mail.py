import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Email credentials and details
smtp_server = "smtp.example.com"
smtp_port = 587  # For TLS
smtp_username = "your_email@example.com"
smtp_password = "your_password"

sender_email = "your_email@example.com"
recipient_email = "recipient_email@example.com"
subject = "Test Email"
body = "This is a test email sent from Python."

# Create the email
msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = recipient_email
msg['Subject'] = subject

msg.attach(MIMEText(body, 'plain'))

try:
    # Connect to the server
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()  # Secure the connection
    server.login(smtp_username, smtp_password)  # Login to the email account
    server.sendmail(sender_email, recipient_email, msg.as_string())  # Send the email
    print("Email sent successfully!")
except Exception as e:
    print(f"Error: {e}")
finally:
    server.quit()  # Close the connection
