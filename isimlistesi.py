from google.oauth2 import service_account
from googleapiclient.discovery import build

# Kimlik bilgilerini yükleyin
credentials = service_account.Credentials.from_service_account_file('credentials.json', scopes=['https://www.googleapis.com/auth/contacts.readonly'])

# Google Contacts API'yi oluşturun
contacts_service = build('people', 'v1', credentials=credentials)

# Kişi listesini alın
contacts = contacts_service.people().connections().list(resourceName='people/me', pageSize=10).execute().get('connections', [])

# Top 10 kişiyi bastırın
print("Top 10 Kişi:")
for i, contact in enumerate(contacts, start=1):
    names = contact.get('names', [])
    if names:
        name = names[0].get('displayName', 'N/A')
        print(f"{i}. {name}")

