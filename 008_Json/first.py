import os.path

base = ["Name", "Second name", "Age", "Position"]
enter = 0
while enter != 5:
    enter = int(input("1 - add, 2 - find, 3 - del : "))
    if enter == 1:
        count = 0
        file = open(os.path.join("lesson14", "base.txt"), "a")
        while count < len(base):
            file.write(input(base[count] + " : ") + " ")
            count += 1
        file.write("\n")
    if enter == 2:
        choice = int(input("1 - sname, 2 - all age, 3 - some : "))
        if choice == 1:
            file = open(os.path.join("lesson14", "base.txt"), "r")
            uenter = input("Enter name : ")
            for i in file:
                for j in i.split():
                    if uenter == j:
                        print(i.replace("\n", "")); break
        elif choice == 2:
            file = open(os.path.join("lesson14", "base.txt"), "r")
            uenter = input("Enter age : ")
            for i in file:
                for j in i.split():
                    if uenter == j:
                        print(i.replace("\n", ""))
        elif choice == 3:
            file = open(os.path.join("lesson14", "base.txt"), "r")
            uenter = input("Enter name : ")
            senter = int(input("1 - sname, 2 - age, 3 - position : "))
            for i in file:
                if uenter in i:
                    print(i.split()[senter]); break                  
    if enter == 3:
        file = open(os.path.join("lesson14", "base.txt"), "r")
        uenter = input("Enter name : ")
        line = [i for i in file]
        print(line)
        for i in line:
            for j in i.split():
                if uenter == j:
                    del line[line.index(i)]; break
        file = open(os.path.join("lesson14", "base.txt"), "w")
        for i in line:
            file.write(i)
