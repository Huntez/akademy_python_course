from random import randint

list = ["+", "-", "*", "/"]
ucount = input("Enter : ")

for i in list:
    if i in ucount:
        number = ucount.split(i)
        if i == "+":
            print(int(number[0]) + int(number[1]))
        if i == "-":
            print(int(number[0]) - int(number[1]))
        if i == "*":
            print(int(number[0]) * int(number[1]))
        if i == "/":
            print(int(number[0]) / int(number[1]))


# Second

nlist = [randint(-10, 10) for a in range(15)]
dcount, ncount, mcount = 0, 0, 0

for a in nlist:
    if a < 0:
        mcount += 1
    if a > 0:
        dcount += 1
    if a == 0:
        ncount += 1

print("List :",nlist)
print("Min :", min(nlist), "Max :", max(nlist))
print("Min c :", mcount, "Pls c :", dcount, "Null c :", ncount)
