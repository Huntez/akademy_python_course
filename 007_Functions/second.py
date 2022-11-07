
# def goodluck(a):
#     fsum, ssum = [int(i) for i in a[:3]], [int(i) for i in a[3:]]
#     if sum(fsum) == sum(ssum):
#         return True
#     else:
#         return False

# print("Goodluck result : ", goodluck(input("Enter number : ")))

# first

from random import randint

# def ssum(a):
#     print(a); return sum(a)

# print("Sum :", ssum([randint(1, 10) for i in range(10)]))

# # Second

# def mmax(a):
#     print(a); return max(a)

# print("Max :", mmax([randint(1, 10) for i in range(10)]))

# # Third

# def ccount(a):
#     print(a)
#     print("Even :", len([i for i in a if i % 2 == 0]))
#     print("Odd :", len([i for i in a if i % 2 != 0]))
#     print("Pos :", len([i for i in a if i > 0]))
#     print("Neg :", len([i for i in a if i < 0]))

# ccount([randint(-10,10) for i in range(10)])

# Fourth

def rever(a):
    print(a)
    return a[::-1]

print("Reverse :", rever([randint(1, 10) for i in range(10)]))

# Five

def sfind(a,b):
    if b in a:
        return True
    else:
        return False

slist = [randint(1, 20) for i in range(10)]; print(slist)
print("Number : ", sfind(slist, int(input("Enter to find : "))))

# Six

def fact(a):
    slist = []
    for i in a:
        facto = 1
        for j in range(1, i+1):
            facto *= j
        slist.append(facto)
    return slist

slist = [1,2,3,4,5,6]; print(slist)
print("Fact list : ", fact(slist))
