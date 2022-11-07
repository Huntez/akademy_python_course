fnumber = int(input("Enter a first number : "))
snumber = int(input("Enter a second number : "))

for a in range(fnumber, snumber + 1):
    if a % 7 == 0:
        print(a)


# Second

fnumber = int(input("Enter a first number : "))
snumber = int(input("Enter a second number : "))

a = 0
for a in range(fnumber, snumber + 1):
    print(a)

a = 0
print("Reverse numbers")
for a in range(snumber, fnumber -1, -1):
    print(a)

print("Number multiples 7")
ccount, a = 0, 0
for a in range(fnumber, snumber + 1):
    if a % 7 == 0:
        print(a)

count, a = 0, 0
for a in range(fnumber, snumber + 1):
    if a % 5 == 0:
        count += 1
print("Count of numbers multiples 5 :", count)

# third

fnumber = int(input("Enter a first number : "))
snumber = int(input("Enter a second number : "))

a = 0
for a in range(fnumber, snumber + 1):
    if a % 3 == 0 and a % 5 == 0:
        print("Fizz Buzz")
    elif a % 3 == 0:
        print("Fizz")
    elif a % 5 == 0:
        print("Buzz")
    else:
        print(a)
