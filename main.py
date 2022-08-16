#Importing built in "Random" Function.
import random

#Text color function.
def color(r, g, b, text):
    return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text)

#Menu Choice: User can choose style of generation.
def MenuP():
    while True:
        print(color(0,200,255,"Type in the number corresponding to the desired generation style."))
        answer = input("1. Magic 8 Ball\n2. Dice\n3. Random Number\n4. "
                       "Passwords Generation\n5. Names Generation\n" + color(250,10,10,"6. Exit\n\n\n"))
        if answer == "1":
            Magic8Ball()

        elif answer == "2":
            Dice()

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
                color(10,200,10,"Signs point to yes."),color(200,150,10,"Im legally not allowed to tell you."),
                color(200,150,10,"That is a very stupid question."),color(200,150,10,"You cant face the truth."),
                color(200,150,10,"Are you drunk?"),color(200,150,10,"Is this even a question?"),
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

#Random Number Choice: User chooses two numbers to generate between.
def Rnumber():
    while True:
        print(color(0,200,255,"\nChoose your two numbers, Roll them, Menu or Back."))
        answer = input("1. Choose Numbers\n" + "2. Roll numbers\n" + ""
        "3. Menu\n" + color(200,10,10,"4. Exit\n\n\n\n\n"))


        if answer == "1":
            try:
                print(color(150,80,230,"\n\n(Note!) The first number cannot be bigger than the second. "
                                       "Both numbers have to be a number!"))
                numb = int(input("Type your first number below\n\n"))
                numb2 = int(input("Type your second number below\n\n"))
            except:
                print(color(200,150,10,"------------------------------------------------"))
                print(color(255,10,10,"GRR.. YOU DIDN'T READ THE NOTES. Re-Choose Your Numbers!"))
                print(color(200,150,10,"------------------------------------------------"))
                Rnumber()

        elif answer == "2":
            try:
                print(color(150,80,230,"Your number: "))
                print(random.randint(numb,numb2))
            except:
                print(color(200,150,10,"-----------------------------"))
                print(color(255,10,10,"Pick Your 'CORRECT' Numbers First!"))
                print(color(200,150,10,"-----------------------------"))
                Rnumber()
        elif answer == "3":
            MenuP()

        elif answer == "4":
            EndP()

        else:
            print("-----------------------")
            print(color(255,165,0,"Please input a valid option!"))
            print("-----------------------")

#Dice choice: Choose a realistic dice option and roll.
def Dice():
    while True:
        print(color(0,200,255,"\nChoose Dice type, Roll it, Menu or Exit."))
        answer = input("1. Choose Dice\n2. Roll\n3. Menu" + color(250,10,10,"\n4. Exit\n\n\n"))
        if answer == "1":
            print(color(10,200,255,"Choose Dice Style:") +
                  color(150,80,230,"\n(Note!) Choose the letter corresponding to the choice!"))
            diceCh = input("\nA. 4 Side\nB. 6 Side\nC. 8 Side\nD. 10 Side\nE. 12 Side"
                           "\nF. 20 Side\n\n\n")
            dicelist = ["a","A", "b", "B", "c", "C", "d", "D", "e", "E", "f", "F"]
            if diceCh not in dicelist:
                print("-----------------------")
                print(color(255,165,0,"Please input a valid option!"))
                print("-----------------------")

        elif answer == "2":
            if diceCh == "a" or "A":
                diceRe = random.randint(1,4)
            if diceCh == "b" or "B":
                diceRe = random.randint(1,6)
            if diceCh == "c" or "C":
                diceRe = random.randint(1,8)
            if diceCh == "d" or "D":
                diceRe = random.randint(1,10)
            if diceCh == "e" or "E":
                diceRe = random.randint(1,12)
            if diceCh == "f" or "F":
                diceRe = random.randint(1,20)
            print(color(150,80,230,"Your Dice Roll Number:{}".format(diceRe)))
        elif answer == "3":
            MenuP()

        elif answer == "4":
            EndP()

        else:
            print("-----------------------")
            print(color(255,165,0,"Please input a valid option!"))
            print("-----------------------")

MenuP()
