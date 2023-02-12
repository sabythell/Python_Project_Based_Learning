#Your job is to rewrite handle_input so that the code becomes a simple game where the user plays to guess the random number the computer generated. You should leave the rest of the code as-is. Specifically, inside handle_input, you should:

#Compare the user's number with the randomly generated global variable at the top of the file.
#If the user guessed too high, say so.
#If they guessed too low, say so.
#If they guessed correctly, say so.
#That's it!
#handle_input should not have any input or while commands in it! Use the input from the loop that is already programmed.

from random import randint  # Get method to make random numbers
target_number = randint(1, 100) # Make a random number between 1 and 100

# This is the function you will write!
# (See instructions!)
def handle_input(num):
  print("you typed", num)
  if num == target_number:
    print("You got it! Don't forget to type 'quit' to quit!")
  if num != target_number:
    if num>target_number:
        print("Too high, try again!")
    if num<target_number:
        print("Too low, try again!")

# This will keep asking the user to type something until they type 'quit'
def input_loop():
  while True:
    user_in = input("> ").strip()
    if user_in == "quit":
      break
    else:
      num = int(user_in)
      handle_input(num)
    print()

print("Welcome to Guess The Number!")
print("Type a number to guess; type 'quit' to quit!")
input_loop()