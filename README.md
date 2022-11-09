# __Python files from akademy course__

## Support
Testing on python __3.10.8__ with arch linux

## TODO

- [ ] Making more readable

## Module 001 - Introduction
Basic python programs written with vscode
<details><summary>Example</summary>
<p>

```python
number = int(input('Enter number : '))
print("result :", number // 10, "," , number % 10)
```

</p>
</details>

## Module 002 - Variables and Data

Working with different data types

<details><summary>Example</summary>
<p>

```python
size_of_file = int(input("Enter a size_of_file : "))
speed = int(input("Enter a connection speed : "))
time = (size_of_file * 1000) / (speed / 800000)
print(time)
```

</p>
</details>

## Module 003 - Conditional Statements
Working with if else conditional and someting with loops

<details><summary>Example</summary>
<p>

```python
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
```

</p>
</details>

## Module 004 - Loop Statements
Advanced working with loops(for, while)

<details><summary>Example</summary>
<p>

```python
enumber = (input("Enter a number : "))
choice, count, summ, a = 0, 0, 0, 0

while(choice != 7):
    choice = int(input("1 - c, 2 - s & avg, 3 - cnull : "))
    if choice == 1:
        for a in enumber:
            count += 1
        print("Count :", count)
    elif choice == 2:
        count = 0
        for a in enumber:
            summ += int(a)
            count += 1
        print("Summ :", summ, "Avg", summ / count)
    elif choice == 3:
        count = 0
        for a in enumber:
            if a == "0":
                count += 1
        print("Null count :", count)
```

</p>
</details>

## Module 005 - Arrays
Working with different data types 

<details><summary>Example</summary>
<p>

__Working with nested dictionaries with using a loops__
    
```python
uenter, dict_book= 0, dict()
data = ("Genre", "Date", "Page numbers", "Publisher")

while(uenter != 7):
    uenter = int(input("1 - add, 2 - pop, 3 - find, 4 - change : "))
    if uenter == 1:
        enter = input("Enter a author : ")
        while True:
            benter = input("Enter book name : ")
            if enter not in dict_book:
                dict_book[enter] = {}
            if benter not in dict_book[enter]:
                dict_book[enter][benter] = {}; break
            else:
                print("This name is busy!")
        for a in data:
            dict_book[enter][benter][a] = input("Enter " + a + " : ")
    elif uenter == 2:
        enter = input("Enter a author : ")
        if enter not in dict_book:
            print("Dict dont have this author!")
        else:
            choice = int(input("1 - some in book, 2 - book , 3 - all : "))
            if choice == 1:
                print(*data, sep=", ", end="")
                senter = input(" : ")
                dict_book[enter][input("Enter book name : ")][senter] = ""
            elif choice == 2:
                #benter = input("Enter book name : ")
                del dict_book[enter][input("Enter book name : ")]
            elif choice == 3:
                dict_book.pop(enter)
    elif uenter == 3:
        enter = input("Enter a author : ")
        if enter not in dict_book:
            print("Dict dont have this author!")
        else:
            choice = int(input("1 - some, 2 - all : "))
            if choice == 1:
                benter = input("Enter book name : ")
                for a in dict_book[enter][benter]:
                    print(a, ":", dict_book[enter][benter][a])
            elif choice == 2:
                for a, b in dict_book[enter].items():
                    print("Book :", a)
                    for i in b:
                        print(i, ":", b[i])
    elif uenter == 4:
        enter = input("Enter a name : ")
        if enter not in dict_book:
            print("Dict dont have this author!")
        else:
            benter = input("Enter book name : ")
            print(*data, sep=", ", end="")
            senter = input(" : ")
            dict_book[enter][benter][senter] = input("Enter " + senter + " : ")
```

</p>
</details>

## Module 006 - Sorting
Different sorting algorythms

<details><summary>Example</summary>
<p>
    
__Optimized bubble sort__

```python

list = [5,7,4,3,8,2]
for i in range(len(list) - 2):
    for j in range(len(list) - 1 - i):
         if list[j] > list[j+1]:
            list[j], list[j+1] = list[j+1], list[j]

print(list)
```

</p>
</details>

## Module 007 - Functions
Working with functions

<details><summary>Example</summary>
<p>
    
__Number pow__

```python
def spow(a, b):
    slpow = []
    for i in a:
        ssum = 1
        for j in range(b):
            ssum *= i
        slpow.append(ssum)
    return slpow

flist = [randint(1, 10) for i in range(5)]; print(flist)
print("Pow res : ", spow(flist, int(input("Enter a pow : "))))

print(list)
```

</p>
</details>

## Module 008 - Files
Working with files

<details><summary>Example</summary>
<p>
    
__Word replacer__

```python
file = open(os.path.join("homework4", "text1.txt"), "r")
line = file.read(); line.replace("\n", ""); print(line)

ureplace = input("Enter a word to replace : ")
uword = input("Enter a word : ")

print(line.replace(ureplace, uword))

file.close()

print(list)
```

</p>
</details>

## Module 009 - OOP
Working with OOP and Exceptions, Raise etd...

<details><summary>Example</summary>
<p>
    
__Sun angle calculation__

```python
class SundontSee(Exception):
    pass

while True:
    try:
        time = input("Time : ")
        stime = [int(i) for i in time.split(":")]
    except(ValueError):
        print("Kva")
    else:
        break
    
if stime[0] >= 18 and stime[0] <= 24 or stime[0] >= 0 and stime[0] < 6:
    raise SundontSee("I dont see sun!")
else:
    print(((stime[0] - 6) * 15) + stime[1] * 0.25)
```

</p>
</details>

## Module 010 - PYMSQL
Working with MYSQL database, making menus etc...

<details><summary>Example</summary>
<p>
    
__Login into MYSQL database and authorization algorithm__

```python
import pymysql
try:
    connection = pymysql.connect(
        host="localhost",
        port=3306,
        user="root",
        password="2255",
        database="koshikDB",
        cursorclass=pymysql.cursors.DictCursor)
    print("Okay!")
    with connection.cursor() as cursor:
        while True:
            try:
                username = input("Enter a username : ")
                password = input("Enter a password : ")
            except Exception as error:
                print(error)
            cursor.execute(f"select login from koshikDB.Logins where username = '{username}'")
            password_check = cursor.fetchall()
            try:
                if password_check[0].get('login') == password:
                    print("Okay!"); break
                else:
                    print("Bad password!")
            except:
                print("Incorrect user")
```

</p>
</details>

