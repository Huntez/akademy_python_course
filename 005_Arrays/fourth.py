#!/usr/bin/env python3

# dict_country = {"Ukraine" : "Kyiv",
#                "USA" : "Washington",
#                "Brazil" : "Brasilia",
#                "Poland" : "Warsaw"}
# print(dict_country)
# uenter = 0
# while(uenter != 7):
#     uenter = int(input("1, 2, 3, 4 : "))
#     if uenter == 1:
#         enter = input("Enter a country : ")
#         senter = input("Enter a capital : ")
#         dict_country.update({enter: senter})
#         print(dict_country)
#     elif uenter == 2:
#         enter = input("Enter a delete : ")
#         dict_country.pop(enter)
#         print(dict_country)
#     elif uenter == 3:
#         enter = input("Enter a symbols : ")
#         print("Found :", dict_country.get(enter))
#     elif uenter == 4:
#         enter = input("Enter a symbols : ")
#         if enter in dict_country:
#             print("True :", dict_country)
#         else:
#             print("False :", dict_country)


# Second

# itstep = "itstep"
# itstep_dict = {
#     "i" : itstep.count("i"),
#     "t" : itstep.count("t"),
#     "s" : itstep.count("s"),
#     "e" : itstep.count("e"),
#     "p" : itstep.count("p")
# }

# print(itstep_dict)

# Third


word = input("Enter a word : ")

some_dict = dict()
for a in word.replace(" ", ""):
    some_dict[a] = word.count(a)

print(some_dict)

# Fourth

# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

# number_dict = dict()
# # for i in a:
# #     number_dict[i] = b[a.index(i)]

# for i in range(len(a)):
#     number_dict[a[i]] = b[i]

# print(number_dict)

# from random import randint

# a = [randint(1, 20) for i in range(10)]

# a_dict = dict()
# for i in a:
#     if i % 2 == 0:
#         a_dict[i] = i * 2

# print(a)
# print("Result :", a_dict)
