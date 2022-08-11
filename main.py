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
            Rnumber()

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
    balldict = [color(10,200,10,"It is certain."),color(10,200,10,"It is decidedly so."),
                color(10,200,10,"Without a doubt."),color(10,200,10,"Yes definitely."),
                color(10,200,10,"You may rely on it."),color(10,200,10,"As I see it, yes."),
                color(10,200,10,"Most likely."),color(10,200,10,"Outlook good."),color(10,200,10,"Yes."),
                color(10,200,10,"Signs point to yes."),color(150,150,10,"Im legally not allowed to tell you."),
                color(150,150,10,"That is a very stupid question."),color(150,150,10,"You cant face the truth."),
                color(150,150,10,"Are you drunk?"),color(150,150,10,"Is this even a question?"),
                color(150,10,10,"No!"),color(150,10,10,"It's quite obvious the answer is no."),
                color(150,10,10,"I dont think so"),color(150,10,10,"Nah"),
                color(150,10,10,"What? absolutly not.")]
    while True:
        print(color(0,200,255,"Type '1' to get back to menu or '2' to exit the program."))
        print(color(150,80,230,"(Note!) that the 8-Ball can respond to No/Yes answers only.\n"
                               "Type your questions below. Answers will appear above."))
        answer = input("1. Back to Menu\n" + color(200,10,10,"2. Exit Program\n\n\n\n\n\n"))
        if answer == "1":
            MenuP()

        elif answer == "2":
            ExitP()

        else:
            ballgenchoice = random.choice(balldict)
            print(ballgenchoice)

def Rnumber():
    while True:
        print(color(0,200,255,"\n\n\n\nChoose your two numbers, Roll them, Menu or Back."))
        answer = input("1. Choose Numbers\n" + "2. Roll your numbers\n" + ""
        "3. Menu\n" + color(200,10,10,"4. Exit\n\n\n\n\n"))

        if answer == "1":
            numb = input(int("Type your first number below\n\n"))
            numb2 = input(int("Type your second number below\n\n"))

        elif answer == "2":
            print(random.randint(numb,numb2))

        elif answer == "3":
            MenuP()

        elif answer == "4":
            EndP()

        else:
            print("-----------------------")
            print(color(255,165,0,"Please input a valid option!"))
            print("-----------------------")


MenuP()
