t1 = "a", "b", "c"
print(t1)    # Output : ('a', 'b', 'c')
# Köşeli yerine yuvarlak parantezler tuple olduğunu gösterir.

t2 = ("a", "b", "c") # Aynı şey

print(id(t1))
print(id(t2))
# Aynı

name = "ali"
age = 12

print("abc", age, name)  # abc 12 ali
print(("abc", age, name))  # ('abc', 12, 'ali')
print(t1)  # ('a', 'b', 'c')

# Tuple parantezle tanımlanmasa da olur ama print içerisinde parantezle yazılmak zorunda

# Tuple'lar içerideki belirli elemanlara erişebilmek için indexin kullanılabilen bir sequence type'dır.
# List'den tek farkı tuple immutable'dır.
# Tuple use less memory than list.

print(t1[0])
print(t1[1])
print(t1[2])
# t1[1] = "d"  gives error

list1 = list(t1)
list1[0] = "z"
print(list1)

# Tuple kullanarak code integrity (bütünlük) koruyabilirsin. Kodda hatalar yapmanı immutable yapısı engeller.

a = b = c = d = e = f = 12  # Eğer 12'yi değişirsem bütün variable ların değeri değişir.

x, y, z = 1, 4, 13  # assignment'ın sağındaki ifade bir tuple'dır.
print(x)            # Sol tarafta tuple olmaz. Çünkü tuple immutable'dır.
print(y)
print(z)

tuple1 = 65,14,98
x, y, z = tuple1
print(x)
print(y)
print(z)

# Buna "Unpacking Tuple" denir.
# Aynı şekilde herhangi bir Sequence Type Unpack yapabiliriz.
# Unpacking a List:

list2 = [5, 10, 15]  # Listeye eleman ekler veya çıkarırsan code crash eder. Tupple kullanmak bu duruma engel olur.
q, p, r = list2
print(q)
print(p)
print(r)

# Enumerate fonksiyonu aslında güzel bir Tuple Unpacking örneğiydi.

for t in enumerate("abcdefgh"):
    print(t)

# enumerate() bir iterable'ın itemini ve index'ini tuple olarak alır ve t'ye atar.
# Eğer iki değişken koysaydık, tuple unpacking yapmış olur ve index değeri birine item değeri diğer değişken bind etmiş olurdu.
# şu anda  t = (0,'a'), (1,'b'), (2,'c') değerlerini alır.

# Tuple'ın daha okunabilir, daha anlaşılabilir olması için unpack etme :

table = ("Coffee Table", 200, 100, 75.5, 34)
print(table[1] * table[2])  # Bu bize masanın alanını verir ama index'lerle bu kodu yazmak çok zor.

name, length, weight, height, price = table
print(length * weight)

# A List containing tuples

albums = [("Welcome to my Nightmare", "Alice Cooper", 1975),
          ("Bad Company", "Bad Company", 1974),
          ("Nightflight", "Budgie", 1981),
          ("More Mayhem", "Emilda May", 2011),
          ("Ride the Lightning", "Metallica", 1984),
          ]  # Tuple olmaları için burada parantez şart.

print(len(albums))

for album, artist, year in albums:
    print("Album: {}  Artist: {}  Year: {}".format(album, artist, year))

# Böyle yapmamızın sebebi, biz buraya yeni bir album eklemek isteyebiliriz. Ama tuple'ların içerisine yeni bir şey ekleme
# şansımız daha az gibi gözüküyor. Dolayısıyla liste içerisinde tuple yapısı mantıklı.

# Tuple'a songs eklemek istersek. Songs bir tuple mı liste mi olmalı
# Eğer şarkılar belliyse, sonradan değişmiyceksen tuple iyidir. Tersi ise liste. Yani duruma göre seçeriz.

# Eğer şarkıların hem ismi hen de numarası olacaksa heterojen bir data demektir. (string ve int).
# Numaralar sonradan gelecek şarkıları vs değişirse liste iyidir. Ama heterojen data için tuple iyi.
# Sonuç olarak tuple içeren liste veya tuple içeren tuple kullanabiliriz.


albums2 = [
    ("Welcome to my Nightmare", "Alice Cooper", 1975,
     [
         (1, "Welcome to my Nightmare"),
         (2, "Devil's Food"),
         (3, "The Black Widow"),
         (4, "Some Folks"),
         (5, "Only Women Bleed"),
     ]
     ),
    ("Bad Company", "Bad Company", 1974,
     [
         (1, "Can't Get Enough"),
         (2, "Rock Steady"),
         (3, "Ready for Love"),
         (4, "Don't Let Me Down"),
         (5, "Bad Company"),
         (6, "The Way I Choose"),
         (7, "Movin' On"),
         (8, "Seagull"),
     ]
     ),
    ("Nightflight", "Budgie", 1981,
     [
         (1, "I Turned to Stone"),
         (2, "Keeping a Rendezvous"),
         (3, "Reaper of the Glory"),
         (4, "She Used Me Up"),
     ]
     ),
    ("More Mayhem", "Imelda May", 2011,
     [
         (1, "Pulling the Rug"),
         (2, "Psycho"),
         (3, "Mayhem"),
         (4, "Kentish Town Waltz"),
     ]
     ),
]

# She Used Me Up yazdırmak için :
print(albums2[2][3][3][1])

print()
for album, artist, year, songs_of_album in albums2:
    print("Album Name = {}\n"
          "Artist = {}\n"
          "Album Release Year = {}\n"
          "Songs : \n".format(album, artist, year))
    for number, name in songs_of_album:
        print("{}-) {}".format(number,name))
    print("\n"+"-"*50+"\n")

# JukeBox App Challange

jukebox_albums = [
    ("Welcome to my Nightmare", "Alice Cooper", 1975,
     [
         (1, "Welcome to my Nightmare"),
         (2, "Devil's Food"),
         (3, "The Black Widow"),
         (4, "Some Folks"),
         (5, "Only Women Bleed"),
     ]
     ),
    ("Bad Company", "Bad Company", 1974,
     [
         (1, "Can't Get Enough"),
         (2, "Rock Steady"),
         (3, "Ready for Love"),
         (4, "Don't Let Me Down"),
         (5, "Bad Company"),
         (6, "The Way I Choose"),
         (7, "Movin' On"),
         (8, "Seagull"),
     ]
     ),
    ("Nightflight", "Budgie", 1981,
     [
         (1, "I Turned to Stone"),
         (2, "Keeping a Rendezvous"),
         (3, "Reaper of the Glory"),
         (4, "She Used Me Up"),
     ]
     ),
    ("More Mayhem", "Imelda May", 2011,
     [
         (1, "Pulling the Rug"),
         (2, "Psycho"),
         (3, "Mayhem"),
         (4, "Kentish Town Waltz"),
     ]
     ),
]

# MY CODE BELOW !!!!

while True:
    print("Please choose your album (Invalid choose exits): ")
    album_name_number = 0
    for album in jukebox_albums:
        album_name_number += 1
        print("{}: {}".format(album_name_number,album[0]))
    album_choice = input()
    if int(album_choice) not in range(1, 1 + album_name_number):
        break
    print("Please choose your song: ")
    song_counter = 0
    for songs in jukebox_albums[int(album_choice)-1][3]:
        song_counter += 1
        print("{}: {}".format(songs[0],songs[1]))
    song_choice = input()
    if int(song_choice) not in range(1, 1 + song_counter):
        break
    print("{} playing now...".format(jukebox_albums[int(album_choice)-1][3][int(song_choice)-1][1]))

# Teacher's Code and "Constants" in Python - "final" Keyword. - Constant's UPPERCASE convention.

SONGS_LIST_INDEX = 3  # Constant'ların uppercase olması bir conventiondur. Bunun yerine final da konsa bu da aynı şeydir.
# Her iki şekilde de dikkatli olması gereken kodu yazan kişi. Python bu değerlere diğerlerinden farklı yaklaşmaz.
SONG_INDEX = 1

while True:
    print("Please choose your album (Invalid choose exits): ")
    for index, (album_name, artist, year, songs_list) in enumerate(jukebox_albums):
        print("{}: {}".format(index+1, album_name))
    # print("-"*70)
    # for index, value in enumerate(jukebox_albums):
    #     album_name, artist, year, songs_list = value    # Yani bu işlemi yukarıdaki kodda tek satırda yaptık
    #     print(index+1, album_name, artist, year, songs_list)

    choice = int(input())
    if 1 <= choice <= len(jukebox_albums):
        songs_list = jukebox_albums[choice-1][SONGS_LIST_INDEX]    # jukebox_albums[choice-1][3] 3 yerine daha anlamlı bir constant olur.
    else:
        break

    print("Please choose your song: ")
    for song_number, song_name in songs_list:  # Burada hoca kullansa da enumerate kullanmıyorum çünkü zaten numaralandırma yapabiliyoruz.
        print("{}: {}".format(song_number, song_name))

    song_choice = int(input())
    if 1 <= song_choice <= len(songs_list):
        print("{} is playing now...".format(songs_list[song_choice-1][SONG_INDEX]))
    # else:
    #     break  # Bir daha menüye gitmesi için bu bloğu kaldırdık. if bloğunu kaldırma ! Yanlış indexte error alırsın.

    print("="*40)
