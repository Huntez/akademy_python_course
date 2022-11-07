# First

day = int(input("Number of day : "))

if day == 1:
    print("Monday")
elif day == 2:
    print("Tuesday")
elif day == 3:
    print("Wednesday")
elif day == 4:
    print("Thursday")
elif day == 5:
    print("Friday")
elif day == 6:
    print("Saturday")
elif day == 7:
    print("Sunday")
else:
    print("Incorrect number")

# Second

month = int(input("Number of month : "))

if day == 1:
    print("January")
elif day == 2:
    print("February")
elif day == 3:
    print("March")
elif day == 4:
    print("April")
elif day == 5:
    print("May")
elif day == 6:
    print("June")
elif day == 7:
    print("July")
elif day == 8:
    print("August")
elif day == 9:
    print("September")
elif day == 10:
    print("October")
elif day == 11:
    print("November")
elif day == 12:
    print("December")
else:
    print("Incorrect number")

# Third

number = int(input("Enter a number : "))

if number > 0:
    print("Number is positive")
elif number < 0:
    print("Number is negative")
else:
    print("Number is equal zero")

# Fourth

fnumber = int(input("Enter a first number : "))
snumber = int(input("Enter a second number : "))

if fnumber == snumber:
    print("First number equal second number")
elif fnumber != snumber and fnumber < snumber:
    print(fnumber, "\n", snumber)
else:
    print(snumber, "\n", fnumber)
