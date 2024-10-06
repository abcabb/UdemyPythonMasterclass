# Random Module In Python and Guess Game
import random

higher = 1000
answer = random.randint(1,higher) #it includes both end points
guessOfUser = None
#print(answer) # TODO: Delete after testing.
counter =10

while True:
    if counter == 0:
        print("You lost the game")
        break
    guessOfUser = int(input("Please guess a number between 1 and {}. 0 for quit. ({} claims left) : ".format(higher,counter)))
    if guessOfUser == 0:
        print("Game over. You gave up.")
        break
    elif answer < guessOfUser:
        print("Incorrect. Guess lower:")
    elif answer > guessOfUser:
        print("Incorrect. Guess higher:")
    else: # answer == guessOfUser
        print("Correct answer !")
        break
    counter -= 1

# Binary Search Example - Hi-Lo Game - Else Clause's use with a Loop. - Conditional Debugging

low = 1
high = 1000
guesses = 10

# while guesses != 0:
#     guess = low + (high - low) / 2
#     answer = input("My guess is : {} .Should i guess higher, lower or this guess is correct? "
#                    "Press h for higher, l for lower and c for correct. q for quit. ({} guesses left)."
#                    .format(int(guess),guesses)).casefold()
#     guesses -= 1
#     if answer == "h":
#         #Guess higher. 1 higher than the guess will be lower bound of range
#         low = guess + 1
#     elif answer == "l":
#         #Guess Lower. 1 lower than the guess will be upper bound of range.
#         high = guess - 1
#     elif answer == "c":
#         print("Answer is correct. I guessed it in {} guesses".format(10-guesses))
#         break
#     elif answer == "q":
#         print("Game Over. You gave up.")
#         break
#     else:
#         print("Please enter h,l or c. q for quit")
#         guesses += 1
# else:
#     print("I couldnt find your guess. Sorry.")

while int(low) != int(high):
    guess = low + (high - low) / 2 # Burada floating point division yaptığın için küsüratlılar.
    answer = input("My guess is : {} .Should i guess higher or lower? "
                   "Press h for higher, l for lower and c for correct. ({} guesses left)."
                   .format(int(guess),guesses)).casefold()
    guesses -= 1
    if answer == "h":
        # Guess higher. 1 higher than the guess will be lower bound of range
        low = guess + 1
    elif answer == "l":
        # Guess Lower. 1 lower than the guess will be upper bound of range.
        high = guess - 1
    elif answer == "c":
        print("I got it in {} guesses!".format(10-guesses))
        break
    else:
        print("Please enter h,l or c.")
        guesses += 1
else:
    print("The number is = {} .".format(int(low)))
    print("I guessed it in {} times".format(10-guesses))


# More on else clause in a loop

numbers = [1, 9, 17, 41, 81]
# Bu listenin içerisinde 8'e bölünen sayı olup olmadığını kontrol edelim.

for number in numbers:
    if number%8 == 0:
        #reject the list.
        print("There is a number that divides by 8. List is unacceptable.")
        break
else:
    print("All numbers are fine. The list is acceptable.")
