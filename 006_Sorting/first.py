from random import randint

numbers = [randint(1, 10) for i in range(10)]
print(numbers)

for i in range(len(numbers) - 1):
    for j in range(len(numbers) - i - 1):
        if numbers[j] > numbers[j+1]:
            number = numbers[j]
            numbers[j] = numbers[j+1]
            numbers[j+1] = number

print(numbers)

numbers = [randint(1, 10) for i in range(10)]
print("\n",numbers)

for i in range(1, len(numbers)):
    number = numbers[i]
    j = i-1
    while j>=0 and numbers[j] > number:
        numbers[j+1] = numbers[j]
        j = j - 1
    numbers[j+1] = number
print(numbers)

numbers = [randint(1, 10) for i in range(10)]
print(numbers)

m=len(numbers) // 2
left_list = numbers[:m]
right_list = numbers[m:]

for i in range(len(left_list) - 1):
    for j in range(len(left_list) - i - 1):
        if left_list[j] > left_list[j+1]:
            number = left_list[j]
            left_list[j] = left_list[j+1]
            left_list[j+1] = number
for i in range(len(right_list) - 1):
    for j in range(len(right_list) - i - 1):
        if right_list[j] > right_list[j+1]:
            number = right_list[j]
            right_list[j] = right_list[j+1]
            right_list[j+1] = number
print(left_list + right_list)
