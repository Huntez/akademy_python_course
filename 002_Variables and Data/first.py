# Задание 1 Пользователь вводит с клавиатуры число.
# Необходимо проверить его на четность и нечетность.
# Если число четное требуется вывести на экран число и надпись Even number.
# Если число нечетное выведите на экран число и надпись Odd number.

a = int(input("Enter a number : "))

if a % 2 == 0:
    print("Even number")
else:
    print("Odd number")

# Задание 2 Пользователь вводит с клавиатуры число.
# Необходимо проверить его на кратность 7.
# Если число кратно требуется вывести на экран число и надпись
# Number is multiple 7. Если число не кратно выведите
# на экран число и надпись Number is not multiple 7.

b = int(input("Enter a number : "))

if b % 7 == 0:
    print("Number is multiple 7")
else:
    print("Number is not multiple 7")

# Задание 3 Пользователь вводит с клавиатуры два числа.
# Необходимо найти максимум из двух чисел и показать его на экран

c = int(input("Enter first number : "))
d = int(input("Enter second number : "))

if c > d:
    print("first bigger than second -", c)
else:
    print("second bigger than first -", d)

# Задание 5 Пользователь вводит с клавиатуры два числа.
# В зависимости от выбора пользователя нужно показать сумму двух чисел,
# разницу двух чисел, среднеарифметическое или произведение двух чисел.

first = int(input("Enter first number : "))
second = int(input("Enter secobd number : "))

print("1 - Summ of numbers")
print("2 - Diff of numbers")
print("3 - Avg of numbers")
print("4 - Multiply of numbers")
choice = int(input("Enter : "))

if choice == 1:
    print("Result :", first + second)
elif choice == 2:
    print("Result :", first - second)
elif choice == 3:
    print("Result :", (first + second) / 2)
elif choice == 4:
    print("result :", first * second)
else:
    print("Nothing of choice")
