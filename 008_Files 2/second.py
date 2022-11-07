import os.path
from xml.etree.ElementTree import TreeBuilder

# file = open(os.path.join("lesson13", "stext.txt"), "r")
# sfile = open(os.path.join("lesson13", "swrong.txt"), "r")
# tfile = open(os.path.join("lesson13", "sfin.txt"), "w")

# # line = [i for i in file]
# lwrong = [i.replace("\n", "") for i in sfile]

# # for i in range(len(line)):
# #     for j in line[i].split():
# #         if j in lwrong:
# #             line[i] = line[i].replace(j, "")

# line = file.read(); print(line + "\n")
# for i in lwrong:
#     print(i)
#     line = line.replace(i, "")

# tfile.write(line); print("\n" + line)

# file.close(); sfile.close(); tfile.close()

# Second

# file = open(os.path.join("lesson13", "stfirst.txt"), "w")
# sfile = open(os.path.join("lesson13", "stsecond.txt"), "w")

# while True:
#     enter = input("Enter first word : ")
#     if enter == "quit":
#         break
#     senter = input("Enter second word : ")
#     file.write(enter+"\n"); sfile.write(senter+"\n")

# file = open(os.path.join("lesson13", "stfirst.txt"), "r")
# sfile = open(os.path.join("lesson13", "stsecond.txt"), "r")

# line = [i for i in file.read().split()]
# sline = [i for i in sfile.read().split()]
# print(line, sline)

# while True:
#     enter = input("Enter a word : ")
#     if enter == "quit":
#         break
#     print("Result :", enter, ":", sline[line.index(enter)])
    

# Third

# enter, line = "", ""
# while True:
#     enter = input("Enter a word : ")
#     if enter == "quit":
#         break
#     file = open(os.path.join("lesson13", enter+".txt"), "r")
#     line += file.read()

# sfile = open(os.path.join("lesson13", "stfin.txt"), "w")
# sfile.write(line)

# Fourth

enter, line = "", ""
while True:
    enter = input("Enter a word : ")
    if enter == "quit":
        break
    file = open(os.path.join("lesson13", enter+".txt"), "r")
    line += file.read()
