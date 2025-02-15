albums = [("Welcome to my Nightmare", "Alice Cooper", 1975,
           [
               (1, "Welcome to my Nightmare"),
               (2, "Devil's Food"),
               (3, "The Black Widow"),
               (4, "Some Folks"),
               (5, "Only Women Bleed"),
           ]),
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
           ]),
          ("Nightflight", "Budgie", 1981,
           [
               (1, "I Turned to Stone"),
               (2, "Keeping a Rendezvous"),
               (3, "Reaper of the Glory"),
               (4, "She Used Me Up"),
           ]),
          ("More Mayhem", "Emilda May", 2011,
           [
               (1, "Pulling the Rug"),
               (2, "Psycho"),
               (3, "Mayhem"),
               (4, "Kentish Town Waltz"),
           ]),
          ]

users_choice = None
valid_choices = []
song_choice = None

for i in range(1, len(albums)+1):
    valid_choices.append(i)
print(valid_choices)

while users_choice != 0:
    valid_song_choices = []
    print("Please choose your album below:")
    for index, album_tuple in enumerate(albums):
        print("{}-) {}".format(index+1, album_tuple[0]))

    users_choice = int(input("Enter your album choice:"))
    if users_choice not in valid_choices:
        break

    print("Please choose your song: ")
    for song_tuple in albums[users_choice-1][3]:
        print("{}-) {}".format(song_tuple[0], song_tuple[1]))

    for i in range(1, len(albums))

    print(valid_song_choices)
    song_choice = int(input())
    if song_choice not in valid_song_choices:
        break
    else:
        print("{} playing...".format(albums[users_choice-1][3][song_choice][1]))
else:
    print("Exit program...")
