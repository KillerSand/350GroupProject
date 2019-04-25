#from clear_screen import *
from CharacterSheetList import *
from saveload import *
from Attributes import skills

# This is testing using git from pycharm
characterList = []
# Starts the official character list

print("Welcome to the character creation program!")
while True:     # This while statement lets the main menu loop
    print("1) Create New Character")
    print("2) Save Character list")
    print("3) Load Character list")
    print("4) Delete Character list")
    print("5) Display Character info")
    print("6) Quit Program")
    try:
        x = int(input("Which function would you like to use(enter a number): "))
        if x == 1:
            characterList.append(characters())
        elif x == 2:
            writeFile(characterList)
        elif x == 3:
            characterList = readFile()
        elif x == 4:
            deleteFile()
        elif x == 5:
            count = len(characterList)
            if count < 1:
                print("No characters found")
                continue
            for (index, char) in zip(range(count), characterList):
                print(f"{index}) {char.name}, Level {char.level} {char.race} {char.job}")
            sel = None
            while sel is None:
                try:
                    print("Which character would you like to view?")
                    sel = int(input(": "))
                    if not sel in range(0, count):
                        raise ValueError("Selection '{}' is out of range".format(sel))
                except ValueError as v:
                    print(v)
                    sel = None
                except Exception:
                    print("Invalid selection")
                    sel = None
            print("\n")
            for attrib in ["Strength", "Dexterity", "Constitution", "Intelligence", "Wisdom", "Charisma"]:
                print(f"{attrib}: {characterList[sel].attributes.GetAttrib(attrib)}")
            print("\n")
            for skill in skills.keys():
                print(f"{skill}: {characterList[sel].attributes.GetSkillMod(skill)}")
        elif x == 6:
            print("Thank You for using our Character Creation Program")
            quit(0)
        else:
            print("Please enter a number 1-5!")
    except ValueError:
        #clear()
        print("Please enter a proper number! ")
