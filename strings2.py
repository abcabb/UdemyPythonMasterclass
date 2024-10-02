parrot = "Norwegian Blue"

# print(parrot[14])
# Eğer bunu yazarsak index out of range error alırız. IndexError: string index out of range.

print(parrot[3])    # w
print(parrot[4])    # e
print(parrot[9])    #
print(parrot[3])    # w
print(parrot[6])    # i
print(parrot[8])    # n

# Negative Indexing In Strings

print()

print(parrot)

print(parrot[-1])   # e
print(parrot[-14])  # N
# print(parrot[-15])
# Eğer bunu yazarsak index out of range error alırız. IndexError: string index out of range.

print()

print(parrot[3 - 14])    # w
print(parrot[4 - 14])    # e
print(parrot[9 - 14])    #
print(parrot[3 - 14])    # w
print(parrot[6 - 14])    # i
print(parrot[8 - 14])    # n

# Slicing a String. Python Sequence Types, lets us to slice the sequence types.

print(parrot[0:6]) #Norweg. Her zamanki gibi 6. index dahil edilmiyor unutma.
print(parrot[3:5]) #we
print(parrot[:9]) # = print(parrot[0:9]).
print(parrot[:6] + parrot[6:]) #Nowegian Blue
print(parrot[:]) #Nowegian Blue

# print(parrot[-4 : 2])
# Böyle bir kod yazamayız. Çünkü -4 String'in sonlarındayken 2 başlarındadır. "Starting position" dan geriye doğru gidemezsin, ileri gitmek zorunlu.Çıktı gözükmez.
print(parrot[-4 : -2])
#Yazabilirsin çünkü squence'da starting position'dan ileri doğru gidiyor.
print(parrot[-14 : 14])

# A Step Value In Slices

print(parrot[0:6:2]) # Nre
print(parrot[0:6:3]) # Nw

number = "9,465,512,678,147,622,359"

print(number[1: :4]) # ( ,,,,,, ) output
# 0 indexinden başlamadığına dikkat et!

number = "9,465;512:678 147,622;359"
seperators = number[1: :4]  #( ,;: ,; ) output
values = "".join(char if char not in seperators else " " for char in number).split()
print([int(val) for val in values])
# Bu kısmı ileride işleyeceğiz, anlamak zorunda değilsin

letters = "abcdefghiklmnopqrstuvwxyz"

backwards = letters[25:0:-1]
print(backwards)            # output : zyxwvutsrponmlkihggfedcb

backwards = letters[25: -1 : -1]
print(backwards)            # output : boş olur. Çünkü -1 z demektir. ve son index dahil değildir. Yani z'den z'ye bile göstermez. Boş gösterir.

backwards = letters[25: :-1]
print(backwards)            # output : zyxwvutsrponmlkihggfedcba

backwards = letters[::-1]
print(backwards)            # output : zyxwvutsrponmlkihggfedcba
# Negatif step value kullandığımızda ve start ve end indexleri vermediğimizde python bu indexin sondan başa doğru başlayıp bittiğini biliyor.
# " : : -1" bir python idiom'udur(Şive, anlama tarzı diyebiliriz). Bunun gibi başka idiom'lar göreceğiz.

backwards = letters[1: 25 : -1]
print(backwards)            # Bu, hatalı gösterimdir. 99'dan geriye sayarak 100 sayısına ulaşamayız. Çıktı boştur.

#Challanges
#Output : qpo
backwards = letters[-10 : -13: -1]
print(backwards)

#Output : edcba
backwards = letters[4: : -1]
print(backwards)

#Output : last 8 characters in reverse order
backwards = letters[ : -9: -1]
print(backwards)
