# def string_display(fstring):
#     return(fstring)


# print(string_display("Don't let the noise of others' opinion\ndrown out you own inner voice.\n\t\t\tSteve Jobs"))


# Second

# def some(a,b):
#     numbers = []
#     for i in range(a+1,b):
#         if i % 2 != 0:
#             numbers.append(i)
#     return numbers

# print(some(int(input("First : ")),int(input("Second : "))))

# Third

# def line(a,b,c):
#     if b == 1:
#         for i in range(a):
#             print(c)
#     elif b == 2:
#         print(c*a)

# line(int(input("W : ")),int(input("D : ")),input("Sa : "))

# Fourth

# def some(a,b,c,d):
#     return max(a,b,c,d)

# print(some(input("1 : "), input("2 : "), input("3 : "), input("4 : ")))

# Five

# def some(a,b):
#     summ = 0
#     for i in range(a,b+1):
#         summ += i
#     return summ

# print(some(int(input("First : ")),int(input("Second : "))))

# Six

def some(a):
    count = 0
    for i in range(1,a):
        if a % i == 0 and i != a:
            count += 1
    if count == 1:
        return True
    else:
        return False

print(some(int(input("Enter a number : "))))
