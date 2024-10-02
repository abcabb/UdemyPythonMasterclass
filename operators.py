a = 12 # 12 -- expression
b = 3 # 3 -- expression
# Bu, assignment to variables işlemi değildir!
# Python, da asign edilmez, bind işlemi yapılır. İki tane variable (label) binding yaptık (değerlere).
#Not : (b =), (a =) birer expression değillerdir. Expression, hesaplanabilir olup sonuç döndürmesi lazım. Sabit sayılar ve işlem sonuçları gibi.
#Başka bir deyişle : You can't have an expression on the left of an assignment.
#The expression on the right of the equals sign is evaluated, and the variable on the left is bound to the result.

print(a + b)    #15 / (a), (b), (a+b) -- expression
print(a - b)    #9 / (a), (b), (a-b) -- expression
print(a * b)    #36 / (a), (b), (a*b) -- expression
print(a / b)    #4.0 / (a), (b), (a/b) -- expression
print(a // b)   #4 (Integer Division) (Aslında sonucu en küçüğe yuvarlar. Yani küsüratı sonuçta göstermez.) / (a), (b), (a//b) -- expression
print(a % b)    #0 / (a), (b), (a%b) -- expression

print()


#for i in range(1,a/b):
#    print(i)
#TypeError: 'float' object cannot be interpreted as an integer

#Bu kod çalışmaz. Python Strongly Typed bir dildir. "int" olması gereken yere "float" koyamazsın.

for i in range(1, a//b): # (1), (a//b), (range(1, a//b)) -- expression
    print(i)            # (i) -- expression
#Not: (i=) expression değildir.
# Expressions
#Expression is anything that can be calculated to return a value.
#And expressions itself can be made up of expressions.
#Neyin expression olup olmadığını yukarıdaki kodda belirttim.
