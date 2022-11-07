#Завдання 1
#Користувач вводить з клавіатури два числа. Вкажіть
#усі числа у заданому діапазоні.

fnumber = int(input("Enter first number : "))
snumber = int(input("Enter second number : "))

for a in range(fnumber, snumber + 1):
    print(a)


# Second

fnumber = int(input("Enter first number : "))
snumber = int(input("Enter second number : "))

for a in range(fnumber, snumber + 1):
    if a % 2 != 0:
        print(a)

# Third

fnumber = int(input("Enter first number : "))
snumber = int(input("Enter second number : "))

if fnumber > snumber:
    for a in range(snumber, fnumber + 1):
        if a % 2 !=0:
            print(a)
else:
    for a in range(fnumber, snumber + 1):
        if a % 2 !=0:
            print(a)

# Fourth

fnumber = int(input("Enter first number : "))
snumber = int(input("Enter second number : "))

# for a in range(fnumber - 1, snumber):
#     print(snumber - a)

for a in range(snumber, fnumber -1, -1):
    print(a)
