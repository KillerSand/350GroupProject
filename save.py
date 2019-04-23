#Sabrina

import pickle

def saveList(characterList):
    #example of created character list
    names = ["Abby", "Sam", "Jon", "Dave", "Michael", "Winona"]
    # created list of characters

    #example  of printed list
    print("Names: ")
    print(characterList)

    #print the list
    #print("Your created Character: ")
    #print(import.CharacterSheet)

    # Save file example
    # must tell what file to use and where to save it to
    # wb = writing in binary mode
    pickle.dump(characterList, open("names.save", "wb"))

    # example of a changed list
    names.remove("test")
    print("Changed list of names: ")
    print(characterList)


    #load save data
    #rb = reading file
    names = pickle.load(open("names.save", "rb"))

    #example  of printed list
    print("Original Names: ")
    print(names)