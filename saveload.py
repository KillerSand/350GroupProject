import os
import pickle

def writeFile(list):
    file = input("Enter a file name: ")
    file = file + ".save"
    pickle.dump(list, open(file, "wb"))
    # with open(file, 'w') as f:
    #   f.write(str(list))
    #  f.close()

def readFile(file):
    file = file + ".save"
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
