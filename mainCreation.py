from CharacterSheetList import characters
from clear_screen import clear
from menuItems import *

a = {}

print("Welcome to the character creation program!")
while True:
    print("1) Create New Character")
    print("2) Save Character list")
    print("3) Load Character list")
    print("4) Delete Character list")
    print("5) Quit Program")
    try:
        x = int(input("Which function would you like to use(enter a number): "))
        if x == 1:
            createcharacter(a)

        elif x == 2:
            saveList()

        elif x == 3:
            loadList()
        elif x == 4:
            deleteList()
        elif x == 5:
            quiting()
        else:
            print("Please enter a number 1-5!")
    except ValueError:
        clear()
        print("Please enter a proper number! ")
