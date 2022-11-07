# dict_basket= dict()
# uenter = 0
# while(uenter != 7):
#     uenter = int(input("1 - add, 2 - pop, 3 - find, 4 - change : "))
#     if uenter == 1:
#         enter = input("Enter a PIB : ")
#         senter = input("Enter a height : ")
#         dict_basket[enter] = senter
#         print(dict_basket)
#     elif uenter == 2:
#         enter = input("Enter a delete : ")
#         dict_basket.pop(enter)
#         print(dict_basket)
#     elif uenter == 3:
#         enter = input("Enter a name : ")
#         print("Height : ", dict_basket.get(enter))
#     elif uenter == 4:
#         enter = input("Enter a PIB for change : ")
#         senter = input("Enter a height : ")
#         dict_basket.update({enter: senter})
#         print(dict_basket)
#     elif uenter == 5:
#         print(dict_basket)


# Second

# dict_words= dict()
# uenter = 0
# while(uenter != 7):
#     uenter = int(input("1 - add, 2 - pop, 3 - find, 4 - change : "))
#     if uenter == 1:
#         enter = input("Enter a word on english : ")
#         senter = input("Enter a french translate : ")
#         dict_words[enter] = senter
#         print(dict_words)
#     elif uenter == 2:
#         enter = input("Enter a delete : ")
#         dict_words.pop(enter)
#         print(dict_words)
#     elif uenter == 3:
#         enter = input("Enter a word : ")
#         print("French tranlsate", dict_words.get(enter))
#     elif uenter == 4:
#         enter = input("Enter a word for change : ")
#         senter = input("Enter a translate : ")
#         dict_words.update({enter: senter})
#         print(dict_words)
#     elif uenter == 5:
#         print(dict_words)


# Third

# uenter, dict_pib= 0, dict()
# data = ("Phone", "Email", "Position", "Cab number", "Skype")

# while(uenter != 7):
#     uenter = int(input("1 - add, 2 - pop, 3 - find, 4 - change : "))
#     if uenter == 1:
#         enter = input("Enter a PIB : ")
#         while True:
#             if enter not in dict_pib:
#                 dict_pib[enter] = {}
#                 break
#             else:
#                 print("This PIB is busy!")
#         for a in data:
#             dict_pib[enter][a] = input("Enter " + a + " : ")
#     elif uenter == 2:
#         enter = input("Enter a name : ")
#         if enter not in dict_pib:
#             print("Dict dont have this PIB!")
#         else:
#             choice = int(input("1 - some, 2 - all : "))
#             if choice == 1:
#                 print(*data, sep=", ", end="")
#                 senter = input(" : ")
#                 dict_pib[enter][senter] = ""
#             elif choice == 2:
#                 dict_pib.pop(enter)
#     elif uenter == 3:
#         enter = input("Enter a PIB : ")
#         if enter not in dict_pib:
#             print("Dict dont have this PIB!")
#         else:
#             for a in dict_pib[enter]:
#                 print(a, " : ", dict_pib[enter][a])
#     elif uenter == 4:
#         enter = input("Enter a name : ")
#         if enter not in dict_pib:
#             print("Dict dont have this PIB!")
#         else:
#             print(*data, sep=", ", end="")
#             senter = input(" : ")
#             dict_pib[enter][senter] = input("Enter " + senter + " : ")


# Fourth

uenter, dict_book= 0, dict()
data = ("Genre", "Date", "Page numbers", "Publisher")

while(uenter != 7):
    uenter = int(input("1 - add, 2 - pop, 3 - find, 4 - change : "))
    if uenter == 1:
        enter = input("Enter a author : ")
        while True:
            benter = input("Enter book name : ")
            if enter not in dict_book:
                dict_book[enter] = {}
            if benter not in dict_book[enter]:
                dict_book[enter][benter] = {}; break
            else:
                print("This name is busy!")
        for a in data:
            dict_book[enter][benter][a] = input("Enter " + a + " : ")
    elif uenter == 2:
        enter = input("Enter a author : ")
        if enter not in dict_book:
            print("Dict dont have this author!")
        else:
            choice = int(input("1 - some in book, 2 - book , 3 - all : "))
            if choice == 1:
                print(*data, sep=", ", end="")
                senter = input(" : ")
                dict_book[enter][input("Enter book name : ")][senter] = ""
            elif choice == 2:
                #benter = input("Enter book name : ")
                del dict_book[enter][input("Enter book name : ")]
            elif choice == 3:
                dict_book.pop(enter)
    elif uenter == 3:
        enter = input("Enter a author : ")
        if enter not in dict_book:
            print("Dict dont have this author!")
        else:
            choice = int(input("1 - some, 2 - all : "))
            if choice == 1:
                benter = input("Enter book name : ")
                for a in dict_book[enter][benter]:
                    print(a, ":", dict_book[enter][benter][a])
            elif choice == 2:
                for a, b in dict_book[enter].items():
                    print("Book :", a)
                    for i in b:
                        print(i, ":", b[i])
    elif uenter == 4:
        enter = input("Enter a name : ")
        if enter not in dict_book:
            print("Dict dont have this author!")
        else:
            benter = input("Enter book name : ")
            print(*data, sep=", ", end="")
            senter = input(" : ")
            dict_book[enter][benter][senter] = input("Enter " + senter + " : ")
