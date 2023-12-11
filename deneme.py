import smtplib
import ssl
from google_auth_oauthlib.flow import InstalledAppFlow

class EtkinlikTakvimi:
    def __init__(self):
        self.etkinlikler = []
        self.gonderilenler = set()
        self.desteklenen_email_saglayicilari = ["gmail.com", "hotmail.com", "outlook.com", "gtu.edu.tr"]

    def etkinlik_ekle(self, etkinlik):
        self.etkinlikler.append(etkinlik)

    def email_gonder(self, sender_email, sender_password, receiver_email, subject, body):
        port = 465  # SMTP SSL portu
        smtp_server = self.get_smtp_server(sender_email)

        context = ssl.create_default_context()

        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(sender_email, sender_password)

            message = f"Subject: {subject}\n\n{body}"

            server.sendmail(sender_email, receiver_email, message)
            self.gonderilenler.add(receiver_email)

    def get_smtp_server(self, email):
        for saglayici in self.desteklenen_email_saglayicilari:
            if saglayici in email:
                return f"smtp.{saglayici}"
        raise ValueError("Desteklenmeyen e-posta servisi")

# Kullanım örneği
takvim = EtkinlikTakvimi()

# E-posta adresleri
email_adresleri = [
    "mehmet-acar-gs@hotmail.com",
    "mhmtacargs107@gmail.com",
    "salih.tangel2017@gtu.edu.tr",
    "mehmetacar@gtu.edu.tr"
]

# Etkinlik eklemek
#takvim.etkinlik_ekle("Toplantı", "2023-11-30 14:00")

# E-posta göndermek
try:
    for email_adresi in email_adresleri:
        takvim.email_gonder(    "salihtangel@gmail.com","+*4152aAbCtX19", email_adresi, "Toplantı Daveti", "Toplantı zamanı: 2023-11-30 14:00")
        print(f"E-posta gönderildi: {email_adresi}")
except Exception as e:
    print(f"E-posta gönderme hatası: {e}")

# Gönderilenler listesini göstermek
print("Gönderilenler Listesi:")
for email in takvim.gonderilenler:
    print(email)
