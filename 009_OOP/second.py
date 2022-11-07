class Car:
    def __init__(self, color, ctype, year):
        self.color = color
        self.ctype = ctype
        self.year = year

    def turn_car(self):
        return "Car is on!"

    def turn_off_car(self):
        return "Car is off!"

    def set_color(self):
        self.color = input("Color : ")
        return "Color is set!"

    def set_year(self):
        self.year = input("Year : ")
        return "Year is set!"

    def set_ctype(self):
        self.ctype = input("Type : ")
        return "Type is set!"

    def __str__(self):
        return f"{self.color, self.ctype, self.year}"

some = Car("", "", "")
print(some.set_color()); print(some.set_year()); print(some.set_ctype()); print(some)
print(some.turn_car()); print(some.turn_off_car())

# Second

# class Soda:
#     def __init__(self, stype):
#         self.stype = stype

#     def show_my_drink(self):
#         slist = ["purple", "orange", "green"]
#         if self.stype in slist:
#             return f"Soda + {self.stype}"
#         else:
#             return "Just soda!"

# soda = Soda(stype=input("Addition : ")); print(soda.show_my_drink())

# Third

# class People:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def nikolay_check(self):
#         if self.name == "Nikolay":
#             return f"Nikolay : {self.age}"
#         else:
#             return f"Im not {self.name}, i am Nikolay!"

# some = People(name=input("Name : "), age=input("Age : "))
# print(some.nikolay_check())

# Fourth

class Car:
    def __init__(self, color, name, year):
        self.color = color
        self.name = name
        self.year = year

    def __str__(self):
        return f"{self.name}, {self.color}, {self.year}"

cars = Car(color="gray", name="ae86", year="1983")
scars = Car(color="gray", name="ae85", year="1981")

class Autosaloon:
    def __init__(self):
        self.adict = {}

    def add_auto(self, sstring):
        alist = str(sstring).split(",")
        self.adict[alist[0]] = {"Color": alist[1], "Year": alist[2]}
        return f"Adding auto {alist[0]}!"

    def buy_auto(self, name):
        if name in self.adict:
            self.adict.pop(name)
            return f"You buy {name}!"
        else:
            return f"{name} not in car list!"

    def __str__(self):
            return f"{str(self.adict)[1:-1]}"

some = Autosaloon()
print(some.add_auto(cars))
print(some.add_auto(scars)); print(some)
print(some.buy_auto(input("Enter auto name : "))); print(some)