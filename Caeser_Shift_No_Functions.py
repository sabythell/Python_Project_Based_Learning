from itertools import count


alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
test = "HELLOWORLD"
encode_string = ""
decode_string = ""
shift = 5

for letter in test:
    find = alpha.find(letter)
    find += shift
    if find > 25:
        find = find - 26
        encode_char = alpha[find]
        encode_string += encode_char
    else:
        encode_char = alpha[find]
        encode_string += encode_char
print(encode_string)
for letter in encode_string:
    find = alpha.find(letter)
    find -= shift
    if find < 0:
        find = find + 26
        decode_char = alpha[find]
        decode_string += decode_char
    else:
        decode_char = alpha[find]
        decode_string += decode_char
print(decode_string)