import magic

def detect_audio_format(data):
    mime = magic.Magic()
    file_type = mime.from_buffer(data)
    return file_type

# Hexadecimal veriyi bytes'a dönüştür
hex_data = "1xffxf6p...."  # Buradaki veriyi kendi hex verinizle değiştirin
byte_data = bytes.fromhex(hex_data)

# Ses dosyasının formatını belirle
file_format = detect_audio_format(byte_data)
print("Dosya Formatı:", file_format)
