# Hexadecimal bir string örneği
hex_string = "1a2b3c"

open 
# Hexadecimal string'i binary veriye çevirme
binary_data = bytes.fromhex(hex_string)

# Binary veriyi ekrana yazdırma
print(binary_data)
