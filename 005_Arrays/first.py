# list = ["1", "32", "18", "18", "del", "hello", "world"]
# print(list)

# uinp = input("Enter a element : ")
# print("Count : ", list.count(uinp))

# Second

# list = [int(input("Enter : ")) for i in range(3)]
# print(sum(list) / 3)

# Third

# count, summ = 0, 0
# list = ["+", "-", "*", "/"]
# ucount = input("Enter : ")
# for a in range(len(list)):
#     if list[count] in ucount:
#         for a in ucount.split("+"):
#             summ list[count]= int(a)
#         count += 1
# print(summ)

# Third

from random import randint

list = [randint(-10, 10) for i in range(10)]
print("List :",list)
print("Парные :", sum([i for i in list if i % 2 == 0]))
print("Меньше нуля :", sum([i for i in list if i < 0]))
print("Кратные двум :", sum([i for i in list if i % 2 != 0]))
print("Index % 3 :", sum([i for i in list if list.index(i) % 3 == 0]))
if list.index(min(list)) < list.index(max(list)):
    list2 = list[list.index(min(list)):list.index(max(list)) + 1]
    print("Summ min and max :", sum(list2))
else:
    list2 = list[list.index(max(list)):list.index(min(list)) + 1]
    print("Summ min and max :", sum(list2))
list3 = [i for i in list if i > 0]
print(sum(list[list.index(list3[0]):list.index(list3[-1] + 1)]))
