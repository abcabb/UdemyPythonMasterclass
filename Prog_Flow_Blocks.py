# Code Blocks (Indentation in Python)

for i in range(1,13):
    print("{} squared is {} and cubed is {}.".format(i, i ** 2, i ** 3))
    print("*" * 50)

# If statement

name = input("Whats your name ?")
age = int(input("Hello {}, how old are you?".format(name)))
print("{} is {} years old".format(name, age))

if age>=18:
    print("You are old enough to vote.")
    print("Please vote.")
elif age>120:
    print("You might typoed.")
else:
    print("Please come back after {} years later.".format(18-age))

# Guessing Game

answer = 5

print("Please guess a number between 1 and 10: ")
guess = int(input())

# if guess<answer:
#     print("Please guess higher")
#     guess = int(input())
#     if guess == answer:
#         print("Correct answer")
#     else:
#         print("Sorry, incorrect")
# elif guess>answer:
#     print("Please guess lower")
#     guess = int(input())
#     if guess == answer:
#         print("Correct answer")
#     else:
#         print("Sorry, incorrect")
# else:
#     print("Its true number!")

if guess == answer:
    print("You answered correctly.")
else:
    if guess < answer:
        print("Please guess higher")
    else: #guess>answer:
        print("Please guess lower")
    guess = int(input())
    if guess == answer:
        print("Correct answer.")
    else:
        print("Incorrect.")

# More On Conditions

age = int(input("How old are you? "))

# if age>=16 and age<=65:
#     print("Have a good day at work.")
#Simplyfy the chained comparison vvvv
if 65>=age>=16:
    print("Have a good day at work.")
else:
    print("Enjoy your free time")

if 16>age or 65<age:
    print("Enjoy your free time")
else:
    print("Have a good day at work.")

# More examples

day = "Monday"
temperature = 30
raining = True

if (day == "Saturday" and temperature>25) or not raining: # Burada operator precedence'a dikkat et.
    print("Go Swimming")    #You must use parantheses to prevent logical mistakes that you can make. And you dont need to remember operator precedence.
else:
    print("Learn Python")

# Truth Value Testing

if 0:
    print("True") # This code is unreachable. Çünkü 0 expression'u hiçbir zaman True döndürmez.
else:
    print("False")

name = input("Please entre your name: ")

if name:
    print("Hello, {}".format(name))
else: # Empty string False değerini verir.
    print("Are you the man with no name?")

# In and Not In Operators
parrot = "Norwegian Blue"

letter = input("Enter the letter: ")

if letter in parrot:
    print("{} is in {}".format(letter,parrot))
else:
    print("We dont need that lettter.")

activity = input("What would you like to do today?")

if "cinema" not in activity.casefold():
    print("But i want to go to the cinema!")
else:
    print("Lets go!")

# Little Challange

name = input("Whats your name?")
age = int(input("Hello {}, how old are you".format(name)))

if 18<=age<=30:
    print("Welcome to holiday.")
else:
    print("Sorry. You are rejected.")
