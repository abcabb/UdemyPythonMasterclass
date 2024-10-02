print('I love "learning" python.')
print("I love 'learning' python.")
# Eğer "" tırnak ile string literal'i enclose edeceksen, içerisinde '' kullan. Eğer '' ile enclose edeceksen içerisinde "" kullan.
print("concatenate" + " strings")

variable1 = "Hello "
variable2 = input("Say World : ")

print(variable1 + variable2)

# Escape Characters (backslash)

splitString = "This string has been \nsplit \nover several \nlines."
print(splitString)
tabbedString = "1\t2\t3\t4\t5"
print(tabbedString)

print('The petshop owner said "No, No, it\'s not for sale\'s.". Then we moved on')
# '' İçerisinde '' kullanmak istesen \ kullanman lazım
#aynı şekilde :
print("The petshop owner said \"No, No, it's not for sale's.\". Then we moved on")
# "" İçerisinde "" kullanmak istesen \ kullanman lazım
#Ama """ """, yani triple quotes kullanırsan, "" ve '' kullanabilirsin.
print("""The petshop owner said "No, No, it's not for sale's." Then we moved on""")
#Ayrıca, triple quotes içerisinde new line'a geçersen outputta da yle gzükür. Ama geçtiğin halde satır sonuna backslash koyarsan outputta new line olmaz.
anotherSplitString = """These are  
some separate 
lines here."""
print(anotherSplitString)
anotherSplitString2 = """These are \
some separate  \
lines here.??""" ##hayır bitişik.
print(anotherSplitString2)

#More Escaping Characters On Strings
# print("C:\Users\timbuchalka\notes.txt") bu şekilde yazamıyoruz. Çünkü \n, \t gibi special character'lerden kaçmamız (escape) lazım.
# Bunun için iki yol var : raw string kullanmak veya backslash'ten backslash ile kaçmak:
print(r"C:\Users\timbuchalka\notes.txt") #raw string
print("C:\\Users\\timbuchalka\\notes.txt") #outputta \ görmek için \\yazman lazım.

# Variables in Python

# Python is "Dynamically Typed" and "Strongly Typed" language. Lest See what that means :

#Python'da type'ı variable'lar değil de, daha çok value yani değerler alır. Variable'ların type'ı olmaz. Sadece o anda işaret ettiği value type'ı her ne ise
# onun da type'ı o olur.

age = 24 # integer
print(age)
print(type(age))

age = "2 years" #string
print(age)
print(type(age))

name = "Ali"
age = 24 #integer
age_in_words = "2 years"
# print(name + " is " + age + " years old.")
# TypeError alırız. TypeError : can only concatenate str to str. Not str to int.
#Python, + ile string verilmişse concat, iki int verilmişse işlem yapacağını bilir. Ama bir str bir int ile ne yapacağını bilemez.

#Java gibi bazı diller int'ları string lerle toplayınca string e çevirip concat işlemi yapabiliyor. Python bunu yapmaz.
#Bu Automatic Type Conversion işlemi bazı kolaylıkları olsa da, bug fixing işlemini zorlaştırıyor diyebiliriz.
