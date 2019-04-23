import os
list= [1,2,3,4,5]
file = '/home/tjlindow/list.txt'


def writeFile(list):
    with open(file, 'w') as f:
        f.write(str(list))
        f.close()
writeFile(list)



def readFile(file):
    with open(file, 'r') as f:
        filecontents = f.read()
        print(filecontents)
        f.close()
readFile(file)

def deleteFile(file):
    if os.path.exists("list.txt"):
        os.remove("list.txt")
        print("The file was deleted")
    else:
        print("The file does not exist")
deleteFile(file)
