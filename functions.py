def multiply(x: float,y: float) -> float:
    # Docstring Use:
    """Multiples two values

    You can enter two sequence types. It can be `int` or `string`

    :param x: The first value the user enters to multiply
    :param y: The second value  the user enters to multiply
    :return: Returns the multiplication of two values user entered.
    """
    result = x * y
    return result


def is_palindrome(string):
    """Takes a string and checks if its reverse is equal to itself or not.

    A palindrome is a string that readable as the same forwards as backwards.

    :param string: The string that is going to be reversed.
    :return: returns a `boolean` value. `True` for palindrome, `False` for not Palindrome.
    """
    # reversed_string = string[::-1]
    # return reversed_string == string
    return string.casefold() == string[::-1].casefold()

# Docstring bakmannın başka bir yolu :

print(input.__doc__)
print("*" * 80)
print(multiply.__doc__) # Docstring'in fonksiyonun içinde olmasının başka bir sebebi
print("*" * 80)

# Başka bir yolu

help(multiply)

# The convention is 2 blank lines before and after a function according to python-style-guide pep-8
answer = multiply(2.5,5)
print(answer)

answer = multiply("-",50)
print(answer)

for i in range(1,5):
    answer = multiply(2,i)
    print(answer)

string1 = input("Please enter a string: ")
if is_palindrome(string1):
    print("{} is a palindrome.".format(string1))
else:
    print("{} is not a palindrome.".format(string1))

# PALINDROME SENTENCE CHALLANGE
letters = "abcdefghijklmnopqrstuvwxyz" # sadece harfleri karsilastirmak istiyoruz.


def is_palindrome_sentence(input_sentence):
    pure_sentence = ""
    for char in input_sentence.casefold():  # Burada .casefold() kullanmazsan kod çalışmaz.
        if char in letters:
            pure_sentence += char
        else:
            continue
    print(pure_sentence)
    return pure_sentence == pure_sentence[::-1]


sentence1 = input("Please enter your sentence: ")
if is_palindrome_sentence(sentence1):
    print("{} is a palindrome sentence.".format(sentence1))
else:
    print("{} is not a palindrome sentence.".format(sentence1))


# Teacher's Solution - .isalnum() Method

# .isalpha() metodu sadece karakter içeren stringler için çalışır
# .isalnum() metodu hem karakter hem digit içeren stringler için de çalışabilir.
# alnum = alpha numeric - burdan aklında kalsın. alpha sadece harfler.


def is_palindrome_sentence2(input_sentence):
    """Checks if a sentence is a palindrome or not.

    This function takes the sentence and concats it's every letter character.
    Then compares to its reverse to understand they are equal or not.

    :param input_sentence: String input that the user enters.
    :return: Returns `True` or `False` values depending on if its palindrome or not.
    """
    pure_string = ""
    for char in input_sentence:
        if char.isalnum():
            pure_string += char
    print(pure_string)
    return is_palindrome(pure_string)
    # Aynı kodu kopyalama. Fonksiyonu kullan


sentence2 = input("Please enter your sentence: ")
if is_palindrome_sentence2(sentence2):
    print("{} is a palindrome sentence.".format(sentence2))
else:
    print("{} is not a palindrome sentence.".format(sentence2))


# Eğer bir fonksiyon bir değer döndürmezse default olarak "None" değerini döndürür.


def return_none():
    0


answer = return_none()
print(answer)

# Banner oluşturma fonksiyonu


# def banner_text(text):
#     screen_width = 50
def banner_text(text : str = " ", screen_width : int = 80) -> None: # return type any = herhangi bir şey. None = hiçbirşey.
    """Appears a string between two asteristk at each end of our screen width.

    If you enter an asterisk "*" it will write whole asterisk series for row.
    If you enter a text it will center the text and put two asterisks around.

    :param text: Your message.
    :param screen_width: Maximum size of screen.
    :raises ValueError: If your message exceeds the limits of empty place.
    """
    if len(text) > screen_width:
        # print("Your text is too long to insert in banner!")
        raise ValueError("{0} too large for specified width {1}"
                         .format(text, screen_width))  # Neyin hatalı olduğunu belirtiyoruz. Ve program duruyor.
    if text == '*':
        print("*"*screen_width)
    else:
        print("**{}**".format(text.center(screen_width-4)))


banner_text("*", 66)    # Positional use
banner_text("Always look on the bright side of life...", 66)
banner_text("If life seems jolly rotten,", 66)
banner_text("There's something you've forgotten!", 66)
banner_text("And that's to laugh and smile and dance and sing,", 66)
banner_text(screen_width = 66)  # Keyword use
banner_text("When you're feeling in the dumps,", 66)
banner_text("Don't be silly chumps,", 66)
banner_text("Just purse your lips and whistle - that's the thing!", 66)
banner_text("And... always look on the bright side of life...", 66)
banner_text("*", 66)

# Fibonacci Function


def fibonacci(n: int = 10) -> int: # Bu tarz bir annotation'da equal'ın her iki tarafına da boşluk bıraklımalı.
    """Returns the `n` th number of our fibonacci series of `n` characters."""
    if 0 <= n <= 1:
        return n
    else:
        n_minus1 = 1
        n_minus2 = 0

        result = None

        for i in range(1,n):
            result = n_minus1 + n_minus2
            n_minus2 = n_minus1
            n_minus1 = result

        return result


for i in range(20):
    answer2 = fibonacci(i)
    print(i, answer2)

# Printing Color
# Some ANSI escape sequences for colours and effects
BLACK = '\u001b[30m'
RED = '\u001b[31m'
GREEN = '\u001b[32m'
YELLOW = '\u001b[33m'
BLUE = '\u001b[34m'
MAGENTA = '\u001b[35m'
CYAN = '\u001b[36m'
WHITE = '\u001b[37m'
RESET = '\u001b[0m'

BOLD = '\u001b[1m'
UNDERLINE = '\u001b[4m'
REVERSE = '\u001b[7m'

print(RED, "This will be in Red color.")
print("and so is this.")
print(RESET, "Now, it is back to normal")


def colour_print(text: str, effect: str) -> None:
    """
        Print "text" using ANSI sequences to change colour, etc
    :param text: The text to print
    :param effect: The effect we want
    """
    # output = "{0}{1}{2}".format(effect,text,RESET)
    # print(output)
    print("{0}{1}{2}".format(effect,text,RESET))

colour_print("I want this to be blue", BLUE)
colour_print("This is underline", UNDERLINE)
colour_print("This is reversed color", REVERSE)
