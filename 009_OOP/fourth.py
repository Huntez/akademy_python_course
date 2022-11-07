import os.path
import json

class Car:
    def __init__(self, color, name, year, code):
        self.color = color
        self.name = name
        self.year = year
        self.code = code

    def __str__(self):
        return f"{self.name}, {self.color}, {self.year}"

cars = Car(code="251893", color="gray", name="ae86", year="1983")
scars = Car(code="251293", color="gray", name="ae85", year="1981")

class Autosaloon:
    def __init__(self, fname):
        self.fname = fname + ".json"
        self.path = os.path.join("lesson16", self.fname)

    def add_auto(self, car):
        file = open(self.path, "r")
        sdict = json.load(file)
        sdict[car.code] = {"name":car.name, "color":car.color, "year":car.year}
        file.close()
        file = open(self.path, "w")
        json.dump(sdict, file); file.close()
        return f"Adding auto!"

    def update_auto(self, car):
        file = open(self.path, "r")
        sdict = json.load(file)
        sdict[car.code] = {"name":car.name, "color":car.color, "year":car.year}
        file.close()
        file = open(self.path, "w")
        json.dump(sdict, file); file.close()
        return f"Upadte auto!"

    def buy_auto(self, code):
        file = open(self.path, "r")
        alist = json.load(file); file.close()
        alist.pop(code)
        file = open(self.path, "w")
        json.dump(alist, file); file.close()
        return "Okay!"
        
    def comprasion(self, car, scar):
        fcar = str(car).split(","); scar = str(scar).split(",")
        # for a,b in zip(fcar, scar):
        #     if a == b:
        #         print(a.replace(" ", ""))
        #     else:
        #         print(a.replace(" ", ""), b.replace(" ", ""))
        for i in range(len(fcar)):
            if fcar[i] == scar[i]:
                print(fcar[i].replace(" ", ""))
            else:
                print(fcar[i].replace(" ", ""), scar[i].replace(" ", ""))
        return "Complete!"
    
    def __str__(self):
        file = open(self.path, "r")
        alist = json.load(file); file.close()
        return "\n".join([f"{item}, {alist.get(item).get('name')},\
 {alist.get(item).get('color')}, {alist.get(item).get('year')}" for item in alist])

some = Autosaloon(fname="new")
print(some.add_auto(cars))
print(some.add_auto(scars)); print(some)
print(some.comprasion(cars, scars))
print(some.buy_auto(input("Enter code : "))); print(some)