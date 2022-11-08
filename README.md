# __Python files from akademy course__

## Warning!
all written code is outdated and does not reflect real skills

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

## Module 004 Loop Statements
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
