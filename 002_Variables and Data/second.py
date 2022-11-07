# Задание 1 Пользователь вводит с клавиатуры время в секундах,
# прошедшее с начала дня. В зависимости от выбора пользователя
# посчитать, сколько часов, минут и секунд осталось до полуночи.

seconds = int(input("Enter a seconds : "))
choice = int(input("1 - h, 2 - m, 3 - s : "))

if choice == 1:
    print("Hours :", int(24 - seconds / 3600))
elif choice == 2:
    print("Minutes :", int(1440 - seconds / 60))
else:
    print("Seconds :", 86400 - seconds)

# Задание 2 Пользователь вводит с клавиатуры диаметр окружности.
# В зависимости от выбора пользователя посчитать
# площадь или периметр окружности.

diam = int(input("Enter a diam : "))
dchoice = int(input("1 - ploshad , 2 - perim : "))

if dchoice == 1:
    print("Ploshad : ", (diam * diam) / 4 * 3.14)
elif dchoice == 2:
    print("Perim", diam * 3.14)

# Задание 3 Пользователь вводит с клавиатуры стоимость
# одной игровой приставки, их количество и процент скидки.
# В зависимости от выбора пользователя посчитать общую
# сумму заказа или стоимость одной приставки с учетом скидки.

price = int(input("Enter a price : "))
pchoice = int(input("1 - order, 2 - price of one : "))

if pchoice == 1:
    count = int(input("Enter a count : "))
    print("Order price : ", price * count)
elif pchoice == 2:
    procent = i nt(input("Enter a procent : "))
    print("Price with procent : ", price - price * procent / 100)

# Задание 4 Пользователь вводит с клавиатуры размер файла
# в гигабайтах и скорость интернет-соединения в битах в секунду.
# В зависимости от выбора пользователя посчитать,
# за сколько часов или минут, или секунд скачается файл.

size_of_file = int(input("Enter a size_of_file : "))
speed = int(input("Enter a connection speed : "))
#schoice = int(input("1 - h, 2 - m, 3 - s : "))
time = (size_of_file * 1000) / (speed / 800000)
print(time)
# if schoice == 1:
#     print("O ", price * count)
# elif schoice == 2:
#     print("Price with procent : ", price - price * procent / 100)
# else:
#     break
