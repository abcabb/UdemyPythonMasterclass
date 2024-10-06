parrot = "Norwegian Blue"

for character in parrot:
    print(character)

# number = "9,465;512:678 147,622;359"
# seperators = number[1: :4]

# Yukarıda slice işlemini biliyorsun. İstediğimiz karakterleri sıralı olduğu için bu şekilde alabiliriz. Ama girdiyi bir kullanıcı girecekse
# bu şekilde düzenli olacağına güvenemeyiz. Dolayısıyla string'in her bir karakterini examine etmek zorundayız. Her karakter için bir digit mi değil mi bakmalıyız.

#number = "9,465;512:678 147,622;359"
#Eğer use input yaparsak
number = input("Please enter a series of numbers, using seperators you'd like to.")
seperators = ""

for char in number:
    if not char.isdigit(): ##ya da " if not char.isnumeric() "
        seperators += char

print(seperators)

values = "".join(char if char not in seperators else " " for char in number).split()
print([int(val) for val in values])
print("The sum = {}".format(sum(int(val) for val in values)))
#This is still a little advanced.

#Range function

for i in range(1,20): # Range function starts from 1 to 20 but not including last item ust like strings
    print("i is now {}".format(i)) # So output will be from 1 to 19.

for i in range(5): # Eğer başlangıç değeri vermezsen default olarak = 0 dan başlar.
    print("i is now {}".format(i))

# Step Value in Ranges (bunun için başlangıç değeri belirtmek zorundasın.)

#for i in range(10,2) Burada step value default olarak +1 olduğu için 10'dan 2 ye artarak hiçbir zaman gidemez. Dolayısıyla output boş olur.

for i in range(5,0,-1):
    print("i is now {}".format(i))

for i in range(0, 12, 2):
    print(i)

#Different use of range :

# if age>=16 and age<=65 = if age in range(16,66)
age = 45
if age in range(16,66):
    print("Have a good day at work.")

# Timestable with Inner Loops

for i in range(1,11):
    for j in range(1,11):
        print("{} times {} = {}".format(i,j,i*j))
    print("-"*50)

# Continue Keyword
shoppingList = ["Milk", "Bread", "Juice", "Spam", "Eggs", "Meat"]

for item in shoppingList:
    if item != "Spam":
        print("Buy " + item)

print()

for item in shoppingList:
    if item == "Spam":
        continue
    print("Buy " + item)

# Break Keyword

itemToFind = "Weapon"
foundAt = None      # None expression is equvailent to Null from Java and C#.

# for item in range(0,6,1) ifadesine eşittir.
# for index in range(len(shoppingList)):
#     if shoppingList[index] == itemToFind:
#         foundAt = index
#         break

if itemToFind in shoppingList:
    foundAt = shoppingList.index(itemToFind)
# Bu da youkarıdaki kod ile aynı işi yapar.

if foundAt != None:
    print("Item found at {} index".format(foundAt))
else:
    print("Item doesn't exist.")

# While Loop

i=0
while i<10:
    print("i is {}".format(i))
    i+=1

# Adventure Game

availableExits = ["north", "south", "east", "west"]

chosenExit = ""

while chosenExit not in availableExits: # Şartı sağladığı sürece while bloğunda kalır.
    chosenExit = input("Enter an exit direction: ").casefold()
    if chosenExit == "quit":
        print("Game Over")
        break   # Yani, eğer break keyword'u okursa else statement'ına girmeden döngüden çıkar.
else: # While döngüsü şartını sağlamadığı zaman else bloğuna gelir.
    print("Arent you glad you got out of there")
