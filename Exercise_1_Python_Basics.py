#Define a function named "print_length" that takes a text string as an argument and prints the length of that text string. For example, this code:
#my_string = "hello"
#print_length(my_string)
#other_string = "goodbye"
#print_length(other_string)
#...should print out:

#The string hello has length 5
#The string goodbye has length 7

def print_length(string):
    string_length = len(string)
    print("The string " + str(string.lower()) + " has length " + str(string_length))
print_length("Hello")
print_length("Goodbye")

#Define a function named "print_copies" that prints as many copies as there are letters in the string. For example, this code:
#my_string = "hello"
#print_copies(my_string)
#other_string = "goodbye"
#print_copies(other_string)
#...should print out:
#
#hellohellohellohellohello
#goodbyegoodbyegoodbyegoodbyegoodbyegoodbyegoodbye

my_string = "hello"
other_string = "goodbye"
def print_copies(string):
    length = len(string)
    multiply = string*length
    print(multiply)
print_copies(my_string)
print_copies(other_string)