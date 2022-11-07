# class Calc:
#     def __init__(self, a, b):
#         try:
#             self.a = int(a)
#             self.b = int(b)
#         except(ValueError):
#             print("Non int value!")
    
#     def divide(self):
#         try:
#             return f"Result : {self.a / self.b}"
#         except(ZeroDivisionError):
#             return "Cant divide by zero!"
#     def multiply(self):
#         return f"Result : {self.a * self.b}"
#     def adding(self):
#         return f"Result : {self.a + self.b}"
#     def minusing(self):
#         return f"Result : {self.a - self.b}"

# # while True:
# #     try:
# #         calc = Calc(a=int(input("a : ")), b=int(input("b : ")))
# #     except(ValueError):
# #         print("Non int value!")
# #     else:
# #         break

# calc = Calc(a=input("a : "), b=input("b : "))
# print(calc.divide())

# class Phone():
#     def __init__(self, phone):
#         if not phone.startswith("+380") or len(phone) != 13\
#         or not phone.strip("+").isdigit():
#             raise Exception("kva")
#         else:
#             self.phone = phone
#     def __str__(self):
#         return self.phone

# ph = Phone(phone="+380673660833"); print(ph)

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

# class CheckTime:
#     def __init__(self, slist):
#         self.list = slist

    


