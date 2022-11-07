#Користувач вводить з клавіатури три цифри. Створіть
#число, яке містить ці цифри. Наприклад, якщо з клавіатури
#введено 1, 5, 7, ви маєте сформувати число 157.

first = input('Enter first number : ')
second = input('Enter second number : ')
third = input('Enter third number : ')

print("Full number :", first + second + third)

#Користувач вводить з клавіатури число, яке складається
#із чотирьох цифр, а ви маєте знайти їх добуток. Наприклад,
#якщо з клавіатури введено 1324, то результат добутку буде
#1*3*2*4 = 24.

number = int(input("Enter a number : "))

print(number // 1000)
print((number // 100) % 10)
print((number // 10) % 10)
print((number // 1) % 10)

print("Result of multiply : ", (number // 1000) *
      ((number // 100) % 10) * ((number // 10) % 10) *
      ((number // 1) % 10 ))

#Користувач вводить з клавіатури якусь кількість метрів.
#Виведіть результат конвертування метрів у сантиметри, де-
#циметри, міліметри, милі
meters = int(input('Enter a number of meters : '))

print("Cantimeters : ", meters * 100)
print("Milimeters : ", meters * 1000)
print("Decimeters : ", meters * 10)
print("Miles : ", meters / 1609)

#Напишіть програму, яка обчислює площу трикутника.
#Користувач вводить з клавіатури розмір основи трикутника
#та його висоту

size_of_triangle = int(input('Enter a size of triangle : '))
height_of_triangle = int(input('Enter a height of triangle : '))

print('Area of triangle : ', 1/2 * (size_of_triangle * height_of_triangle))

#Користувач вводить з клавіатури чотиризначне число.
#Переверніть це число і виведіть результат. Наприклад, якщо
#введено 4512, результат буде 2154.

r_number = int(input("Number for reverse : "))

print("Result of reverse : {}{}{}{}" .format(((r_number // 1) % 10),
      ((r_number // 10) % 10), ((r_number // 100) % 10),
      (r_number // 1000)))
