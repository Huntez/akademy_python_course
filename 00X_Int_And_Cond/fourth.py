# First

fnumber = int(input("Enter a first number : "))
snumber = int(input("Enter a second number : "))
tnumber = int(input("Enter a third number : "))

choice = int(input("1 - summ, 2 - multiplay : "))

if choice == 1:
    print("Summ :", fnumber + snumber + tnumber)
else:
    print("Multiplay : ", fnumber * snumber * tnumber)

# Second

fnumber = int(input("Enter a first number : "))
snumber = int(input("Enter a second number : "))
tnumber = int(input("Enter a third number : "))

choice = int(input("1 - max, 2 - min, 3 - avg : "))

if choice == 1:
    if fnumber > snumber and fnumber > tnumber:
        print("Max :", fnumber)
    elif snumber > fnumber and snumber > tnumber:
        print("Max :", snumber)
    else:
        print("Max :", tnumber)
elif choice == 2:
    if fnumber < snumber and fnumber < tnumber:
        print("Min:", fnumber)
    elif snumber < fnumber and snumber < tnumber:
        print("Min:", snumber)
    else:
        print("Min:", tnumber)
else:
    print("Avg :", (fnumber + snumber + tnumber) / 3 )

# Third

meters = int(input('Enter a number of meters : '))
choice == int(input("1 - miles, 2 - inch, 3 - yards : "))

if choice == 1:
    print("Miles : ", meters / 1609)
elif choice == 2:
    print("Inch : ", meters * 39.37)
else:
    print("Yards : ", meters * 1.094)
