# class Device:
#     def __init__(self, name, year):
#         self.name = name
#         self.year = year

# class CoffeMachine(Device):
#     def __str__(self):
#         return f"Coffe machine : {self.name}, Year : {self.year}"
        
# class MeatGrinder(Device):
#     def __str__(self):
#         return f"Meat grinder : {self.name}, Year : {self.year}"

# coffe = CoffeMachine(name="Cofinius", year="1993")
# meat = MeatGrinder(name="Mitius", year="1993")
# print(coffe); print(meat)

# Second

# class Ship:
#     def __init__(self, name, year):
#         self.name = name
#         self.year = year

# class Destroyer(Ship):
#     def __str__(self):
#         return f"Destroyer : {self.name}, Year : {self.year}"
        
# class Cruiser(Ship):
#     def __str__(self):
#         return f"Cruiser : {self.name}, Year : {self.year}"

# destro = Destroyer(name="Sdistro", year="1993")
# cruis = Cruiser(name="Scruis", year="1995")
# print(destro); print(cruis)

# Third

class Money:
    def __init__(self, money, cents, mtype):
        self.money = money
        self.cents = cents
        self.mtype = mtype

    def setmoney(self, money):
        self.money = money
        return "Money is set!"

    def setcents(self, cents):
        self.cents = cents
        return "Cents is set!"
    
    def convertmoney(self, mtype):
        if mtype == "USD" and self.mtype == "UA":
            self.money = int(self.money / 37.16)
            self.cents= int(self.cents / 37.16)
        elif mtype == "USD" and self.mtype == "EU":
             self.money = int(self.money * 1.03)
             self.cents= int(self.cents * 1.03)
        elif mtype == "UA" and self.mtype == "USD":
             self.money = int(self.money * 37.16)
             self.cents= int(self.cents * 37.16)
        elif mtype == "UA" and self.mtype == "EU":
             self.money = int(self.money * 36.16)
             self.cents= int(self.cents * 36.16)
        return "Okay!"

    def __str__(self):
        return f"Money {self.money}, Cents : {self.cents}"

class Product(Money):
    def lowmoney(self, summ):
        self.money -= summ
        return "Okay!"

    def lowcents(self, summ):
        self.cents -= summ
        return "Okay!"

mon = Money(money=132, cents=23, mtype="UA"); print(mon)
print(mon.convertmoney("USD")); print(mon)
# print(mon.setmoney(int(input("Enter money : "))))
# print(mon.setcents(int(input("Enter cents : ")))); print(mon)

# prod = Product(money=132, cents=23); print(prod)
# print(prod.lowmoney(int(input("Enter summ : "))))
# print(prod.lowcents(int(input("Enter summ: ")))); print(mon)