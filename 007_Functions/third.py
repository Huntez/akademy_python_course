
# def ppow(a, b):
#     if b == 0:
#         return 1
#     else:
#         return a * ppow(a, b - 1)
    
# print(ppow(int(input("N : ")),int(input("P : "))))

# Second

def ppow(a, b):
    if a == b:
        return a
    else:
        return b + ppow(a, b-1)
    
print(ppow(int(input("F : ")),int(input("S : "))))


# def symb(a,b):
#     if b == 1:
#         return "*" 
#     else:
#         return a + symb(a, b - 1)
    
# print(symb("*", int(input("Size : "))))