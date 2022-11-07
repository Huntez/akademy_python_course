
def tprint(a):
    return a

print(tprint('''Dont compare yourself with anyone in this world...
  if you do so, you are insulting yourself.\n\t\t\t\t\tBill Gates'''))


# Second

def some(a,b):
    for i in range(a+1,b):
        if i % 2 == 0:
            print(i)

some(int(input("Enter first : ")), int(input("Enter second : ")))


# Third

def cube(a,b,c):
    print(c)
    if c == True:
        for i in range(a):
            print((b + "  ") * a)
    else:
        print((b + " ")*a)
        for i in range(a-2):
            d = a - 2
            print(b + d * "  " + " " + b)
        print((b + " ")*a)

cube(int(input("S : ")), input("Sym : "), int(input("0 or 1 : ")))

# Fourth

def fmin(a,b,c,d,e):
    return min(a,b,c,d,e)

print("Min res : ",fmin(1,25,-1,18,11))

# Five

def dobut(a,b):
    summ = 1
    if a > b:
        for i in range(b,a+1):
            summ *= i
    else:
        for i in range(a,b+1):
            summ *= i
    return summ

print("Dobutor res : ", dobut(int(input("F : ")), int(input("S : "))))

# Six

def ncount(a):
    return len(a)

print("Len : ", ncount(input("Enter number : ")))

# Seven

def polin(a):
    a = a.replace(" ", "");
    if a.lower() == a.lower()[::-1]:
        return True
    else:
        return False

print("Polindrom resulut : ", polin(input("Enter word or string : ")))
