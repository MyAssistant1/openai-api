# Refer to the Python quickstart on how to setup the environment:
# https://developers.google.com/calendar/quickstart/python
# Change the scope to 'https://www.googleapis.com/auth/calendar' and delete any
# stored credentials.
import datetime
import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

event = {
  'summary': 'Google I/O 2015',
  'location': '800 Howard St., San Francisco, CA 94103',
  'description': 'A chance to hear more about Google\'s developer products.',
  'start': {
    'dateTime': '2023-10-27T09:00:00-07:00',
    'timeZone': 'America/Los_Angeles',
  },
  'end': {
    'dateTime': '2023-10-28T17:00:00-07:00',
    'timeZone': 'America/Los_Angeles',
  },
  'recurrence': [
    'RRULE:FREQ=DAILY;COUNT=2'
  ],
  'attendees': [
    {'email': 'salihtangel@gmail.com'},
    {'email': 'mhmtacargs107@gmail.com'},
  ],
  'reminders': {
    'useDefault': False,
    'overrides': [
      {'method': 'email', 'minutes': 24 * 60},
      {'method': 'popup', 'minutes': 10},
    ],
  },
}

from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow

#TODO
#burada surekli izin almak istiyor bu bir seferlik olmasi lazim bununla ilgilen
# Kullanılacak API
API_NAME = 'calendar'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/calendar']

# OAuth 2.0 kimlik doğrulama akışını başlat
flow = InstalledAppFlow.from_client_secrets_file(
    'credentials.json',  # Google API Console'dan indirdiğiniz JSON dosyasının yolu
    SCOPES
)
credentials = flow.run_local_server(port=0)

# API'yi oluştur
service = build(API_NAME, API_VERSION, credentials=credentials)
event = service.events().insert(calendarId='primary', body=event).execute()
print ('Event created: %s' % (event.get('htmlLink')) )

