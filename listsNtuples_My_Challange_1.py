available_workouts = ["Chest workout",
                      "Triceps workout",
                      "Biceps workout",
                      "Back workout",
                      "Shoulders workout",
                      "Legs workout",
                      "Forearm workout",
                      "Glutes workout"]

available_choices = []
#1-) String Comprehension            range(1, 7+1)
# available_choices = [str(i) for i in range(1,len(available_workouts)+1)]

#2-) Using for loop
for i in range(1, len(available_workouts)+1):
    available_choices.append(str(i))
print(available_choices)

my_training_program = []
choice = "-"

while choice != "0":
    if choice in available_choices:
        print("{} added to your program.".format(choice))
        index_of_choice = int(choice) - 1
        chosen_item = available_workouts[index_of_choice]
        my_training_program.append(chosen_item)
    else:
        for number, item in enumerate(available_workouts):
            print("{}: {}".format(number+1, item))

    choice = input()

print(my_training_program)
