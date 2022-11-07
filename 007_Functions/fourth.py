from random import randint
from random import shuffle

plist = [1,2,3,4,5,6,7,8]; shuffle(plist)
plist.insert(randint(1,8), " ")
fplist = [1,2,3,4,5,6,7,8," "]
enter = 0

while enter != 5:
    count = 0
    for i in plist:
        print(i, end=" ")
        count += 1
        if count % 3 == 0:
            print(end="\n")
    enter = int(input("1-l,2-r,3-u,4-d : "))
    if enter == 1:
        plist_ind = plist.index(" ")
        if plist_ind != 0 and plist_ind != 3 and plist_ind != 6:
            number = plist[plist_ind-1]
            plist[plist_ind] = number
            plist[plist.index(number)] = " "
    elif enter == 2:
        plist_ind = plist.index(" ")
        if plist_ind != 2 and plist_ind != 5 and plist_ind != 8:
            number = plist[plist_ind+1]
            plist[plist.index(number)] = " "
            plist[plist_ind] = number
    elif enter == 3:
        plist_ind = plist.index(" ")
        if plist_ind != 0 and plist_ind != 1 and plist_ind != 2:
            number = plist[plist_ind-3]
            plist[plist_ind] = number
            plist[plist.index(number)] = " "
    elif enter == 4:
        plist_ind = plist.index(" ")
        if plist_ind != 6 and plist_ind != 7 and plist_ind != 8:
            number = plist[plist_ind+3]
            plist[plist.index(number)] = " "
            plist[plist_ind] = number
    if plist == fplist:
        print("Finish!"); break   
