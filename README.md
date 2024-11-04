# API Monitoring Script

This repository contains a Python script for monitoring the status of a RESTful API. The script checks the health of the API at regular intervals and sends an email alert if the API becomes unavailable.

## Features

- Checks API status at configurable intervals.
- Sends email alerts when the API is down.
- Uses environment variables for configuration to keep sensitive information secure.

## Requirements

- Python 3.x
- `requests` library
- `python-dotenv` library

## Installation

1. **Clone the repository:**

        git clone https://github.com/yourusername/api_monitoring.git
        cd api_monitoring

2. Install the required packages:
You can install the required packages using pip:

       pip install requests python-dotenv


3. Create a .env file:
In the project directory, create a .env file with the following contents:

 ```bash
  API_URL= your_api_url
  EMAIL_FROM=your_email@gmail.com
  EMAIL_PASSWORD=your_app_password  # Use your Gmail App Password 
  EMAIL_TO=recipient_email@gmail.com
```
Replace your_email@gmail.com with your Gmail address.
Generate an App Password if you have two-factor authentication enabled (see Gmail App Passwords).
Replace recipient_email@gmail.com with the email address that should receive alerts.

## Usage
Run the monitoring script:

```bash
python monitor_api.py
```
The script will check the API status every minute and send an alert if the API is down.

