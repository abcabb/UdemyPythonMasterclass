print("Please choose your training program for today from the list below.")
while True:
    print("1-) Work out triceps\n" +
          "2-) Work out biceps\n"+
          "3-) Work out chest\n"+
          "4-) Work out six-pack\n"+
          # "5-) Work out legs\n"+
          # "6-) Work out back\n"+
          # "7-) Work out forearms\n"+
          # "8-) Work out shoulders\n"+
          # "9-) Work out martial\n"+
          "0-) Exit")
    select_of_user = input("Write something about your choice :\n").casefold()
    if select_of_user in "1-) work out triceps":
        print("Lets work triceps!")
        break
    elif select_of_user in "2-) work out biceps":
        print("Lets work biceps!")
        break
    elif select_of_user in "3-) work out chest":
        print("Lets work chest!")
        break
    elif select_of_user in "4-) work out six-pack":
        print("Lets work six-pack!")
        break
    elif select_of_user in "0-) exit":
        break
    else:
        print("There is no such option. Write again.")

# Another example
print("-" * 45)

choice = "-"
while choice != "0":
    # if choice == "0":
    #     break         Bunu burda yazmak yerine direkt while'ın conditionu yapmak daha kısa.
    if choice in "1234":
        print("Your choice is {}".format(choice))
    else:
        print("1-) Work out triceps\n" +
              "2-) Work out biceps\n"+
              "3-) Work out chest\n"+
              "4-) Work out six-pack\n"+
              "0-) Exit")

    choice = input("Write something about your choice :\n")
