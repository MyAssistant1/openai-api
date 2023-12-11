# import spacy

# def find_names(sentence):
#     # Using a more general English language model
#     nlp = spacy.load("en_core_web_sm")
#     doc = nlp(sentence)

#     # Extracting entities labeled as persons
#     names = [ent.text for ent in doc.ents if ent.label_ == "PERSON"]

#     return names

# # Example sentence
# sentence = "Send email to Salih and Mehmet."
# names = find_names(sentence)
# print("Names:", names)

import re
import mailatma

def isimleri_bul(cumle):
    # Cümleden isimleri çıkarmak için regex kullanalım
    isimler = re.findall(r'\b[A-Za-zÇçĞğİıÖöŞşÜü]+\b', cumle)
    return isimler

def kisiyi_bul(isim, kisiler):
    bulunan_kisiler = [k for k in kisiler if isim in k]

    if len(bulunan_kisiler) == 1:
        return bulunan_kisiler[0]
    elif len(bulunan_kisiler) > 1:
        print(f"{isim} ismi listede birden fazla bulunuyor. Lütfen soyadını belirtin:")
        soyad = input("Soyad: ")
        for kisi in bulunan_kisiler:
            if soyad.lower() == kisi[1].lower():
                return kisi

    return None

def bul(cumle):
    # Örnek cümle
    #cumle = "Salih ve Mehmet'e mail at"

    # Cümleden isimleri çıkar
    isimler = isimleri_bul(cumle)

    # Kişiler listesi
    kisiler = [
        ("Salih", "Tangel", "salihtangel@gmail.com"),
        ("Ayşe", "Demir", "ayse.demir@email.com"),
        ("Mehmet", "Acar", "mehmet-acar-gs@hotmail.com"),
        ("Ahmet", "Celik", "ahmet.celik@email.com"),


    ]

    # Cümlede bulunan her bir isim için kişiler listesinde kontrol et
    email_adresleri = []
    check = False
    for isim in isimler:
        kisi = kisiyi_bul(isim, kisiler)
        if kisi:
            check = True
            email_adresleri.append(kisi[2])
            print("İsim:", kisi[0])
            print("Soyisim:", kisi[1])
            print("E-posta:", kisi[2])
            print()

    if check==True:
        mailatma.emailgonder(email_adresleri)

    return check

