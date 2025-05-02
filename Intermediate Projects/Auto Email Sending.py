import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os
import getpass

def send_email(sender_email, sender_password, receiver_email, subject, body, attachment_path=None):
    """
    Send an email with optional attachment.
    
    Args:
        sender_email (str): Email address of the sender
        sender_password (str): Password for the sender's email account
        receiver_email (str): Email address of the recipient
        subject (str): Subject of the email
        body (str): Body content of the email
        attachment_path (str, optional): Path to file to attach. Defaults to None.
    """
    try:
        # Create message container
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = receiver_email
        msg['Subject'] = subject
        
        # Add body to email
        msg.attach(MIMEText(body, 'plain'))
        
        # Add attachment if provided
        if attachment_path and os.path.exists(attachment_path):
            attachment = open(attachment_path, "rb")
            
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(attachment.read())
            encoders.encode_base64(part)
            
            part.add_header('Content-Disposition', 
                           f"attachment; filename= {os.path.basename(attachment_path)}")
            
            msg.attach(part)
            attachment.close()
        
        # Create SMTP session
        with smtplib.SMTP('smtp.gmail.com', 587) as server:  # Using Gmail SMTP server
            server.starttls()  # Enable security
            server.login(sender_email, sender_password)  # Login
            text = msg.as_string()
            server.sendmail(sender_email, receiver_email, text)
        
        print("Email sent successfully!")
    
    except Exception as e:
        print(f"Error occurred while sending email: {e}")

if __name__ == "__main__":
    print("Email Sender Application")
    print("------------------------")
    
    sender_email = input("Enter your email address: ")
    sender_password = getpass.getpass("Enter your email password: ")
    receiver_email = input("Enter recipient email address: ")
    subject = input("Enter email subject: ")
    body = input("Enter email body: ")
    
    attach = input("Do you want to attach a file? (yes/no): ").lower()
    attachment_path = None
    
    if attach == 'yes':
        attachment_path = input("Enter the full path to the file: ")
    
    send_email(sender_email, sender_password, receiver_email, subject, body, attachment_path)
