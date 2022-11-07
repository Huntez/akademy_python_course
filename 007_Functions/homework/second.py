from random import randint

def dobut(a):
    dobut = 1
    for i in a:
        dobut *= i
    return dobut

flist = [randint(1, 10) for i in range(5)]; print(flist)
print("Dobut res : ", dobut(flist))

mmin(a):
    pr

# Second

def mmin(a):
    return min(a)

flist = [randint(1, 10) for i in range(5)]; print(flist)
print("Min res : ", mmin(flist))

# Third

def some(a):
    scount = 0
    for i in a:
        count = 0
        for j in range(1, i):
            if i % j == 0 and j != i:
                count += 1
        if count == 1:
            scount += 1
    return scount

flist = [randint(1, 10) for i in range(5)]; print(flist)
print("Simple numbers count :", some(flist))

# Fourth

def sdel(a, b):
    lists, count = list(a), 0
    for i in a:
        if i == b:
            lists.remove(b)
            count += 1
    print(lists)
    return count

flist = [randint(1, 10) for i in range(5)]; print(flist)
print("Del count :", sdel(flist, int(input("Enter a number : "))))

# Five

def merger(a,b):
    return a+b

flist = [randint(1, 10) for i in range(5)]
slist = [randint(1, 10) for i in range(5)]
print(flist, slist)
print("Merge result :", merger(flist, slist))

# Six

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
