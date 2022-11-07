from curses.ascii import isdigit
from operator import ilshift
import os.path

# file = open(os.path.join("homework4", "text1.txt"), "r")
# sfile = open(os.path.join("homework4", "text2.txt"), "r")

# line = [i.replace("\n", "") for i in file]
# sline = [i.replace("\n", "") for i in sfile]

# for i in range(len(line)):
#     if line[i] != sline[i]:
#        print("Line :", line[i])
#        print("Sline :", sline[i])

# file.close(); sfile.close()

# Second

# file = open(os.path.join("homework4", "second.txt"), "r")
# sfile = open(os.path.join("homework4", "seconds.txt"), "w")

# symbols, vowels, consontans, digits = 0, 0, 0, 0
# lvowels = ["a", "e", "i", "o", "u"]
# lconsontans = ["b", "c", "d", "f", "g", "h", "j", "k", 
# "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]
# strings = len([i for i in file])

# file = open(os.path.join("homework4", "second.txt"), "r")
# line = file.read()

# for i in line.lower():
#     symbols += 1
#     if i in lvowels:
#         vowels += 1
#     if i in lconsontans:
#         consontans += 1
#     if i.isdigit():
#         digits += 1

# sfile.write("Symbols : " + str(symbols) + "\n")
# sfile.write("Strings : " + str(strings) + "\n")
# sfile.write("Vowels : " + str(vowels) + "\n")
# sfile.write("Consontans : " + str(consontans) + "\n")
# sfile.write("Digits : " + str(digits))

# file.close(); sfile.close()

# Third

# file = open(os.path.join("homework4", "text1.txt"), "r")
# sfile = open(os.path.join("homework4", "third.txt"), "w")

# line = [i for i in file]; line.pop(len(line)-1)

# for i in line:
#     sfile.write(i)

# file.close(); sfile.close()

# Fourth

# file = open(os.path.join("homework4", "text1.txt"), "r")

# line = [i.replace("\n", "") for i in file]
# print(max(line)); print("Len :", len(max(line)))

# file.close()

# Five

# file = open(os.path.join("homework4", "text1.txt"), "r")
# line = file.read(); line.replace("\n", ""); print(line)

# uchoice = input("Enter a word : ")
# print("Count :", line.count(uchoice))

# file.close()

# Six

file = open(os.path.join("homework4", "text1.txt"), "r")
line = file.read(); line.replace("\n", ""); print(line)

ureplace = input("Enter a word to replace : ")
uword = input("Enter a word : ")

print(line.replace(ureplace, uword))

file.close()
