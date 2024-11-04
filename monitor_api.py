import requests
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import time
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Configuration from environment variables
api_url = os.getenv("API_URL")
email_from = os.getenv("EMAIL_FROM")
email_password = os.getenv("EMAIL_PASSWORD")
email_to = os.getenv("EMAIL_TO")

def send_email_alert():
    """Sends an email alert if the API is down."""
    try:
        # Create the email
        msg = MIMEMultipart()
        msg['From'] = email_from
        msg['To'] = email_to
        msg['Subject'] = "Alert: API is down!"
        body = f"The API at {api_url} is not responding."
        msg.attach(MIMEText(body, 'plain'))

        # Setup the SMTP server
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(email_from, email_password)
        text = msg.as_string()

        # Send the email
        server.sendmail(email_from, email_to, text)
        server.quit()
        print("Email alert sent.")
    except Exception as e:
        print("Failed to send email alert:", e)

def check_api():
    """Checks the API status and sends an alert if it's down."""
    try:
        # Make a request to the API
        response = requests.get(api_url, timeout=5)
        # Check if the response is OK
        if response.status_code == 200:
            print("API is up and running.")
        else:
            print("API returned non-200 status code:", response.status_code)
            send_email_alert()
    except requests.RequestException as e:
        # Handle any request exception (e.g., connection error)
        print("API is down:", e)
        send_email_alert()

# Check API every minute
while True:
    check_api()
    time.sleep(60)