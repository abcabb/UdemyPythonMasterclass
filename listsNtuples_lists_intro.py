# Lists Intro

computer_parts = ["computer", "monitor", "keyboard", "mouse", "mouse mat"]

for part in computer_parts:
    print(part)

print()
print(computer_parts[2])

print(computer_parts[0:3])
#Slicing a list creates another list.
print(computer_parts[-1])
#Same old negative indexing.
#Note : While strings are immutable, lists are mutable.

print("-" * 50)
# Immutables' Logic, id() function

result = True
another_result = result
print(id(result))
print(id(another_result))
# İkisinin de adresi aynı gözükür çünkü, aynı Boolean değerini bind ettiler.

result = False
print(id(result))
#Boolean değeri değişmiş olmadı. Sadece result farklı bir boolean değerini bind ediyor.
print("-" * 20)

result = "Correct"
another_result = result
print(id(result))
print(id(another_result))

result += "ish"    # result  = (result + "ish" (yeni değer)) başka adresteki yeni str.
print(id(result))

# Mutable Logic, .append() function

shopping_list = ["milk",
                 "pasta",
                 "eggs",
                 "spam",
                 "bread",
                 "rice"]

another_list = shopping_list
print(id(another_list))
print(id(shopping_list))

shopping_list += ["cookies"]
print(shopping_list)
print(id(shopping_list))
print(another_list)     # Buraya kadar şuan 1 tane liste var. Sadece 1 tane.

a = b = c = d = e = f = shopping_list
print(a)
print(b)

print("Adding cream to our list")
d.append("Cream")
print("Adding fish to our list")
f.append("Fish")
print(e)

# Hala sadece tek bir listemiz var. Aynı adreste. Bütün değişkenler onu bind ediyor.
# Ve hepsi onu güncelleyebilir. Çünkü lists are mutable.

print("-"*50)

# Number Lists,Functions : (min()-max(),.count())

even = [2,4,6,8]
odd = [1,3,5,7,9]

print(min(even))
print(min(odd))
print(max(even))
print(max(odd))

print()
print("mississippi".count("s"))
print("mississippi".count("iss"))
print("mississippi".count("issi"))

print("-"*50)
# Enumerable Example

for index, character in enumerate("abcdefg"):
    print(index , character)


print("-"*50)
# Important Example, String Comprehension Method

available_parts = ["computer",
                   "monitor",
                   "keyboard",
                   "mouse",
                   "hdmi cable",]

valid_choices = []
# String Comprehension Method
# valid_choices = [str(i) for i in range(1, len(available_parts)+1)] Output : ['1', '2', '3', '4', '5', '6']

#There is a better way than string comprehension to do that :

for i in range(1, len(available_parts)+1):
    valid_choices.append(str(i))
print(valid_choices)

current_choice = "-"
computer_parts2 = [] # We created an empty list.

while current_choice != "0":

    # if current_choice in "123456": Bunun yerine;
    if current_choice in valid_choices:
        print("{} added to the list.".format(current_choice))
        index_of_chosen = int(current_choice) - 1
        chosen_part = available_parts[index_of_chosen]
        computer_parts2.append(chosen_part)

        # if current_choice == "1":
        #     computer_parts2.append("computer")
        # elif current_choice == "2":
        #     computer_parts2.append("monitor")
        # elif current_choice == "3":
        #     computer_parts2.append("keyboard")
        # elif current_choice == "4":
        #     computer_parts2.append("mouse")
        # elif current_choice == "5":
        #     computer_parts2.append("mouse mat")
        # elif current_choice == "6":
        #     computer_parts2.append("hdmi cable")

    else:
        print("Please add options from the list below:")

        # print("1: computer")
        # print("2: monitor")
        # print("3: keyboard")
        # print("4: mouse")
        # print("5: mouse mat")
        # print("6: hdmi cable")
        # print("0: to finish")

        # Bu kod yerine :

        # for part in available_parts:
        #     print("{}: {}".format(available_parts.index(part)+1 , part))

        # Even tough, this is not so efficcient way to list items.
        # Because when you deal with huge list it's not efficient to look every item and their indexes.
        # We have much more efficient way to do this in Python : Enumerate Function.
        # Enumerate returns each item with its index position :

        for number, part in enumerate(available_parts): # enumerate fonksiyonu pair of values verir (Yani değer çifti verir)
            print("{}: {}".format(number + 1 , part))   # ilk değişken index değerini, iknici de item(string) değerini alır.
        # Enumerate() herhangi bir iterable type ile kullanılabilir.

    current_choice = input()

print(computer_parts2)
