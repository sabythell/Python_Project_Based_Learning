import math

# Read the instructions to see what to do!
global alpha
global numbers

alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = []
no_count = 0
for letter in alpha:
    numbers.append(no_count)
    no_count += 1

# PART 1
# These functions are provided for you!
def mod_inverse_helper(a, b):
    q, r = a//b, a%b
    if r == 1:
        return (1, -1 * q)
    u, v = mod_inverse_helper(b, r)
    return (v, -1 * q * v + u)

def mod_inverse(a, m):
    assert math.gcd(a, m) == 1, "You're trying to invert " + str(a) + " in mod " + str(m) + " and that doesn't work!"
    return mod_inverse_helper(m, a)[1] % m


# These are the functions you'll need to write:
def affine_encode(text, a, b):
    string  = ""
    for letter in text:
        index = alpha.index(letter)
        index = (index * a) + b
        affine = index%26
        string = string + alpha[affine]
    return string


def affine_decode(text, a, b):
    string = ""
    for letter in text:
        index = alpha.index(letter)
        index = (index - b) * mod_inverse(a,26)
        decode = index%26
        string = string + alpha[decode]
    return string

test = "HELLOWORLD"
a = 3
b = 9
enc = affine_encode(test, a, b)
dec = affine_decode(enc, a, b)
print(enc)
print(dec)
# If this worked, dec should be the same as test!



# PART 2
# These  are the functions you'll need to write:
def convert_to_num(ngram):
    result_list = []
    count = 0
    for letter in ngram:    #for every letter in ngram
        index = alpha.index(letter)     #the variable index = the index number where that letter is in the alphabet a=0, z= 25
        index_result = index * (26**count)  #index result = current alphabet index multiplied by 26 to the power of count
        result_list.append(index_result)    #add result to result list
        count += 1  #count updates by 1. The next index result increases the power multiplication by 1
    r = 0   #temporary result set to 0
    for number in result_list:  #for every number in number list
        r = r + number  #result is equal to the current result plus the next in the list
    return r    #return the total


def convert_to_text(num, n):
    count = n
    list = []
    while n > 0:
        mod = num%26
        list.append(int(mod))
        num = num/26
        n -= 1
        string = ""
        for number in list:
            letter = alpha[number]
            string = string + letter
    return string
        





test = "ABCZ"
l = len(test)
num = convert_to_num(test)
answer = convert_to_text(num, l)
print(num)
print(answer)
# If this worked, answer should be the same as test!



# PART 3

# These are the functions you'll need to write:
def affine_n_encode(text, n, a, b):
    while len(text)%n != 0:
        text += "X"
    length = len(text)
    count = 0
    end = count + n
    list = []
    for letter in text:
        if count >= length:
            break
        else:
            sub = (text[count:end])
            list.append(sub.upper())
            count = count + n
            end = end + n
    encoded_string = ""
    for subword in list:
        converted_sub = convert_to_num(subword)
        affine = (converted_sub * a) + b
        affine = affine%(26**n)
        convert = convert_to_text(affine,n)
        encoded_string+= str(convert)
    return encoded_string



def affine_n_decode(text, n, a, b):
    length = len(text)
    count = 0
    end = count + n
    list = []
    for letter in text:
        if count >= length:
            break
        else:
            sub = (text[count:end])
            list.append(sub.upper())
            count = count + n
            end = end + n
    decoded_string = ""
    for subword in list:
        converted_sub = convert_to_num(subword) #correct to here 543,345
        converted_sub = (converted_sub-b)*mod_inverse(a,26**n) #solution was here, a,26**n instead of a,26
        converted_sub = converted_sub%26**n
        convert = convert_to_text(converted_sub,n)
        decoded_string+= str(convert)
    #if (decoded_string[-2:]) == "XX":
    #    decoded_string = decoded_string[:-2] #This is some extra code i added to remove the added 'XX'
    return decoded_string


test = "COOL"
n = 3
a = 3
b = 121
enc = affine_n_encode(test, n, a, b)
dec = affine_n_decode(enc, n, a, b)
print(enc, dec)
# If this worked, dec should be the same as test!