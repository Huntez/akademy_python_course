# from random import randint

# number = randint(1, 500)
# print(number)
# useri, count = 0, 0
# while (useri != number):
#     useri = int(input("Enter a number : "))
#     count += 1
#     if useri == number:
#         print("Congratulations!")
#     elif useri > number:
#         print("Input bigger than number!")
#     elif useri < number:
#         print("Input smaller than number!")

# print("Count of trys : ", count)

# # Second

# csize = int(input("Enter a size of cube : "))

# a = 0
# while(a < csize):
#     print("*" * csize)
#     a += 1

# Third

# csize = int(input("Enter a weight of cube : "))
# hsize = int(input("Enter a height of cube : "))

# a = 0
# while(a < hsize):
#     print("*" * csize)
#     a += 1

# Fourth

# csize = int(input("Enter a weight of cube : "))
# hsize = int(input("Enter a height of cube : "))

# a = 0
# print("* " * csize)
# while(a < hsize):
#     print("* " + "  " * (csize - 2) + "*")
#     a += 1
# print("* " * csize)


# fifth

enumber = (input("Enter a number : "))
choice, count, summ, a = 0, 0, 0, 0

while(choice != 7):
    choice = int(input("1 - c, 2 - s & avg, 3 - cnull : "))
    if choice == 1:
        for a in enumber:
            count += 1
        print("Count :", count)
    elif choice == 2:
        count = 0
        for a in enumber:
            summ += int(a)
            count += 1
        print("Summ :", summ, "Avg", summ / count)
    elif choice == 3:
        count = 0
        for a in enumber:
            if a == "0":
                count += 1
        print("Null count :", count)
