#Refer back to the demo to see examples of all the commands you'll need to use in order to figure out these questions.

#Replace the blank function for each question with the code to accomplish what the question asks for.

#Level 1 – straightforward.

#If you’re stumped, you probably just need to look at the demo file again and find the right command!

#Return the character at index 2 in string s. (Which I’ll remind you is not the second character.)
#s = "Hello"
#print(string[2])
#
#Return the fifth character in string s. (Which I’ll remind you is not the character at index 5.)
#s = "Hello"
#print(s[4])
#
#Return the number of characters in the string.
#s = "Hello"
#print(len(s))
#
#Return the first character.
#s = "Hello"
#print(s[0])
#
#Return the last character.
#s = "Hello"
#print(s[-1])
#Return the penultimate character. (Penultimate means “second to last”).
#s = "Hello"
#print(s[-2])
#
#Return the five character long substring starting at index 3.
#s = "Bonjourno"
#sub = s[3:9]
#print(sub)
#
#Return a substring consisting of the last five characters of the string.
#s = "Bonjourno"
#sub = s[-5:]
#print(sub)
#
#Return a substring starting at the character at index 3 and continuing to the end of the string.
#s = "Bonjourno"
#sub = s[3:]
#print(sub)
#
#Return the original string in all lowercase.
#s = "HELLO"
#lower = s.lower()
#print(lower)
#
#Return the original string in all uppercase.
#s = "hello"
#upper = s.upper()
#print(upper)
#
#Convert the string to a list and return the list. (For instance, "CATS" --> ["C", "A", "T", "S"].)
#s = "Bonjourno"
#list = []
#for letter in s:
#  list.append(letter)
#print(list)
#
#Return the string shifted to the right by one (ie, the original string with the last character removed).
#s = "Hello"
#s_new = s[:-1]
#print(s_new)
#
#Return the string shifted to the left by one (ie, the original string with the first character removed).
#s = "Hello"
#s_new = s[1:]
#print(s_new)
#
#Level 2 – kinda tricky.

#Some of these questions are pretty challenging! It's ok if you need to ask for help! You can absolutely do these with only the commands demonstrated in the demo file though; no need to Google.

#Return the number of times a lower case e appears in the string.
#s = "Steeering"
#e_count = s.count('e')
#print(e_count)
#
#Return the number of times a lower or upper case e appears in the string.
#s = "steeeeeeEEEeering"
#e_count = s.count('e') + s.count('E')
#print(e_count)
#
#Return the total number of times any lower or upper case vowel (do not include y) appears in the string. Example: "Every vowel counts" --> 6, because there are 6 total vowels in that string, including the capital E.
#vowels = ['a','e','i','o','u']
#vowelcount = 0
#string = "Every vowel counts, including this extra part"
#for letter in string.lower():
#  if letter in vowels:
#    vowelcount += 1
#  else:
#    pass
#print(vowelcount)
#
#Return a list containing every vowel from the original string, in the order they originally appeared. (Hint: make a blank list, then use a for loop over each character in the string and use an if statement inside the for loop to decide when to append to the list.)
#Example: "Every vowel counts" --> ["E", "e", "o", "e", "o", "u"]
#string = "Every vowel counts"
#vowel_list = []
#vowels = ['a','A','e','E','i','I','o','O','u','U']
#for letter in string:
#  if letter in vowels:
#    vowel_list.append(letter)
#  else:
#    pass
#print(vowel_list)
#
#Make a new string that consists of every other character in the original string (ie, the characters at index 0, 2, 4, etc) and return that.
#string = "Bonjourno"
#newstring = ""
#count = 0
#for letter in string:
#  if count % 2 == 0:
#    newstring += letter
#    count += 1
#  else:
#    count += 1
#print(newstring)
#
#Make a new string that consists of every other character in the original string starting with the character at index 1 (ie, the characters at index 1, 3, 5, etc) and return that.
#string = "Bonjourno"
#newstring = ""
#count = 0
#for letter in string:
#  if count % 2 == 1:
#    newstring += letter
#    count += 1
#  else:
#    count += 1
#print(newstring)
#
#Return a list of every 2-character substring of the original string. Example: "CATS" --> ["CA", "AT", "TS"]
#string = "DOGGIES"
#currentindex = ""
#newstring = ""
#list = []
#index = 0
#for letter in string:
#  currentindex = letter
#  if letter is not string[-1]:
#    list.append(string[index:index+2])
#    index += 1
#  else:
#    pass
#print(list)
#
#Return a string made by replacing every third character of the original string with an exclamation point, starting at index 0.
string = "ExampleString"
newstring = ""
index = 0
for letter in string:
  if (index/3).is_integer() == True:
    newstring += "!"
    index += 1
  else:
    newstring += letter
    index += 1
print(newstring)

#Return a string made by replacing every third character of the original string with an exclamation point, starting at index 2.
#indexcount = 0
#string = "Bonjourno"
#newstring = ""
#threelist = [2,5,8,11,14,17,20]
#for letter in range(len(string)):
#  if letter in threelist:
#    newstring += "!"
#    indexcount += 1
#  else:
#    indexcount += 1
#    newstring += str(string[letter])    
#print(newstring)
# 
#Example output.

#You can certainly use the built in tests, but if you want to see it all at once, here is what the complete output should look like if you use s = "ExampleString".

#Questions 17, 18, 22, and 23 are especially worth double-checking!

#1: a
#2: p
#3: 13
#4: E
#5: g
#6: n
#7: mpleS
#8: tring
#9: mpleString
#10: examplestring
#11: EXAMPLESTRING
#12: ['E', 'x', 'a', 'm', 'p', 'l', 'e', 'S', 't', 'r', 'i', 'n', 'g']
#13: ExampleStrin
#14: xampleString
#15: 1
#16: 2
#17: 4
#18: ['E', 'a', 'e', 'i']
#19: Eapetig
#20: xmlSrn
#21: ['Ex', 'xa', 'am', 'mp', 'pl', 'le', 'eS', 'St', 'tr', 'ri', 'in', 'ng']
#22: !xa!pl!St!in!
#23: Ex!mp!eS!ri!g



