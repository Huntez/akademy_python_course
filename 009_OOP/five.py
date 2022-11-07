# class Triangle_checker():
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c

#     def is_trinagle(self):
#         if self.a.strip("-").isdigit() == False or self.b.strip("-").isdigit() \
#         == False or self.c.strip("-").isdigit() == False:
#             return "Only digits!"
#         else:
#             self.a = int(self.a)
#             self.b = int(self.b)
#             self.c = int(self.c)
#         if self.a <= 0 or self.b <= 0 or self.c <= 0:
#             return "Numbers equal or lower than zero!"
#         if self.a + self.b > self.c and self.a + self.c > self.b \
#         and self.b + self.c > self.a:
#             return "We can build this!"
#         else:
#             return "Oh shit, we cant build!"\

# nikolay = Triangle_checker(a = input("a : "), b = input("b : "), 
# c = input("c : "))
# print(nikolay.is_trinagle())

class Figure():
    def __init__(self, a, b):
        self.a = a
        self.b = b

class Rect(Figure):
    def __str__(self):
        return f"Rectangle S = {self.a * self.b}"
class Triangle(Figure):
    def __str__(self):
        return f"Right triangle S = {(self.a * self.b) / 2}"
class Circle(Figure):
    def __init__(self, a):
        self.a = a
    def __str__(self):
        return f"Circle S = {3.14 * pow(self.a,2)}"
class Trapec(Figure):
    def __init__(self, a, b, h):
        self.h = h
        super().__init__(a, b)
    def __str__(self):
        return f"Trapecia S = {((self.a + self.b) / 2) * self.h}"

rect = Rect(a=1, b=2); print(rect)
trian = Triangle(a=1, b=2); print(trian)
circle = Circle(a = 10); print(circle)
trapec = Trapec(a=2, b=3, h=5); print(trapec)


