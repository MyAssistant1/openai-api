# Refer to the Python quickstart on how to setup the environment:
# https://developers.google.com/calendar/quickstart/python
# Change the scope to 'https://www.googleapis.com/auth/calendar' and delete any
# stored credentials.

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from datetime import datetime, timedelta

def addEvent(name,subject,content,time): 
  # Get the current date and time
  current_datetime = datetime.now()

  # Remove the 'th' from the day in the time string
  time_without_th = time.replace('th', '')

  # Parse the provided time string
  user_input_time = datetime.strptime(time_without_th, '%B %d %I:%M %p')

  # Set the date part to the current date
  event_time = current_datetime.replace(month=user_input_time.month, day=user_input_time.day,
                                          hour=user_input_time.hour, minute=user_input_time.minute)

  # Calculate the offset between the current timezone and UTC
  utc_offset = current_datetime.utcoffset().total_seconds() / 3600

  # Create the event dictionary
  event = {
      'summary': subject,
      'description': content,
      'start': {
          'dateTime': f'{event_time.strftime("%Y-%m-%dT%H:%M:%S")}{f"{int(utc_offset):+03d}" if utc_offset != 0 else ""}',
          'timeZone': str(current_datetime.tzinfo),
      },
      'end': {
          'dateTime': f'{(event_time + timedelta(hours=1)).strftime("%Y-%m-%dT%H:%M:%S")}{f"{int(utc_offset):+03d}" if utc_offset != 0 else ""}',
          'timeZone': str(current_datetime.tzinfo),
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

