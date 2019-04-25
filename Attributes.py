from math import floor
import roller

# Skills and from what they derive
skills = {
    "Acrobatics" : "Dex",
    "Animal Handling" : "Wis",
    "Arcana" : "Int",
    "Athletics" : "Str",
    "Deception" : "Cha",
    "History" : "Int",
    "Insight" : "Wis",
    "Intimidation" : "Cha",
    "Investigation" : "Int",
    "Medicine" : "Wis",
    "Nature" : "Int",
    "Perception" : "Wis",
    "Performance" : "Cha",
    "Persuasion" : "Cha",
    "Religion" : "Int",
    "Sleight of Hand" : "Dex",
    "Stealth" : "Dex",
    "Survival" : "Wis"
}

class Attributes:
    
    # Create a new Attributes object. If values are provided, they will be used as opposed to prompting user.
    def __init__(self, values = None):
        # Initialize Attributes
        self.Strength = 10
        self.Dexterity = 10
        self.Constitution = 10
        self.Intelligence = 10
        self.Wisdom = 10
        self.Charisma = 10

        # If we have values, use those and done
        if values is not None:
            self.Strength = values[0]
            self.Dexterity = values[1]
            self.Constitution = values[2]
            self.Intelligence = values[3]
            self.Wisdom = values[4]
            self.Charisma = values[5]
            return

        # Give user option of stat decision
        sel = None
        while sel is None:
            try:
                print("How would you like to decide stats?\n0: Roll randomly\n1: Manual input")
                sel = int(input(": "))
                if not sel in [0, 1]:
                    raise ValueError("Selection '{}' is out of range".format(sel))
            except ValueError as v:
                print(v)
                sel = None
            except Exception:
                print("Invalid selection")
                sel = None

        # Roll
        if sel is 0:
            self.RollStats()
        # Ask
        else:
            self.AskStats()

        # All done with constructor

    # Return value of attribute based on short name
    def GetAttrib(self, attribName):
        return {
            "Str" : self.Strength,
            "Dex" : self.Dexterity,
            "Con" : self.Constitution,
            "Int" : self.Intelligence,
            "Wis" : self.Wisdom,
            "Cha" : self.Charisma
        }[attribName]

    # Return attribute mod from name
    # (Attribute - 10) / 2
    def GetAttribMod(self, attribName):
        return floor((self.GetAttrib(attribName) - 10) / 2)

    # Return skill mod from name
    def GetSkillMod(self, skillName):
        return self.GetAttribMod(skills[skillName])

    # FIXME: Roll our stats randomly
    def RollStats(self):
        stats = roller.dieRoller()
        for stat, value in zip(["Strength", "Dexterity", "Constitution", "Intelligence", "Wisdom", "Charisma"],stats):
            setattr(self, stat, value)
            print(stat + " = " + str(value))
        print("\n")


    # Ask user for each stat
    def AskStats(self):
        for stat in ["Strength", "Dexterity", "Constitution", "Intelligence", "Wisdom", "Charisma"]:
            sel = None
            while sel is None:
                try:
                    sel = int(input("What is your {} stat?: ".format(stat)))
                    if not sel in range(1, 21):
                        raise ValueError("Stat must be in range 1-20")
                except ValueError as v:
                    print(v)
                    sel = None
                except Exception:
                    print("Invalid input")
                    sel = None
            setattr(self, stat, sel)

    
