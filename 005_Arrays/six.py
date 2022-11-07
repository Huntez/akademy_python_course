dict_dates= dict()
uenter = 0
while(uenter != 7):
    uenter = int(input("1 - add, 2 - pop, 3 - find, 4 - change : "))
    if uenter == 1:
        while True:
            enter = input("Enter a date : ")
            senter = input("Enter a time : ")
            if enter not in dict_dates:
                dict_dates[enter] = {}
            if senter not in dict_dates[enter]:
                tenter = input("Enter a deal : ")
                dict_dates[enter][senter] = tenter
                break
            else:
                print("This time is busy!")
        print(dict_dates)
    elif uenter == 2:
        enter = input("Enter a name : ")
        choice = int(input("1 - phone, 2 - email, 3 - all : "))
        if choice == 1:
            dict_dates[enter]["Phone"] = ""
        elif choice == 2:
            dict_dates[enter]["Email"] = ""
        elif choice == 3:
            dict_dates.pop(enter)
        print(dict_dates)
    elif uenter == 3:
        enter = input("Enter a name : ")
        choice = int(input("1 - phone, 2 - email : "))
        if choice == 1:
            print("Phone :", dict_dates[enter]["Phone"])
        elif choice == 2:
            print("Email :", dict_dates[enter]["Email"])
    elif uenter == 4:
        enter = input("Enter a name : ")
        choice = int(input("1 - phone, 2 - email : "))
        if choice == 1:
            senter = input("Enter a phone : ")
            dict_dates[enter]["Phone"] = senter
        elif choice == 2:
            senter = input("Enter a email : ")
            dict_dates[enter]["Email"] = senter
    elif uenter == 5:
        date = input("Date : ")
        time_check = []
        for i in dict_dates[date]:
            time_check.append(i.replace(":", ""))
        time_check.sort()
        for i in time_check:
            complete = i[:2] + ":" + i[2:]
            print(complete,":",dict_dates[date][complete])
