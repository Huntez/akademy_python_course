import os.path
import json

file = open(os.path.join("lesson14", "third.json"), "r")
sdict = json.load(file)
enter = 0
while enter != 5:
    enter = int(input("1 - add, 2 - search, 3 - del : "))
    if enter == 1:
        file = open(os.path.join("lesson14", "third.json"), "w")
        uenter = input("Name : "); senter = input("Sname : ")
        tenter = input("Age : ")
        sdict[uenter] = {"Sname": senter, "Age": tenter}
        json.dump(sdict, file)
    if enter == 2:
        file = open(os.path.join("lesson14", "third.json"), "r")
        senter = int(input("1 - name, 2 - age, 3 - all : "))
        if senter == 1:
            uenter = input("Enter name : ")
            if uenter in sdict:
                for i in sdict[uenter]:
                    print(i + " : " + sdict[uenter][i])
            else:
                print("Nothing find!")
        elif senter == 2:
            uenter = input("Enter age : ")
            for i in sdict:
                for j in sdict[i]:
                    if sdict[i][j] == uenter:
                        print(i, ":", sdict[i])
        elif senter == 3:
            for i in sdict:
                print(i)
                for j in sdict[i]:
                    print(j, ":", sdict[i][j])
    if enter == 3:
        file = open(os.path.join("lesson14", "third.json"), "w")
        uenter = input("Enter name : ")
        if uenter in sdict:
            sdict.pop(uenter); json.dump(sdict, file)
        else:
            print("Nothing to delete!")
        
            

            
    