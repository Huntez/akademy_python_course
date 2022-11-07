# string = input("Enter a string : ")
# print(string[::-1])

# Second

# string = input("Enter a string : ")
# ncount, dcount = 0, 0

# for a in string:
#     if a.isalpha():
#         ncount += 1
#     elif a.isdigit():
#         dcount += 1

# print("Symbol count :", ncount)
# print("Digit count :", dcount)

# Third

# string = input("Enter a string : ")
# symbol = input("Enter a symbol : ")

# print("Symbol count :", string.count(symbol))

# Fourth

# string = input("Enter a string : ")
# word = input("Enter a word : ")
# replace = input("Enter a replace : ")

# print(string.replace(word, replace))

# Five

text = '''If a column that you want to sort contains
both numbers and text—such as Product #15, Product #100,
Product #200—it may not sort as you expect.
You can format cells that contain 15, 100!,
and 200 so that they appear in the worksheet as Product #15,
Product #100, and! Product #200 '''


print(text.title())

count = 0
for a in text:
    if a.isdigit():
        count += 1

print("Digit count :", count)
print("Punctuation count :", int(text.count(",")) + int(text.count(".")))
print("Exclamation mark count :", text.count("!"))

count = 0
for i in text.split():
    if len(i) == 3:
        count += 1
print("Word == 3 :", count)
