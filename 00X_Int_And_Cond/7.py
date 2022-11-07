x = int(input("Enter x : "))
y = int(input("Enter y : "))

summ = x
for a in range(1, y ):
        summ = summ * x

print(summ)

# Second

fcount = 0
for a in range(100, 999):
    fn = (a // 100) % 10
    sn = (a // 10) % 10
    tn = a % 10
    if fn == sn or fn == tn or sn == tn:
        fcount += 1

print("Count of numbers :", fcount)

# third

fcount = 0
for a in range(100, 9999):
    bn = (a // 1000) % 10
    fn = (a // 100) % 10
    sn = (a // 10) % 10
    tn = a % 10
    if bn != fn and bn != sn and bn != tn and fn != sn and fn != tn and sn != tn:
        fcount += 1

print("Count of numbers :", fcount)

# Fourth

name = input("Enter a number : ")
new_number = ""

for i in name:
    if i != "6" and i != "3":
        new_number += i

print(new_number)
