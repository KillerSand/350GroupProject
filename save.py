#Sabrina

import pickle

#example of created character list
names = ["Abby", "Sam", "Jon", "Dave", "Michael", "Winona"]
# created list of characters
 #import CharacterSheetList

#example  of printed list
print("Names: ")
print(names)

#print the list
#print("Your created Character: ")
#print(import.CharacterSheet)

# Save file example
# must tell what file to use and where to save it to
# wb = writing in binary mode
pickle.dump(names, open("names.save", "wb"))

# example of a changed list
names.remove("Abby")
print("Changed list of names: ")
print(names)


#load save data
#rb = reading file
names = pickle.load(open("names.save", "rb"))

#example  of printed list
print("Original Names: ")
print(names)