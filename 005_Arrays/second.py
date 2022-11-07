cort = ("apple", "apple", "bananaapple", "melon", "melon", "mango")
print(cort)
uenter = input("Enter a name : ")
print("Count :", cort.count(uenter))

count = 0
for a in cort:
    if uenter in a:
        count += 1
print(count)
