import nltk
# #nltk.download('punkt')
# #nltk.download('averaged_perceptron_tagger')
# def analiz_et(cumle):
#     kelimeler = nltk.word_tokenize(cumle)
#     etiketler = nltk.pos_tag(kelimeler)

#     for kelime, etiket in etiketler:
#         print(f"{kelime}: {etiket}")

# cumle = "Send email to Mehmet and Salih."
# analiz_et(cumle)

import nltk
# nltk.download('punkt')  # Gerekli olabilir, ancak bir kere indirildikten sonra tekrar indirme gerekmez
# nltk.download('averaged_perceptron_tagger')

def analiz_et(cumle):
    kelimeler = nltk.word_tokenize(cumle)
    etiketler = nltk.pos_tag(kelimeler)

    # Sadece NN ve NNP etiketlerini içeren kelimeleri filtrele
    istenen_etiketler = ['NN', 'NNP']
    filtrelenmis_kelimeler = [kelime for kelime, etiket in etiketler if etiket in istenen_etiketler]

    return filtrelenmis_kelimeler 

cumle = "Send email to Mehmet and Salih."
analiz_et(cumle)
