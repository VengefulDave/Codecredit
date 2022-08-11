#Importing built in "Random" Function.
import random

#Text color function.
def color(r, g, b, text):
    return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text)

#Menu Choice: User can choose style of generation.
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

#8-Ball Choice: User can shake ball, Menu or back.
def Magic8Ball():
    balldict = ["It is certain.","It is decidedly so.","Without a doubt.","Yes definitely.",
                "You may rely on it.","As I see it, yes.","Most likely.","Outlook good.","Yes.",
                "Signs point to yes.","Im legally not allowed to tell you.","That is a very stupid question.",
                "You cant face the truth.","Are you drunk?","Is this even a question?","No!",
                "It's quite obvious the answer is no.","I dont think so","Nah","What? absolutly not."]
    while True:
        print(color(0,200,255,"Type '1' to get back to menu or '2' to exit the program."))
        print(color(150,80,230,"Note that the 8-Ball will resond to No/Yes answers only.\n"
                               "Type your questions below."))
        answer = input("1. Back to Menu\n" + color(200,10,10,"2. Exit Program\n\n\n\n\n\n"))
        if answer == "1":
            MenuP()

        elif answer == "2":
            ExitP()

        else:
            ballgenchoice = random.choice(balldict)
            print(ballgenchoice)
MenuP()

