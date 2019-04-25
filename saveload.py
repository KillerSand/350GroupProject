import os
import pickle

def writeFile(list):
    file = askFile()
    pickle.dump(list, open(file, "wb"))
    # with open(file, 'w') as f:
    #   f.write(str(list))
    #  f.close()

def readFile():
    file = askFile()
    if not os.path.exists(file):
        print(f"The file '{file}' does not exist")
    try:
        characterList = pickle.load(open(file, "rb"))
    except:
        print(f"Could not load {file}")
    return characterList
    #with open(file, 'r') as f:
    #    filecontents = f.read()
    #    print(filecontents)
    #   f.close()

def deleteFile():
    file = askFile()
    if os.path.exists(file):
        os.remove(file)
        print(f"The file '{file}' was deleted")
    else:
        print(f"The file '{file}' does not exist")

def askFile():
    print("\nCurrent Files:")
    for n in filter(lambda i: i.endswith(".save"), os.listdir(".")):
        print(n)
    file = input("Enter the file name: ")
    if not file.endswith(".save"):
        file = file + ".save"
    return file