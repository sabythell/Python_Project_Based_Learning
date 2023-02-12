#Your job is to write the function test_my_inputs so that your code tells the user if they match your name or age (or both).
# For example, if my name were Jose and I were 17 years old, my code might create the following example runs:
#Type your first name: Jose
#Type your age: 17
#We have the same name and age!

#You should have six different if / elif statements in your code - do you see why?

#After you write test_my_inputs, run several tests to make sure it's working!

def test_my_inputs(name,age):
    if name == my_name and age == my_age:
        print("We have the same name and age!")
    elif name == my_name and age != my_age:
        if age<my_age:
            print("We have the same name, but you are younger!")
        elif age>my_age:
            print("We have the same name, but you are older!")
    elif name != my_name:
        if age == my_age:
            print("We have a different name, but are the same age!")
        elif age != my_age:
            if age>my_age:
                print("We do not have the same name and you are older!")
            elif age<my_age:
                print("We do not have the same name and you are younger!")

my_name = "Sam"
my_age = 30
while True:
    first_name = input("Type your first name: ")
    typed_age = input("Type your age: ")
    age = int(typed_age)
    test_my_inputs(first_name, age)