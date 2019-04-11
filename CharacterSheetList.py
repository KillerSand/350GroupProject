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

        self.name = name
        self.job = ""
        self.age = 0
        self.height = 0
        self.weight = 0
        self.race = ""
        self.attributes = attribute()

