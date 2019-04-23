from Attributes import *

class characters:
    def __init__(self,playerName):
        x = True
        self.health = 0
        while x:
            try:
                self.level = int(input("What level are you?: "))
                x = False
            except ValueError:
                print("Enter a valid integer!")
                x = True

        self.playerName = playerName
        # Name
        self.name = input("What is the name of the character?: ")

        # Race
        self.race = input("What is your character's race?: ")

        # Age
        while y:
            try:
                self.age = int(input("What is the age of your character?: "))
                y = False
            except ValueError:
                print("Please enter a valid integer")
                y = True

        #Class
        self.job = input("What your character's class?: ")
        self.attributes = Attributes()

