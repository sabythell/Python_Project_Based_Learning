#You should see two function headers in main.py. Write the two functions so they correctly encode and decode using a given Vigenere Cipher keyword and return the results.

#Some details to consider:

#You might need to spend some time thinking about how to decode a message that's been encoded with a Vigenere Cipher - it's a little tricky!
#You will ONLY get strings made of capital letters. We won't worry about spaces, lowercase letters, grammar characters, etc.
#You're given alpha at the top of your main.py file; use it!
#You should use the above test case to make sure your code is working properly!

#expected result below:
#THEQUICKBROWNFOXJUMPEDOVERTHELAZYDOG
#TESTTESTTESTTESTTESTTESTTESTTESTTEST
#------------------------------------
#MLWJNMUDUVGPGJGQCYEIXHGOXVLAXPSSRHGZ

alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
test = "THEQUICKBROWNFOXJUMPEDOVERTHELAZYDOG"
vig_key = "TEST"

def vig_encode(text, keyword):
    count = 0
    vig_key_full = ""
    vig_key_number_list = []
    total_list = []
    for index in range(len(test)):
        if count == 3:
            vig_key_full += vig_key[count]
            count = 0
        else:
            vig_key_full += vig_key[count]
            count += 1
    count = 0
    for letter in vig_key_full:
        find = alpha.find(letter)
        vig_key_number_list.append(find)
    current_index = 0
    for letter in test:
        find = alpha.find(letter)
        sum = find + int(vig_key_number_list[current_index])
        total_list.append(sum)
        current_index += 1
    final_list = []
    for number in total_list:
        if number > 25:
            number = number - 26
            final_list.append(number)
        else:
            final_list.append(number)
    current_index = 0
    encode = ""
    for number in final_list:
        encode += alpha[number]
    return(encode)

def vig_decode(text, keyword):
    count = 0
    vig_key_full = ""
    vig_key_number_list = []
    total_list = []
    for index in range(len(enc)):
        if count == 3:
            vig_key_full += vig_key[count]
            count = 0
        else:
            vig_key_full += vig_key[count]
            count += 1
    count = 0
    for letter in vig_key_full:
        find = alpha.find(letter)
        vig_key_number_list.append(find)
    current_index = 0
    for letter in enc:
        find = alpha.find(letter)
        sum = find - int(vig_key_number_list[current_index])
        total_list.append(sum)
        current_index += 1
    final_list = []
    for number in total_list:
        if number > 25:
            number = number - 26
            final_list.append(number)
        else:
            final_list.append(number)
    current_index = 0
    decode = ""
    for number in final_list:
        decode += alpha[number]
    return(decode)


enc = vig_encode(test, vig_key)
dec = vig_decode(enc, vig_key)
print(enc)
print(dec)



    





