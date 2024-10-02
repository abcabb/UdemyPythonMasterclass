a = 12
b = 3
# Bu, assignment to variables işlemi değildir!
# Python, da asign edilmez, bind işlemi yapılır. İki tane variable (label) binding yaptık (değerlere).

print(a + b)    #15
print(a - b)    #9
print(a * b)    #36
print(a / b)    #4.0
print(a // b)   #4 (Integer Division)
print(a % b)    #0

print()


#for i in range(1,a/b):
#    print(i)
#TypeError: 'float' object cannot be interpreted as an integer

#Bu kod çalışmaz. Python Strongly Typed bir dildir. range içerisinde int olması gereken yere float koyamazsın.

for i in range(1, a//b):
    print(i)
