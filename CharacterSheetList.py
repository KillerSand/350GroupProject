from Attributes import *

class characters:
    def __init__(self,name):
        x = True
        self.health = 0
        while x:
            try:
                self.level = int(input("What level are you?: "))
                x = False
            except ValueError:
                print("Enter a valid integer!")
                x = True

        # Name
        self.name = input("What is the name of the player?: ")

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

        # Class
        self.job = input("What your character's class?: ")

        self.name = name
        self.job = ""
        self.age = 0
        self.height = 0
        self.weight = 0
        self.race = ""
        self.attributes = attribute()

