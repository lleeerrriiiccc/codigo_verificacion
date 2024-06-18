import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import random
import json




# Example usage

def generate_verification_code():
    code = []
    for i in range(6):
        verification_code = random.randint(0, 9)
        code.append(verification_code)
    str(code)
    code = str(code).replace(",","").replace("[","").replace("]","")
    return code
verification_code = generate_verification_code()
# Corrected example usage with properly formatted HTML content

def send_email(sender_email, receiver_email, subject, code):

    # Set up the SMTP server
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    smtp_username = "code86613@gmail.com"
    smtp_password = "awwu qqpz uuse luii"
    
    # Create a multipart message
    email_message = MIMEMultipart()
    email_message["From"] = sender_email
    email_message["To"] = receiver_email
    email_message["Subject"] = subject
    html_content = f"""
    <style>
        .head {{
            text-align: center;
            background-color: green;
            padding: 20px;
        }}

        h1 {{
            color: #333;
            font-size: 24px;
            margin-bottom: 10px;
        }}

        p {{
            color: #666;
            font-size: 16px;
            margin-bottom: 5px;
        }}

        .code {{
            text-align: center;
            margin-top: 20px;
        }}

        .code p {{
            font-size: 20px;
            font-weight: bold;
            color: blue;
        }}
    </style>

    <div class="head">
        <h1>Code Verification</h1>
    </div>

    <div class="code">
        <p>This is your verification code</p>
        <p>{code}</p>
    </div>
    """
    # Add body to the email
    email_message.attach(MIMEText(html_content, "html"))
   
    # Connect to the SMTP server and send the email
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(smtp_username, smtp_password)
        server.send_message(email_message)
        with open("data/code.json", "w") as file:
            json.dump({"code": code}, file)
def check_code():
    with open("data/code.json", "r") as file:
        data = json.load(file)
    return data["code"]
