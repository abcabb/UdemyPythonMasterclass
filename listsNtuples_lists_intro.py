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
        index_of_chosen = int(current_choice) - 1
        chosen_part = available_parts[index_of_chosen]
        if chosen_part in computer_parts2: # for item remove from the list
            print("{} removed from the list.".format(current_choice))
            computer_parts2.remove(chosen_part)
        else:
            print("{} added to the list.".format(current_choice))
            computer_parts2.append(chosen_part)
        print("Your list now contains {}".format(computer_parts2))

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

# Sorting Lists:

evenn = [1,3,5,7,9]
odd = [0,2,4,6,8]

evenn.extend(odd)   # .extend() = Concatenate two lists
# contanete_lists = evenn + odd   bu da bir metoddur.

print(evenn)

digits_2 = sorted("467982135")

print(digits_2)

evenn.sort() # increase order ile sıralar
print(evenn)

evenn.sort(reverse=True) # reverse, sort fonksiyonunun içerisindeki bir argüman.
# Ona buradan değer atayarak ters listelemesini sağlarız.
print(evenn)
# Dikkat edersen yeni bir liste oluşturmadık. Bir listeyi düzenledik. (evenn listesi)
# Yeni oluşturan metodlar var ama, "sort metodu listeyi kopyalamaz! İçerisindeki itemleri düzenler."

# Listeler haricindeki şeyleri sıralamak için sorted() function
pangram = "The quick brown fox jumps over the lazy dog"

letters = sorted(pangram)
print(letters)
# Outputta space'leri en başta, sonrasında Capital harfleri, sonrasında da sırasıyla diğer harfleri gördük.
# Bunun sebebini biliyorsun ASCII ye göre sort edildikleri için.
# sorted function'u budur. İçerisine bir iterable verilir, fonksiyon da itemlerini listede sıralanmış olarak döndürür.
# Diğerlerinden farkı, yeni bir liste oluşturup onu döndürmesidir. Bu önemlidir.

numberss = [8.6, 4.3, 6.7, 2.5, 3.9, 7.8, 2.1]

sorted_numberss = sorted(numberss)
print(sorted_numberss)
print(numberss)     # Bu hala sort edilmemiştir çünkü sorted() fonksiyonu yeni liste oluşturdu bunu ellemedi.

# sorted() fonksiyonu yeni liste oluşturup liste döndürürken, sort hiçbir değer döndürmez. (None değeri döndürür)

new_numb_list = [6,2,5,9,1]

sorted_new_numb_list = new_numb_list.sort()
print(new_numb_list)    # Sort edilmiş liste
print(sorted_new_numb_list)  # None

# Bir literal'ı da sort edebiliriz

missing_letter = "abCgfed"  # String literal

print(sorted(missing_letter, key=str.casefold)) # key kısmı Capital Case insensitive olsun diye.

namess = ["Ali",
          "Veli",
          "ayşe",
          "fatma",
          "Omer"]

namess.sort()
print(namess)  # Case sensitive olduğu için büyük harfle başlayanlar önce sıralanır.
namess.sort(key=str.casefold)
print(namess)

print(sorted(namess))
print(sorted(namess, key=str.casefold))

# Using list to create a list from an iterable. (list bir fonksiyon değil, bir sınıf initializer'ıdır.)

digits_3 = list("648972153")

print(digits_3)  # Bir liste oluşur. Ama sırasız. Herhangi bir iterable için list() kullanarak liste oluşturabilirsin.

even2 = [1, 3, 5, 7, 9]
odd2 = [0, 2, 4, 6, 8]

concat_numbers = even2 + odd2
more_numbers = list(concat_numbers)

print(concat_numbers)
print(more_numbers)

print(concat_numbers is more_numbers)  # false
print(concat_numbers == more_numbers)  # true
# concat_numbers ve more_numbers eşitlerdir. Yani içeriklerindeki değerler aynıdır.
# Ama aynı liste değillerdir. Her iki liste de yeni oluşturulan listelerdir.

# Aynı listeden yeni bir tane oluşturmanın başka bir yöntemi : slice

more_numbers2 = concat_numbers[:]
print(more_numbers2)
print(more_numbers2 is concat_numbers)  # false

# Bir liste kopyalamanın En iyi yolu .copy() metodu.

more_numbers3 = concat_numbers.copy()
print(more_numbers3)
print(more_numbers3 is concat_numbers)  # false

new_list = ["computer", "monitor", "keyboard", "mouse", "mouse mat"]
print(new_list)

new_list[3] = "trackball"
print(new_list)

new_list[4:] = "mouse"  # Bir iterable atadık, tek tek itemlerini listeye ekler.
print(new_list)

new_list[-1::1] = ["mouse mat"]  # Bu şekilde bir liste içerisinde ilettiğimiz için iterable'ın item'ı string dir ve tek bir string olarak eklenir.
print(new_list)

data1 = [4, 5, 101, 108, 132, 142, 165, 182, 188, 192,
         205, 255, 265, 274, 291, 380, 390]
# print(data1)
# del data1[0]
# print(data1)
# del data1[1]
print(data1)
min_valid_number = 100
max_valid_number = 200

for index, item in enumerate(data1):  # Doğru çalışmaz çünkü listeden her eleman silindiği zaman index değerleri değişir.
    if (item<min_valid_number) or (item>max_valid_number):
        del data1[index]
# Iterate ettiğin object'in size'ını değiştirirken sorular yaşarsın.

print(data1)

# Safely removing values from a list

data2 = [4, 5, 101, 108, 132, 142, 165, 182, 188, 192,
         205, 255, 265, 274, 291, 380, 390]

stop = 0
for index, value in enumerate(data2):
    if value >= min_valid_number:
        stop = index
        break

print(stop)
del data2[:stop]  # Bu şekilde 100'den küçük değerleri silebiliriz. (data sıralı olduğu için)
print(data2)

# Üst değerleri silelim

start = 0
                #  Başlangıç   , bitiş (dahil olmadığı için bir azalttık, artış miktarı
for index in range(len(data2)-1, -1, -1):  #  range fonksiyonu slice mantığıyla çalışmaz.
    print(index)
    if data2[index] <= max_valid_number:
        stop = index + 1
        break

del data2[stop:]  # Bu sayede 200'den büyük sayıları sildik.
print(data2)

# Removing Items From a List backwards

data3 = [103,185,174,308,164,189,3,142,
         112,4,101,394,192]
min_valid_number = 100
max_valid_number = 200

for index in range(len(data3)-1, -1, -1):
    if data3[index] < min_valid_number or data3[index] > max_valid_number:
        print(index)  # Beklediğimiz değerleri aldık. 11 - 9 - 6 - 3
        del data3[index]

print(data3)

# Peki for ile düzgün çalışan bu kod enumerate ile neden indexleri atladığı için doğru çalışmıyor?
# Çünkü elemanları tersten siliyoruz. Bir eleman silindiği zaman sadece ondan sonrakilerin index değerleri değişir.
# Öncesindeki itemlerin indexleri aynı olduğundan, silinme işlemi loop'u bozmaz.

# Enumerate ile şu şekilde yapabiliriz :

data4 = [103,185,174,308,164,189,3,142,
         112,4,101,394,192]

last_index = len(data4)-1
for index, value in enumerate(reversed(data4)):
    if value < min_valid_number or value > max_valid_number:
        print(last_index - index, value)
        del data4[last_index - index]  # Amacımız listeye baktığında liste üzerinden tersten siliyor olmak.

print(data4)

# Aynı problem için farklı bir yaklaşım :

data5 = [103,185,174,308,164,189,3,142,
         112,4,101,394,192]

last_index = len(data5) - 1
for index, value in enumerate(data5[::-1]):
    if value < min_valid_number or value > max_valid_number:
        print(last_index - index, value)
        del data5[last_index - index]

print(data5)

# Time

# BUNLARIN ARASINDA RUNTİME'I EN İYİ OLAN SORTED LİST'İ SIRALAYANLARDIR.
# Bunun sebebi o yöntem tekte silerken, diğerleri tek tek bakıp siliyor.
# DAHA SONRASINDA ENUMERATE FONKSİYONUNU KULLANANLAR DAHA VERİMLİ.
# EN VERİMSİZİ İSE RANGE FONKSİYONU İLE ELEMAN SİLEN.

# 10 MİLYON ELEMANIN OLDUĞU LİSTELERİN OUTPUTUNU GÖREBİLMEK İÇİN
# SIRALANMIŞ OLARAK YAPTIĞIMIZ METOD 1 SANIYENIN ALTINDA IKEN,
# ENUMERATE METODUYLA 9 SANİYEDE SONUCU ALDIK.  Daha çok veri için daha da verimsiz.


# Nested Lists

even3 = [2,4,6,8]
odd3 = [1,3,5,7,9]

number_lists1 = [even3,odd3]  # 2 Lists inside of a List.
print(number_lists1)

# Bunu göstermek için:

for number_list in number_lists1:
    print("-"*50)
    print(number_list)
    print("-"*50)

    for value in number_list:
        print(value)

#  How to write list due to PEP-8 :
# İlk eleman bir enter sonrasına yazılır. Son square bracket de altta yazılır. Hepsi 4 satır atlanarak alt alta

menus1 = [
    ["egg", "bacon"],
    ["egg", "sausage", "bacon"],
    ["egg", "spam"],
    ["egg", "bacon", "spam"],
    ["egg", "bacon", "sausage", "spam"],
    ["spam", "bacon", "sausage", "spam"],
    ["spam", "sausage", "spam", "bacon", "spam", "tomato", "spam"],
    ["spam", "egg", "spam", "spam", "bacon", "spam"], # Son virgul genelde redundant'dır. Ama koyması edit işini kolaylaştırır.
]  # Ornegin google style guide'ı o son virgulu koymayı onerir.

# Doğru yazım bu şekilde olmalıdır.

for menu_list in menus1:
    if "spam" not in menu_list:
        print("-"*10)
        print(menu_list)
        print("-"*10)

        for value in menu_list:
            print(value)

    else:
        print("{} has spam score of {}"
              .format(menu_list, menu_list.count("spam")))

# Challange : Print out all the menus on the list with spam removed.

menus2 = [
    ["egg", "bacon"],
    ["egg", "sausage", "bacon"],
    ["egg", "spam"],
    ["egg", "bacon", "spam"],
    ["egg", "bacon", "sausage", "spam"],
    ["spam", "bacon", "sausage", "spam"],
    ["spam", "sausage", "spam", "bacon", "spam", "tomato", "spam"],
    ["spam", "egg", "spam", "spam", "bacon", "spam"],
]

for menu_list in menus2:
    if "spam" not in menu_list:
        print("-"*10)
        print(menu_list)
        print("-"*10)

        for value in menu_list:
            print(value)

    else:
        last_index_of_current_list = len(menu_list) - 1
        for index, value in enumerate(reversed(menu_list)):
            if value == "spam":
                print("index: {}  value: {}  is deleted".format(index,value))
                print("-"*20)
                del menu_list[last_index_of_current_list - index]  # Bu döngü sonucu her listedeki spamlerin hepsi silinecek

i=1
for menu_list in menus2:
    print("Menu-{}".format(i))
    i+=1
    print(menu_list)    # Menuleri tek tek sıralayıp listeler.

# Teacher's Solution to this challange
menus4 = [
    ["egg", "bacon"],
    ["egg", "sausage", "bacon"],
    ["egg", "spam"],
    ["egg", "bacon", "spam"],
    ["egg", "bacon", "sausage", "spam"],
    ["spam", "bacon", "sausage", "spam"],
    ["spam", "sausage", "spam", "bacon", "spam", "tomato", "spam"],
    ["spam", "egg", "spam", "spam", "bacon", "spam"],
]

print("---"*20)

for list in menus4:
    for item in list:
        if item != "spam":
            print(item)
    print()

print("---"*20)

menus3 = [
    ["egg", "bacon"],
    ["egg", "sausage", "bacon"],
    ["egg", "spam"],
    ["egg", "bacon", "spam"],
    ["egg", "bacon", "sausage", "spam"],
    ["spam", "bacon", "sausage", "spam"],
    ["spam", "sausage", "spam", "bacon", "spam", "tomato", "spam"],
    ["spam", "egg", "spam", "spam", "bacon", "spam"],
]

for list in menus3:
    for index in range(len(list)-1, -1, -1):
        if list[index] == "spam":
            del list[index]

    print(list)

# İf we want to format the way how output is. (Default list format is inside of square brackets [])


# Function's Signatures
# Print Function
print()

name = "Semi"
age = "8"
print(name, age, "Python", 2024)
# Fonksiyon definition'da " *objects " vardı. Buradaki asterisk(star) birden fazla value sağlanabileceğini belirtir.
# Biz de bu sayede 4 tane değişken fonksiyon içerisine girebildik.

# "sep" parameter in print()

print(name, age, "Java", 2022, sep=" ,") # sep default olarak (sep = " ") dir.
# Output : Semi ,8 ,Java ,2022

# "end" parameter in print()

for i in range(1,11):
    print(i)

for i in range(1,11):
    print(i, end = " - ") # end default olarak (end = \n) dır.
# Output : 1 - 2 - 3 - 4 - 5 - 6 - 7 - 8 - 9 -

# THE .join() METHOD
print(end = "\n\n")
# print() fonksiyonu, içerisine bir list konduğunda default olarak
# ['item1','item2','item3'] olarak gösterir. Bu tırnakları ve parantezleri düzenleyebiliriz.

instance_list = [
    "item1",
    "item2",
    "item3"
]

print(instance_list)  # Output : ['item1', 'item2', 'item3']
print(", ".join(instance_list))  # Output : item1, item2, item3

# .join() metodu, bir iterable'ın item'larını tek tek alır. Ve join ettiği şey ile onları ayırır. Bu kadar.

ornek_seperator = " *|* "
seperated_list = ornek_seperator.join(instance_list)

print(seperated_list)  # Output : item1 *|* item2 *|* item3

string_1 = "thisisastirng"
seperator1 = " | "
print(seperator1.join(string_1))  # String iterable'ının itemlerinin arasına koyar (harflerin).

# .join , str class'ının bir metodudur. Bir iterable'ı iterate eder, her bir ogesinin arasına string koyar ve yeni bir string oluşturur.

# Not : eğer itemleri .join() etmek istiyorsan
# Bütün elemanlar STRING olmak zorundadır.

instance_list2 = ["1, 3, 5", "265", 8]

print(instance_list2)  # Output : ['1, 3, 5', '265', 8]
# " | ".join(instance_list2) Runtime type error. Çünkü listede integer var. Yani listeler homogenous olmalı.

# THE .split() METHOD - Opposite of .join() method for strings.

# The split method splits a string up into "words". (kelimelere bölüyo)

pangram = "The quick\n brown fox jumps over\t the lazy dog"

word_list = pangram.split()

print(word_list)  # Output : ['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog']

# .split() fonksiyonunda "sep" keywordu

# Bu keyword string'de kelimeleri hangi değerin ayıracağını belirler. Default olarak sep = ' ' (1 space karakter) dir.

instance_string = "HelloxThisxIsxAnxInstancexString"

word_list2 = instance_string.split(sep = 'x')

print(word_list2)

instance_string2 = "5,923,484,824,321,674"

word_list3 = instance_string2.split(",")

print(word_list3)

generated_list = ['9', ' ',
                  '2', '2', '3', ' ',
                  '3', '7', '2', ' ',
                  '0', '3', '6', ' ',
                  '8', '5', '4', ' ',
                  '7', '7', '5', ' ',
                  '8', '0', '7']
values = "".join(generated_list)
print(values)
values_list = values.split()
print(values_list)

# CHALLANGE

# Use a for loop to produce a list of ints, rather than strings.
# You can either modify the contents of the 'values_list' list in place,
# or create a new list of ints.

# Lets modify the "values_list" list.

new_list = []
for item in values_list:
    print("{} added to the list as an integer".format(item))
    new_list.append(int(item))
print(new_list)

# Teachers solutions
print(values_list)
for index in range(len(values_list)):
    values_list[index] = int(values_list[index])  # Buradaki hatayı ignore edebiliriz. Çünkü yapmak istediğimiz şey string içeren listeye int atamak.
print(values_list)


# Onemli bir kod. Yaptığım bir hata :

number_list2 = "7,5,-1".split(',')  # Liste oluşturduk
print(number_list2)

for index, item in enumerate(number_list2):
    number_list2[index] = int(item)  # integer'a çevirdik

result = 0 # YAPTIĞIM HATA :
# for i in range(len(number_list)):
#     result += number_list[i]
# else:
#     result -= number_list[i]
# Olmaz çünkü for döngüsünde range(2) i=2 asla olmaz. Else bloğuna geçtiğinde i=1'dir.

i=0
while(i != len(number_list2)-1):
    result += number_list2[i]
    i += 1
else:
    result -= number_list2[i]

print(result)
