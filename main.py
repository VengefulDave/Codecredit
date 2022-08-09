#Importing built in "Random" Function.
import random

#Text color function.
def color(r, g, b, text):
    return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text)

#Menu Popup: User can choose style of generation.
def MenuP():
    while True:
        print(color(0,200,255,"Type in the number corresponding to the desired generation style."))
        answer = input("1. Magic 8 Ball\n2. Dice\n3. Random Number\n4."
                       "Passwords Generation\n5. Names Generation\n6. Exit\n\n")
        if answer == "1":
            Magic8Ball()

        elif answer == "2":
            pass

        elif answer == "3":
            pass

        elif answer == "4":
            pass

        elif answer == "5":
            pass

        elif answer == "6":
            EndP()

        else:
            print("-----------------------")
            print(color(255,165,0,"Please input a valid option!"))
            print("-----------------------")

#Code exit function
def EndP():
    exit()

#8-Ball Popup: User can shake ball, Menu or back.
def Magic8Ball():
    while True:
        print(color(0,200,255,"Please choose an option in number form"))
        answer = input("1. Shake 8-Ball\n2. Back to Menu\n3. Exit Program\n\n\n\n\n")
        if answer == "1":
            pass

        elif answer == "2":
            MenuP()

        elif answer == "3":
            EndP()

        else:
            print("-----------------------")
            print(color(255,165,0,"Please input a valid option!"))
            print("-----------------------")
MenuP()

