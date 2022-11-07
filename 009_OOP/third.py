# class Calc:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b

#     def adding(self):
#         return f"Result : {self.a + self.b}"

#     def minusing(self):
#         return f"Result : {self.a - self.b}"

#     def dividing(self):
#         return f"Result : {self.a / self.b}"
    
#     def multiply(self):
#         return f"Result : {self.a * self.b}"
    
#     def replace(self, a, b):
#         self.a = a
#         self.b = b
#         return "Okay!"
    
# some = Calc(a=int(input("F : ")), b=int(input("S : ")))
# print(some.adding()); print(some.minusing())
# print(some.dividing()); print(some.multiply())
# print(some.replace(int(input("F : ")), int(input("S : "))))
# print(some.adding()); print(some.minusing())
# print(some.dividing()); print(some.multiply())

# class Books():
#     def __init__(self, name, date, author, genre):
#         self.name = name
#         self.date = date
#         self.author = author
#         self.genre = genre
#         self.review = {}

#     def add_review(self, text):
#         self.review = {self.name: str(text)}

#     def __str__(self):
#         return f"{str(self.review)[1:-1]}, Date : {self.date},\
# Author : {self.author}, Genre : {self.genre}"

# some = Books(name="1984", date="1984", author="George", genre="Kva")

# class Review():
#     def __init__(self, text):
#         self.text = text

#     def __str__(self):
#         return self.text

# ssome = Review(text="Some text bla bla bla!")
# some.add_review(ssome); print(some)
# some = Books(name="1985", date="1985", author="George", genre="Kva")
# ssome = Review(text="Some text bla bla bla!")
# some.add_review(ssome); print(some)

# class Human():
#     def __init__(self, name):
#         self.name = name

# class Builder(Human):
#     def __str__(self):
#         return f"Im a builder {self.name}"

# class Sailor(Human):
#     def __str__(self):
#         return f"Im a sailor {self.name}"

# class Pilot(Human):
#     def __str__(self):
#         return f"Im a pilot {self.name}"

# builder = Builder(name="Bob"); print(builder)
# sailor = Sailor(name="Bob2"); print(sailor)
# pilot = Pilot(name="Bob3"); print(pilot)

class Animals():
    def __init__(self, name):
        self.name = name

class Tiger(Animals):
    def __str__(self):
        return f"Buzz - {self.name}"

class Crocodile(Animals):
    def __str__(self):
        return f"Meow - {self.name}"

class Kangaroo(Animals):
    def __str__(self):
        return f"Gruuu - {self.name}"

builder = Tiger(name="Tiger"); print(builder)
sailor = Crocodile(name="Crocodile"); print(sailor)
pilot = Kangaroo(name="Kangaroo"); print(pilot)

# class Passport():
#     def __init__(self, name, age, id, country):
#         self.name = name
#         self.id = id
#         self.age = age
#         self.country = country

# class ForeignPassport(Passport):
#     def __init__(self, name, age, id, country, visa, number):
#         super().__init__(name, age, id, country)
#         self.visa = visa
#         self.number = number

#     def __str__(self):
#         return f"Name : {self.name}, Age : {self.age}, Id : {self.id} \
# Country : {self.country}, Visa : {self.visa}, Number : {self.number}"

# some = ForeignPassport("Bob", "58", "58bob123", "Bobauntry", "B0B5801", "+8800")
# print(some)