#from clear_screen import *
from CharacterSheetList import *
from saveload import *

# This is testing using git from pycharm
characterList = []
# Starts the official character list

print("Welcome to the character creation program!")
while True:     # This while statement lets the main menu loop
    print("1) Create New Character")
    print("2) Save Character list")
    print("3) Load Character list")
    print("4) Delete Character list")
    print("5) Quit Program")
    try:
        x = int(input("Which function would you like to use(enter a number): "))
        if x == 1:
            characterList.append(characters())
        elif x == 2:
            writeFile(characterList)
        elif x == 3:
            readFile()
            # elif x == 4:
            # deleteList()
        elif x == 5:
            print("Thank You for using our Character Creation Program")
            quit(0)
        else:
            print("Please enter a number 1-5!")
    except ValueError:
        #clear()
        print("Please enter a proper number! ")
