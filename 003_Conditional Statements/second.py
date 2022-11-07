fnumber = int(input("Enter first number : "))
snumber = int(input("Enter second number : "))

summ = 0

for a in range(fnumber, snumber + 1):
    summ = summ + a
    if a == snumber:
        print(summ)
        print(summ / a)

# Second

facto = int(input("Enter a facto number : "))

a = 0
f = 1
while a < facto:
    a = a + 1
    f = f * a
    if a == facto:
        print(f)

a = 0
f = 1
for a in range(1, facto + 1):
    f = f * a
    if a == facto:
        print(f)


# third

count = int(input("Enter a count : "))

a = 0
while a < count:
    a = a + 1
    #print("*", end="")
    if a == count:
        print("*" * count, "\n")

# fourth

multiply = int(input("Enter a multiply number : "))

a = 0
summ = 0
for a in range(1, 9 + 1):
    summ = multiply * a
    print(multiply, "*", a, "=", summ)


# fifth

fnumber = int(input("Enter first number : "))
snumber = int(input("Enter second number : "))

a = 0
while True:
    diap = int(input("Enter a diap : "))
    if diap >= fnumber and diap <= snumber:
        for a in range(fnumber, snumber + 1):
            if a == diap:
                print("!" + str(a) + "!")
            else:
                print(a)
        break
    else:
        print("Enter a correct number")
