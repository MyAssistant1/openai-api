# Refer to the Python quickstart on how to setup the environment:
# https://developers.google.com/calendar/quickstart/python
# Change the scope to 'https://www.googleapis.com/auth/calendar' and delete any
# stored credentials.

from email import parser
from anyio import Event
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from datetime import datetime, timedelta
from dateutil import parser
from dateutil.relativedelta import relativedelta

def parse_date_time(input_str):
    # Verilen string'i parse ederek datetime nesnesini döndürür
    dt = parser.parse(input_str)
    return dt

def create_event(summary, location, description, start_datetime, end_datetime, attendees):
    # Etkinlik nesnesi oluşturur
    event = {
        'summary': summary,
        'location': location,
        'description': description,
        'start': {
            'dateTime': start_datetime,
            'timeZone': 'Europe/Istanbul',
        },
        'end': {
            'dateTime': end_datetime,
            'timeZone': 'Europe/Istanbul',
        },
        'attendees': [{'email': email} for email in attendees],
        'reminders': {
            'useDefault': False,
            'overrides': [
                {'method': 'email', 'minutes': 24 * 60},
                {'method': 'popup', 'minutes': 10},
            ],
        },
    }
    return event


   
def addEvent(subject,content,input_date_time_str):
# Kullanım örneği:
#input_date_time_str = "December 19th at 20:00"
  attendees_emails = ['salihtangel@gmail.com', 'mhmtacargs107@gmail.com']
  # Kullanıcıdan alınan tarih ve saat bilgisini parse et
  parsed_datetime = parse_date_time(input_date_time_str)

      # Etkinlik süresini belirle (örneğin, 2 saat)
  end_datetime = parsed_datetime + relativedelta(hours=2)

      # Event nesnesini oluştur
  event = create_event(
          summary='Google I/O 2015',
          location='800 Howard St., San Francisco, CA 94103',
          description='A chance to hear more about Google\'s developer products.',
          start_datetime=parsed_datetime.isoformat(),
          end_datetime=end_datetime.isoformat(),
          attendees=attendees_emails,
  )

      # Oluşturulan etkinliği ekrana yazdır
  print(event)

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
