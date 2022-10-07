# Read the instructions to see what you need to do here!

from base64 import decode


alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
cipher_alphabet = "WJKUXVBMIYDTPLHZGONCRSAEFQ"
test = "HELLOWORLD"

def sub_encode(text, codebet):
  encode_string = ""
  for letter in test:
    find = alpha.find(letter)
    encode = cipher_alphabet[find]
    encode_string += encode
  return encode_string

def sub_decode(text, codebet):
  decode_string = ""
  for letter in enc:
    find = cipher_alphabet.find(letter)
    decode = alpha[find]
    decode_string += decode
  return decode_string


enc = sub_encode(test, cipher_alphabet)
dec = sub_decode(enc, alpha)
print(enc)
print(dec)

