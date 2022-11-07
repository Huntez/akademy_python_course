while True:
    fnumber = int(input("Enter a fnumber : "))
    snumber = int(input("Enter a snumber : "))
    if fnumber < 9 and snumber < 9:
        print("Error, two number smaller than 9")
    else:
        break

hsumm, nsumm, esumm = 0, 0, 0
hcount, ncount, ecount = 0, 0, 0

for a in range(fnumber, snumber + 1):
    if a % 2 == 0:
        hsumm = hsumm + a
        hcount += 1
    elif a % 9 == 0:
        esumm = esumm + a
        ecount += 1
    else:
        nsumm = nsumm + a
        ncount += 1

print("Even summ :", hsumm, "Avg : ", hsumm / hcount)
print("Odd summ :", nsumm, "Avg : ", nsumm / ncount)
print("Multiple of 9 summ :", esumm, "Avg : ", esumm / ecount)


# Second

size_of_line = int(input("Enter size of line : "))
symbol = input("Enter a symbol : ")

a = 0

for a in range(1, size_of_line + 1):
    print(symbol)


# Third

while True:
    number = int(input("Enter a number : "))
    if number == 7:
        print("Godbay!")
        break
    elif number > 0:
        print("Number is positive")
    elif number < 0:
        print("Number is negative")
    else:
        print("Number is equal to zero")

# Fourth

summ = 0
number = int(input("Enter a number : "))
mmax = number
mmin = mmax
while True:
    summ += number
    if number == 7:
        print("Godbay!")
        break
    elif number > mmax:
        mmax = number
    elif number < mmin:
        mmin = number
    number = int(input("Enter a number : "))

print("Summ :", summ)
print("Min :", mmin)
print("Max :", mmax)
