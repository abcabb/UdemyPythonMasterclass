string1 = "He's "
string2 = "probably "
string3 = "pining "
string4 = "for the "
string5 = "fjords."

print(string1 + string2 + string3 + string4 + string5)

print("He's " "probably " "pining " "for the " "fjords.") # String concatenate için + kullanmana gerek yok. Bu python'un bir özelliğidir.

print("Hello " * 5)

# print("Hello " * 5 + 4) # Type Error. Operator precedence gereği ilk olarak çarpım işlemi yapılır. Ama çarpım sonucu bir string ile bir integer toplanamaz.

print("Hello " * (5+4)) # Bu olur.

# Is a Substring part of another String ?

today = "Friday"

print("day" in today)   #True
print('Fri' in today)   #True (Not: Capital letter fark eder!)
print('wed' in today)   #False
print('fjord' in today) #False

# String Replacement Fields

age = 24
# Bu integer'ı string'lerle birlikte concatenate edip göstermek için

# "Coerce" an int to a string.
print("Hello, i am " + str(age) + " years old.")

# Dot Format Method
print("Hello, i am {0} years old.".format(age))
# Bu da aynı sonucu üretecektir ama integer i string olmaya coerce etmediğimiz için daha verimli. Çünkü öbür yol çok meşakkatli. Tek tek yapmak gerek.
print("There are {0} days in a week : {1}, {2}, {3}, {4}, {5}, {6}, {7}."
      .format(7, "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"))
# .format içerisindeki fieldlar sıralarına göre {0}, {1}, {2}.. gibi yerleşirler. Ama tabii, string içerisindeki süslü parantezler sıralı olmak zorunda değiller.
# ve birden fazla defa kullanılabilirler.
print("{0} {0} {5} {2}".format("Ali", "Veli", "Ayşe", "Fatma", "Sakine", "Mehmet"))
print("{} {:<5} {:10} {:<10}".format("Ali", "Veli", "Ayşe", "Fatma", "Sakine", "Mehmet"))
#Fieldlara rakam koymazsan sıralı kullanmak zorundasın. Bunları da format edebilirsin.

# .format()'in field'larına herhangi bir expression yazabilirsin. Int, string, çarpma işlemi, bölme işlemi vs...
for i in range(1,6):
    print("{0} squared is {1} and cubed is {2}".format(i, i ** 2, i ** 3))
#Bu output formatını daha güzel bir şekilde gösterebiliriz.
print()
for i in range(1,6):
    print("{0:1} squared is {1:2} and cubed is {2:3}.".format(i, i ** 2, i ** 3))
# Formatı solda sıranacak şekilde ayarlamak için
print()
for i in range(1,6):
    print("{0:1} squared is {1:<2} and cubed is {2:^3}.".format(i, i ** 2, i ** 3))
#"<" sembolü kullanırız.
# Ortalamak için "^" sembolü kullanırız.

print("pi is approximately {0:12}".format(22/7)) # Burada anlamadığımız bir şey yok. ':12' sadece format(sağa sola kaydırmak) için.
# Default olarak 15 decimal gösteriyor. (virgülden sonra küsürat 15 rakam)
print("pi is approximately {0:12f}".format(22/7)) # 12 yanına 'f' koyduk. 'f' kullanarak virgüllü bir sayı belirttiğimizde,
# Default olarak decimal pointten sonra 6 sayı alıyoruz.
#Aşağıdaki satırlar için ise, hala folating point format belirtiyoruz, 50 sayısını belirtiyoruz. Yani decimal point'ten sonra 50 sayı grürüyz.
# Yani '.f' default 6 gösteriyordu, biz '.50f' ile 50 gösterdik.
print("pi is approximately {0:12.50f}".format(22/7)) # 12 yanına '.50f' koyduk.
print("pi is approximately {0:52.50f}".format(22/7)) # 12'yi 52 olarak güncelledik. Ve yanına '.50f' koyduk.
print("pi is approximately {0:62.50f}".format(22/7)) # 12'yi 62 olarak güncelledik. Ve yanına '.50f' koyduk.
print("pi is approximately {0:72.50f}".format(22/7)) # 12'yi 72 olarak güncelledik. Ve yanına '.50f' koyduk.
#Not : ':12', ':52', ':72' gibi format düzenleyicilere "field with" diyebiliriz.
