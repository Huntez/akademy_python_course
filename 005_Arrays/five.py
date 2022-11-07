dict_pib= dict()
uenter = 0
while(uenter != 7):
    uenter = int(input("1 - add, 2 - pop, 3 - find, 4 - change : "))
    if uenter == 1:
        enter = input("Enter a name: ")
        senter = input("Enter phone : ")
        tenter = input("Enter a email : ")
        dict_pib[enter] = {"Phone": senter, "Email": tenter}
        print(dict_pib)
    elif uenter == 2:
        enter = input("Enter a name : ")
        choice = int(input("1 - phone, 2 - email, 3 - all : "))
        if choice == 1:
            dict_pib[enter]["Phone"] = ""
        elif choice == 2:
            dict_pib[enter]["Email"] = ""
        elif choice == 3:
            dict_pib.pop(enter)
        print(dict_pib)
    elif uenter == 3:
        enter = input("Enter a name : ")
        choice = int(input("1 - phone, 2 - email : "))
        if choice == 1:
            print("Phone :", dict_pib[enter]["Phone"])
        elif choice == 2:
            print("Email :", dict_pib[enter]["Email"])
    elif uenter == 4:
        enter = input("Enter a name : ")
        choice = int(input("1 - phone, 2 - email : "))
        if choice == 1:
            senter = input("Enter a phone : ")
            dict_pib[enter]["Phone"] = senter
        elif choice == 2:
            senter = input("Enter a email : ")
            dict_pib[enter]["Email"] = senter
    elif uenter == 5:
        print(dict_pib)