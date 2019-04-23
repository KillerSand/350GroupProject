import os
import pickle

list= [1,2,3,4,5]
file = 'list.txt'


def writeFile(list):
    pickle.dump(list, open("list.save", "wb"))
    # with open(file, 'w') as f:
    #   f.write(str(list))
    #  f.close()

def readFile(file):
    names = pickle.load(open(file, "rb"))
    print(names[0].race)
    #with open(file, 'r') as f:
    #    filecontents = f.read()
    #    print(filecontents)
    #   f.close()

def deleteFile(file):
    if os.path.exists("list.txt"):
        os.remove("list.txt")
        print("The file was deleted")
    else:
        print("The file does not exist")
