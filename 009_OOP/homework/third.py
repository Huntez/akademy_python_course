import os.path

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
    def __init__(self, fname):
        self.fname = fname + ".txt"
        self.path = os.path.join("lesson16", self.fname)

    def add_auto(self, sstring):
        file = open(self.path, "a")
        file.write(str(sstring) + "\n"); file.close()
        return f"Adding auto!"

    def buy_auto(self, name):
        file = open(self.path, "r")
        alist = [i for i in file if not name in i]; file.close()
        file = open(self.path, "w")
        for i in alist:
            file.write(i)
        file.close()
        return "Okay!"
    
    def __str__(self):
        file = open(self.path, "r")
        alist = [i for i in file]; file.close()
        return "".join(alist)

some = Autosaloon(fname="new")
print(some.add_auto(cars))
print(some.add_auto(scars)); print(some)
print(some.buy_auto(input("Enter auto name : "))); print(some)