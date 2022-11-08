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

## 003 - Conditional Statements
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

