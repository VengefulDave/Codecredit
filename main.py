#Importing built in "Random" Function.
import random

#Text color function: Makes some text more noticeable and understandable.
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
            PassGen()

        elif answer == "5":
            NameGen()

        elif answer == "6":
            EndP()

        else:
            print(color(200,150,10,"-----------------------"))
            print(color(255,10,10,"Please input a valid option!"))
            print(color(200,150,10,"-----------------------"))

#Code End Choice: Ends the code completely.
def EndP():
    print(color(200,150,10,"\n\n\n\n\n\n\nAre You Sure You Want To Exit, Type The Number Of Choice Options."))
    answer = input(color(255,10,10,"\n1. Yes, End This Program!") +
                   color(10,255,10,"\n2. No, Get Me Back To The Program!\n\n\n\n\n"))
    while True:
        if answer == "1":
            exit()
        elif answer == "2":
            MenuP()
        else:
            print(color(200,150,10,"-----------------------"))
            print(color(255,10,10,"Please input a valid option!"))
            print(color(200,150,10,"-----------------------"))
            EndP()

#8-Ball Choice: User can shake ball and recieve answers.
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
        print(color(0,200,255,"Type '1' For Menu, '2' to End Program or Type Questions Below."))
        print(color(150,80,230,"(Note!) that the 8-Ball can respond to No/Yes answers only.\n"
                               "Type your questions below. Answers will appear above."))
        answer = input("1. Back to Menu\n" + color(200,10,10,"2. Exit Program\n\n\n\n\n\n"))
        if answer == "1":
            MenuP()

        elif answer == "2":
            EndP()

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
            print(color(200,150,10,"-----------------------"))
            print(color(255,10,10,"Please input a valid option!"))
            print(color(200,150,10,"-----------------------"))

#Dice Choice: Choose a realistic dice option and roll.
def Dice():
    userdice = "Nothing!"
    while True:
        print(color(0,200,255,"\nChoose Dice type, Roll it, Menu or Exit."))
        answer = input("1. Choose Dice\n2. Roll\n3. Menu" + color(250,10,10,"\n4. Exit\n\n\n"))
        if answer == "1":
            print(color(10,200,255,"Choose Dice Style:") +
            color(150,80,230,"\n(Note!) Choose the letter corresponding to the choice!"))
            diceCh = input("\nA. 4 Side\nB. 6 Side\nC. 8 Side\nD. 10 Side\nE. 12 Side"
                           "\nF. 20 Side\n\n\n")
            dicelist = ["a","A", "b", "B", "c", "C", "d", "D", "e", "E", "f", "F"]
            if diceCh.lower() == "a":
                userdice = "A. 4 Side"
            elif diceCh.lower() == "b":
                userdice = "B. 6 Side"
            elif diceCh.lower() == "c":
                userdice = "C. 8 Side"
            elif diceCh.lower() == "d":
                userdice = "D. 10 Side"
            elif diceCh.lower() == "e":
                userdice = "E. 12 Side"
            elif diceCh.lower() == "f":
                userdice = "F. 20 Side"
            else:
                print(color(200,150,10,"-----------------------"))
                print(color(255,10,10,"Please input a valid option!"))
                print(color(200,150,10,"-----------------------"))
            print(color(150,80,230,"\nYour Choice: {}".format(userdice)))

        elif answer == "2":
            try:
                if diceCh.lower() == "a":
                    diceRe = random.randint(1,4)
                if diceCh.lower() == "b":
                    diceRe = random.randint(1,6)
                if diceCh.lower() == "c":
                    diceRe = random.randint(1,8)
                if diceCh.lower() == "d":
                    diceRe = random.randint(1,10)
                if diceCh.lower() == "e":
                    diceRe = random.randint(1,12)
                if diceCh.lower() == "f":
                    diceRe = random.randint(1,20)
                print(color(150,80,230,"Your Dice Roll Number:{}".format(diceRe)))
            except:
                print(color(200,150,10,"-----------------------"))
                print(color(255,10,10,"Choose a Dice first!"))
                print(color(200,150,10,"-----------------------"))
        elif answer == "3":
            MenuP()

        elif answer == "4":
            EndP()

        else:
            print(color(200,150,10,"-----------------------"))
            print(color(255,10,10,"Please input a valid option!"))
            print(color(200,150,10,"-----------------------"))

#Password.Gen Choice: Generates passwords of user's choice or preset.
placelist = []
emotionlist = []
animallist = []
def PassGen():
    while True:
        print(color(0,200,255,"\nGenerate Passwords, Input your own keywords, See list, Menu or Exit."))
        answer = input("1. Generate Preset Pass\n2. Genarate Own Pass\n3. Input Own Pass Keywords\n4. See Own List"
                    "\n5. Menu" + color(250,10,10,"\n6. Exit\n\n\n"))
        passlist1 = random.choice("QWERTYUIOPASDFGHJKLZXCVBNM")
        passlist2 = random.choice("!@#$%^&*()")
        passlist3 = random.choice("1234567890")
        if answer == "1":
            print(color(150,80,230,"Your Password:") +
                "{}{}{}{}{}{}".format(passlist1,passlist1,passlist1,passlist2,passlist3,passlist3,))

        elif answer == "2":
            try:
                placegen = placelist[(random.randint(0,len(placelist)-1))]
                emotiongen = emotionlist[(random.randint(0,len(emotionlist)-1))]
                animalgen = animallist[(random.randint(0,len(animallist)-1))]
                print(color(150,80,230,"Your Password:") +
                    "{} {} @ {}".format(emotiongen,animalgen,placegen))
            except:
                print(color(200,150,10,"-----------------------"))
                print(color(255,10,10,"Please Input Your Keywords For Each Option First!"))
                print(color(200,150,10,"-----------------------"))
        elif answer == "3":
            while True:
                print(color(0,200,255,"\n\n\nTypes of words to add to your password generation, or Back"))
                answer = input("\n1. Choose a Memorable Place To You, Eg. Kulim Park"
                           "\n2. Choose Your Most Common Emotion, Eg. Anger\n3. Choose Your Favourite Animal" +
                           color(255,150,10,"\n4. Back to Password Gen Menu\n\n\n"))
                if answer == "1":
                    while True:
                        ownchoice1 = input(color(150,80,230,
                            "Type Below a/multiple Memorable Place, or Type '1' to go Back\n\n"))
                        if ownchoice1 == "1":
                            break
                        else:
                            placelist.append(ownchoice1)
                            print("{} : ".format(ownchoice1) + color(255,150,10,"Has been added to the 'Place' List!"))
                elif answer == "2":
                    while True:
                        ownchoice2 = input(color(150,80,230,
                            "Type Below Common Emotion/Emotions To You, or Type '1' to go Back\n\n"))
                        if ownchoice2 == "1":
                            break
                        else:
                            emotionlist.append(ownchoice2)
                            print("{} : ".format(ownchoice2) + color(255,150,10,"Has been added to the 'Emotion' List!"))
                elif answer == "3":
                    while True:
                        ownchoice3 = input(color(150,80,230,
                            "Type Below Your Favourite Animal/Animals, or Type '1' to go Back\n\n"))
                        if ownchoice3 == "1":
                            break
                        else:
                            animallist.append(ownchoice3)
                            print("{} : ".format(ownchoice3) + color(255,150,10,"Has been added to the 'Animal' List!"))
                elif answer == "4":
                    PassGen()
                else:
                    print(color(200,150,10,"-----------------------"))
                    print(color(255,10,10,"Please input a valid option!"))
                    print(color(200,150,10,"-----------------------"))

        elif answer == "4":
            while True:
                print("Your Place List: {}".format(placelist))
                print("Your Emotion List: {}".format(emotionlist))
                print("Your Animal List: {}".format(animallist))
                answer = input(color(0,200,255,"\nChoose list and Remove Word, or Back") + "\n1. Edit Place List\n"
                    "2. Edit Emotion List\n3. Edit Animal List\n4. Back" + color(250,10,10,"\n5. Exit\n\n\n"))
                if answer == "1":
                    while True:
                        try:
                            print("Your Place List: {}".format(placelist))
                            listremove = int(input(color(150,80,230,"Type the number of the word you want to delete in PLACE LIST, or Type '0' to go back.\n\n\n")))
                            if listremove == 0:
                                break
                            else:
                                del placelist[listremove-1]
                        except:
                            print(color(200,150,10,"-----------------------"))
                            print(color(255,10,10,"Please input a valid option!"))
                            print(color(200,150,10,"-----------------------"))

                elif answer == "2":
                    while True:
                        try:
                            print("Your Emotion List: {}".format(emotionlist))
                            listremove = int(input(color(150,80,230,"Type the number of the word you want to delete in EMOTION LIST, or Type '0' to go back.\n\n\n")))
                            if listremove == 0:
                                break
                            else:
                                del emotionlist[listremove-1]
                        except:
                            print(color(200,150,10,"-----------------------"))
                            print(color(255,10,10,"Please input a valid option!"))
                            print(color(200,150,10,"-----------------------"))
                elif answer == "3":
                    while True:
                        try:
                            print("Your Animal List: {}".format(animallist))
                            listremove = int(input(color(150,80,230,"Type the number of the word you want to delete in ANIMAL LIST, or Type '0' to go back.\n\n\n")))
                            if listremove == 0:
                                break
                            else:
                                del animallist[listremove-1]
                        except:
                            print(color(200,150,10,"-----------------------"))
                            print(color(255,10,10,"Please input a valid option!"))
                            print(color(200,150,10,"-----------------------"))
                elif answer == "4":
                    PassGen()
                elif answer == "5":
                    EndP()
                else:
                    print(color(200,150,10,"-----------------------"))
                    print(color(255,10,10,"Please input a valid option!"))
                    print(color(200,150,10,"-----------------------"))

        elif answer == "5":
            MenuP()

        elif answer == "6":
            EndP()

        else:
            print(color(200,150,10,"-----------------------"))
            print(color(255,10,10,"Please input a valid option!"))
            print(color(200,150,10,"-----------------------"))

#Name.Gen:
def NameGen():
    rname1_list = ["Oliver"
        "Noah","Jack","Leo","George","Charlie","Lucas","Theodore","William","Luca",
        "Elijah","Liam","Mason","James","Thomas","Hudson","Arlo","Lachlan",
        "Archie","Arthur","Hunter","Oscar","Max","Levi","Finn",
        "Hugo","Ethan","Asher","Henry","Cooper","carter",]
    rname2_list = ["Ezra","Lincoln","Felix","Alexander","Archer","Beau",
        "Harrison","Eli","Jackson","Louis","Theo","Benjamin","Nikau","Isaac","Joseph",
        "Joshua","Blake","Daniel","Samuel","Grayson","Caleb","Jasper","Luka",
        "Braxton","Edward","Jacob","Harry","Harvey","River","Riley","Roman"]
    rname1 = rname1_list[0,len(rname1_list)-1]
    rname2 = rname2_list[0,len(rname2_list)-1]
    gname1_list = ["Administered","Arranged","Chaired","Coordinated",
        "Directed","Executed","Delegated","Headed","Managed","Operated","Orchestrated","Organized","Planned",
        "Produced","Programmed","Spearheaded","Accelerated","Achieved","Advanced","Amplified","Boosted","Capitalized",
        "Conserved","Consolidated","Decreased","Deducted","Delivered","Enhanced","Expanded","Expedited"]
    gname2_list = []
    while True:
        print(color(0,200,255,"\nGenerate Preset Names, Input your own Names, See Own list, Menu or Exit."))
        answer = input("1. Generate Real Name\n2. Genarate Gamer Name\n3. Generate Own Name\n4. Create Own Name Gen"
                       "\n5. See Own Gen List\n6. Menu" + color(250,10,10,"\n7. Exit\n\n\n"))
        if answer == "1":
            print(color(150,80,230,"Your Generated Name:") + "{}{}".format(rname1,rname2))
        elif answer == "2":
            print(color(150,80,230,"Your Generated Name:") + "{}{}".format(gname1,gname2))
        elif answer == "3":
            pass
        elif answer == "4":
            pass
        elif answer == "5":
            pass
        elif answer == "6":
            pass
        elif answer == "7":
            pass
        else:
            print(color(200,150,10,"-----------------------"))
            print(color(255,10,10,"Please input a valid option!"))
            print(color(200,150,10,"-----------------------"))



MenuP()

