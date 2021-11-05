from random import randint as r
from termcolor import colored
import shutil

def replace_line(file_name, line_num, text):
    lines = open(file_name, 'r', encoding="UTF-8").readlines()
    lines[line_num] = text + "\n"
    out = open(file_name, 'w', encoding="UTF-8")
    out.writelines(lines)
    out.close()

# In order (1)

def inorder(Lan1, Lan2):
    correct = 0

    for i in range(len(Lan1)):
        print((Lan1[i]).center(cols))
        tl = input(("Your translation: \n").center(cols))
        certainty = input(("are you sure? (press ENTER if certain, if not, write another translation)\n").center(cols))

        if certainty.strip() != "":
            tl = certainty

        if tl.lower().strip() == "n":
            break
        
        elif tl.lower().strip() == Lan2[i].lower().strip():
            print((colored("Correct!", "green")).center(cols))
            print(("press 'n' to finish").center(cols))
            print("\n")

            correct += 1
        
        else:
            print((colored("Wrong!", "red")).center(cols))
            print(("Actual translation: " + Lan2[i]).center(cols))
            print(("press 'n' to finish").center(cols))
            print("\n")

            if Lan1[i] not in tempmist:
                tempmist.append(i)
                print(i, file=Mistakes)
                
    print((str(correct) + " out of " + str(len(Lan1)) + " answers correct!").center(cols))
    print("\n")

# Randomized Repeating (2)

def randomized(Lan1, Lan2):
    while True:
        i = r(0, len(Lan1) - 1)
        print((Lan1[i]).center(cols))

        tl = input(("Your translation: \n").center(cols))
        certainty = input(("are you sure? (press ENTER if certain, if not, write another translation)\n").center(cols))

        if certainty.strip() != "":
            tl = certainty

        if tl.lower().strip() == "n":
            break
            
        elif tl.lower().strip() == Lan2[i].lower().strip():
            print((colored("Correct!", "green")).center(cols))
            print(("press 'n' to finish").center(cols))
            print("\n")
            
        else:
            print((colored("Wrong!", "red")).center(cols))
            print(("Actual translation: " + Lan2[i]).center(cols))
            print(("press 'n' to finish").center(cols))
            print("\n")

            if Lan1[i] not in tempmist:
                tempmist.append(i)
                print(i, file=Mistakes)

# Randomized Without Repeating (3)

def notrep(Lan1, Lan2):
    newLan1 = Lan1.copy()
    newLan2 = Lan2.copy()
    correct = 0
    oldlen = len(Lan1)

    while len(newLan1) != 0:
        i = r(0, len(newLan1) - 1)
        print((newLan1[i]).center(cols))
            
        tl = input(("Your translation: \n").center(cols))
        certainty = input(("are you sure? (press ENTER if certain, if not, write another translation)\n").center(cols))

        if certainty.strip() != "":
            tl = certainty

        if tl.lower().strip() == "n":
            break
    
        elif tl.lower().strip() == newLan2[i].lower().strip():
            print((colored("Correct!", "green")).center(cols))
            print(("press 'n' to finish").center(cols))
            print("\n")

            correct += 1
            
        else:
            print((colored("Wrong!", "red")).center(cols))
            print(("Actual translation: " + newLan2[i]).center(cols))
            print(("press 'n' to finish").center(cols))
            print("\n")

            if newLan1[i] not in tempmist:
                newi = Lan1.index(newLan1[i])
                tempmist.append(newi)
                print(newi, file=Mistakes)

        newLan1.pop(i)
        newLan2.pop(i)
    
    print((str(correct) + " out of " + str(oldlen) + " answers correct!").center(cols))
    print("\n")

# Fix Mistakes (4)

def fixmistakes(Lan1, Lan2, mistakes):
    for i in mistakes:
        print((Lan1[int(i)]).center(cols))
        tl = input(("Your translation: \n").center(cols))
        certainty = input(("are you sure? (press ENTER if certain, if not, write another translation)\n").center(cols))

        if certainty.strip() != "":
            tl = certainty

        if tl.lower().strip() == "n":
            break
        
        elif tl.lower().strip() == Lan2[int(i)].lower().strip():
            print((colored("Correct!", "green")).center(cols))
            print(("press 'n' to finish").center(cols))
            print("\n")
        
        else:
            print((colored("Wrong!", "red")).center(cols))
            print(("Actual translation: " + Lan2[int(i)]).center(cols))
            print(("press 'n' to finish").center(cols))
            print("\n")
        
# Change Translation (5)

def changeTL(Lan1, Lan2, chooseLan):
    while True:
        wordtochange = input(("word to change:\n").center(cols))

        if wordtochange.lower().strip() in Lan1:
            wordindex = Lan1.index(wordtochange.lower().strip())
            newword = input(("New translation:\n").center(cols))

            if chooseLan == "2":
                replace_line('words/language_1.txt', wordindex, newword.lower().strip())
            else:
                replace_line('words/language_2.txt', wordindex, newword.lower().strip())

        elif wordtochange.lower().strip() in Lan2:
            wordindex = Lan2.index(wordtochange.lower().strip())
            newword = input(("New translation:\n").center(cols))

            if chooseLan == "2":
                replace_line('words/language_1.txt', wordindex, newword.lower().strip())
            else:
                replace_line('words/language_2.txt', wordindex, newword.lower().strip())

        else:
            print(("This word is not in the list\n").center(cols))
    
        moree = input((("Would you like to change more? 'y' or 'n':\n")).center(cols))
    
        if moree != "y":
            break

cols, rows = shutil.get_terminal_size()

InLan1 = open("words/language_1.txt", "r", encoding="UTF-8")
InLan2 = open("words/language_2.txt", "r", encoding="UTF-8")
Mistakes = open("words/mistakes.txt", "w", encoding="UTF-8")

readmistakes = open("words/mistakes.txt", "r", encoding="UTF-8")
tempmist = readmistakes.read().split("\n")

Lan1 = InLan1.read().split("\n")
Lan2 = InLan2.read().split("\n")

while True:
    print(("From language 1 to language 2 -- enter '1'").center(cols))
    chooseLan = input(("From language 2 to language 1 -- enter '2'\n").center(cols))
    
    if chooseLan == "1":
        break
    elif chooseLan == "2":
        Lan1, Lan2 = Lan2, Lan1
        break

while True:
    print(("Exit -- n").center(cols))
    print(("Words in order -- '1'").center(cols))
    print(("Words randomized -- '2'").center(cols))
    print(("Random words without repeating -- '3'").center(cols))
    print(("Fix your mistakes -- '4'").center(cols))

    choice = input(("Change translation -- '5'\n").center(cols))

    if choice == "1":
        inorder(Lan1, Lan2)

    elif choice == "2":
        randomized(Lan1, Lan2)
    
    elif choice == "3":
        notrep(Lan1, Lan2)

    elif choice == "4":
        if len(tempmist[1:]) != 0:
            fixmistakes(Lan1, Lan2, tempmist[1:])

        else:
            print((colored("No mistakes yet!", "blue")).center(cols))

    elif choice == "5":
        changeTL(Lan1, Lan2, chooseLan)

    elif choice == "n":
        break
