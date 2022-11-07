#Завдання 1
#Користувач вводить з клавіатури три числа. Розра-
#хуйте суму чисел та добуток чисел. Результати обчислень
#виведіть на екран.

first = int(input("Enter first number : "))
second = int(input("Enter Second number : "))
third = int(input("Enter third number : "))

print("Summ of number :", first + second + third)
print("Multiply of number : ", first * second * third)

# Завдання 2
# Користувач вводить з клавіатури три числа. Перше
# число — зарплата за місяць, друге число — сума місячного
# платежу за кредитом банку, третє число — заборгованість
# за комунальні послуги. Виведіть на екран суму, яка зали-
# шиться у користувача після всіх виплат.

pay_for_mounth = int(input("Enter a payday : "))
credit_for_bank = int(input("Enter credit in the bank : "))
duty = int(input("Enter a duty : "))

print("Balance after operations : ", pay_for_mounth -
      credit_for_bank - duty)

# Завдання 3
# Напишіть програму, яка підраховує площу ромба.
# Користувач вводить з клавіатури довжину двох його
# діагоналей.

f_diag = int(input("Enter first diag : "))
s_diag = int(input("Enter second diag : "))

print("Area of rhombus : ", (f_diag * s_diag) / 2)

# Завдання 4
# Виведіть на екран напис «To be or not to be» на різних
# рядках. Приклад виведення:
# To be
# or not
# to be.

print("To be \nor not \nto be")

# Завдання 5
# Виведіть на екран напис «Life is what happens when
# you’re busy making other plans. John Lennon» на різних ряд-
# ках. Приклад виведення:
# “Life is what happens
# when
# you’re busy making other plans”
# John Lennona

print("Life is what happens\n   when\n\tyou’re busy making other plans. \n\t\t\t   John Lennon")
