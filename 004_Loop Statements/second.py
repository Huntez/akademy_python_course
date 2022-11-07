from random import randint

# count = int(input("Enter a size of desk : "))

# for a in range(1, count + 1):
#      print(("*" * count + "_" * count) * 3)
#      print(("_" * count + "*" * count) * 3)

# Second
#
# gcount, bcount, enter, randc = 0, 0, 0, 0
# while(enter != 7):
#     enter = int(input("1 - e, 2 - m, 3 - h : "))
#     if enter == 1:
#         randc = 9
#     elif enter == 2:
#         randc = 99
#     elif enter == 3:
#         randc = 999
#     elif enter == 7:
#         print("End of game")
#         break
#     fnumber = randint(1, randc)
#     snumber = randint(1, randc)
#     print(fnumber, "*", snumber)
#     uenter = int(input("Enter a number : "))
#     if uenter == fnumber * snumber:
#         print("Congrutilations!")
#         gcount += 1
#     else:
#         print("Bad result")
#         bcount += 1

# print("\nSuccess count :", gcount)
# print("Failed count :", bcount)

# if gcount > bcount:
#     print("Good result")
# else:
#     print("Bad result")


# Third

c = 6
d = 6

# for a in range(1, 5):
#     print(" " * int(d / a) + "*" * int(a - 1), "*" * int(a / d))
#     if a == 4:
#         for b in range(2, 4):
#             print(" " * int(d * b / c) + "*")
