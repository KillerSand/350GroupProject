from Attributes import *

class characters:
    def __init__(self):
        while True:
            playerName = input("Who will be using this character?: ")
            # name will be playerName for using character method
            if input("Will " + playerName + " be using this character? (Y or N): ").lower() == 'y':
                # Check if user's input is y and if it is exit the loop and continue with program
                # Otherwise prompt user for character's name again
                break
        self.playerName = playerName
        # Name
        self.name = input("What is the name of the character?: ")

        # Race
        self.race = input("What race is " + self.name + "?: ")

        # Class
        self.job = input("What class will " + self.name + " be?: ")
        while True:
            try:
                self.level = int(input("What level is " + self.name + "?: "))
                break
            except ValueError:
                print("Enter a valid integer!")
        # Age
        while True:
            try:
                self.age = int(input("How old is " + self.name + "?: "))
                break
            except ValueError:
                print("Please enter a valid integer")

        self.attributes = Attributes()