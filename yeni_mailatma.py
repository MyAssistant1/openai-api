import os
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import base64

# API izinleri
SCOPES = ['https://www.googleapis.com/auth/gmail.send']

def get_credentials():
    """Gets valid user credentials from storage or creates new credentials."""
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json')
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    return creds

def create_message(sender, to, subject, body):
    """Create a message for an email."""
    message = MIMEMultipart()
    message['to'] = to
    message['from'] = sender
    message['subject'] = subject
    msg = MIMEText(body)
    message.attach(msg)
    raw = base64.urlsafe_b64encode(message.as_bytes())
    raw = raw.decode('utf-8')
    return {'raw': raw}

def send_message(service, sender, to, subject, body):
    """Send an email message."""
    message = create_message(sender, to, subject, body)
    try:
        message = service.users().messages().send(userId="me", body=message).execute()
        print(f"Message Id: {message['id']}")
        return message
    except Exception as error:
        print(f"An error occurred: {error}")
        return None

def send_email(sender, to, subject, body):
    """Send an email."""
    creds = get_credentials()
    service = build('gmail', 'v1', credentials=creds)
    send_message(service, sender, to, subject, body)

if __name__ == '__main__':
    sender_email = "salihtangel@gmail.com"
    receiver_email = "mehmet-acar-gs@hotmail.com"
    email_subject = "Test Mail"
    email_body = "Merhaba, bu bir test mailidir."
    
    send_email(sender_email, receiver_email, email_subject, email_body)
