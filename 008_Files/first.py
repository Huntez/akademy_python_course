# import os.path
# # path = os.path.join("data_base", "test1.txt")
# # file = open(path, "w")
# # file.write("Hello world")
# # file.close()
# path = os.path.join("data_base", "test1.txt")
# file = open(path, "r")
# # for i in file:
# #     print(i)
# line = file.read()[5:10]qweqwea
# print(line)
# for i in line:
#     print(i)
# file.close()    

import os.path

# First

# file = open(os.path.join("lesson12", "some.txt"), "r")
# sfile = open(os.path.join("lesson12", "finish.txt"), "w")

# for i in file:
#     data = i.split()
#     for j in range(len(data)):
#         if len(data[j]) == 7:
#             print(data[j])
#             sfile.write(data[j]); sfile.write("\n")

# file.close(); sfile.close()
      
# file = open(os.path.join("lesson12", "some.txt"), "r")
# sfile = open(os.path.join("lesson12", "text.txt"), "w")

# line = file.read().split()
# for i in line:
#     if len(i) == 7:
#         sfile.write(i + "\n")

# file.close(); sfile.close()

# Third

# file = open(os.path.join("lesson12", "some.txt"), "r")
# sfile = open(os.path.join("lesson12", "text.txt"), "w")

# slist = list()
# for i in file:
#     slist.append(i)

# slist.reverse()

# for i in slist:
#     sfile.write(i)

# file.close(); sfile.close()

# Fourth

# Маємо текстовий файл. Додайте до нього рядок із
# дванадцяти зірочок (************), помістивши його після
# останнього з рядків, в яких немає коми. Якщо таких рядків
# немає, додайте новий після всіх рядків файлу. Результат
# запишіть до іншого файлу

file2 = open(os.path.join("lesson12", "text.txt"), "r")
file = open(os.path.join("lesson12", "fin.txt"), "w")

base_list = [i.replace("\n", "") for i in file2]
base_list.reverse()

for i in range(len(base_list)):
    if not "," in base_list[i]:
        base_list[i] = base_list[i] + "*"*12
        break
base_list.reverse()
for i in base_list:
    file.write(i + "\n")
    
file.close()


# Five

# file = open(os.path.join("lesson12", "some.txt"), "r")
# count, line = 0, file.read().split()

# uchoice = input("Enter a symbol : ")
# for i in line:
#         if i.startswith(uchoice):
#             print(i)
#             count += 1

# print("Count of words : ", count)

# Six

file = open(os.path.join("lesson12", "text.txt"), "r")
sfile = open(os.path.join("lesson12", "fin.txt"), "w")

line = file.read()
for i in line:
    if i == "*":
        sfile.write("&")
    elif i == "&":
        sfile.write("*")
    else:
        sfile.write(i)

