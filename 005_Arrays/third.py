# acort = ("kia", "ford", "toyota", "ford", "ferrari", "mitsubishi")
# uenter = input("Enter a name : ")
# replace = input("Enter for replace : ")
# cort = []

# for a in acort:
#     if uenter == a:
#         cort.append(replace)
#     else:
#         cort.append(a)


# print(tuple(cort))

# Second

# from random import randint

# cort = tuple([randint(1, 200) for i in range(10)])
# print(cort)

# fcount, scount, tcount = 0, 0, 0
# for a in cort:
#     if len(str(a)) == 3:
#         tcount += 1
#     if len(str(a)) == 2:
#         scount += 1
#     if len(str(a)) == 1:
#         fcount += 1

#print(fcount, scount ,tcount)

# Third

# set_country = {"Ukraine", "USA", "Brazil", "Poland"}
# print(set_country)
# uenter = 0
# while(uenter != 7):
#     uenter = int(input("1, 2, 3, 4 : "))
#     if uenter == 1:
#         enter = input("Enter a country : ")
#         set_country.add(enter)
#         print(set_country)
#     elif uenter == 2:
#         enter = input("Enter a delete : ")
#         set_country.discard(enter)
#         print(set_country)
#     elif uenter == 3:
#         enter = input("Enter a symbols : ")
#         for a in set_country:
#             if enter in a:
#                 print("Found :", a)
#     elif uenter == 4:
#         enter = input("Enter a symbols : ")
#         if enter in set_country:
#             print("True :", set_country)
#         else:
#             print("False :", set_country)

# # Fourth

# fset = {"Kiyv", "Lviv", "Kriviy Rih", "Dnipro"}
# sset = {"Dnipro", "Kiyv", "Donetsk", "Poltava"}
# print(fset, "\n", sset)
# tset = fset.intersection(sset)
# print(tset)

# Five

fset = {"Kiyv", "Lviv", "Kriviy Rih", "Dnipro"}
sset = {"Dnipro", "Kiyv", "Donetsk", "Poltava"}
print(fset, sset)
print(fset.difference(sset))

# Six

fset = {"Kiyv", "Lviv", "Kriviy Rih", "Dnipro"}
sset = {"Dnipro", "Kiyv", "Donetsk", "Poltava"}
print(fset, sset)
print(sset.difference(fset))

# Seven

fset = {"Kiyv", "Lviv", "Kriviy Rih", "Dnipro"}
sset = {"Dnipro", "Kiyv", "Donetsk", "Poltava"}
tset = fset.symmetric_difference(sset)
print(fset, sset)
print(tset)
