# class Auto:
#     def __init__(self, name, date, volume, color, price):
#         self.name = name
#         self.date = date
#         self.volume = volume
#         self.color = color
#         self.price = price

#     def change_name(self):
#         self.name = input("Enter a name : ")
#         return "Okay!"

#     def __str__(self):
#         return f"{self.name, self.date, self.volume, self.color, self.price}"

# some = Auto(name=input("Name : "),date=input("Date : "),volume=input("Volume : "),
# color=input("Color : "),price=input("Price : "))
# print(some); print(some.change_name()); print(some)

#Second

class Books:
    def __init__(self, name, date, publisher, genre, author, price):
        self.name = name
        self.date = date
        self.publisher = publisher
        self.genre = genre
        self.author = author
        self.price = price

    def change_name(self):
        self.name = input("Enter a name : ")
        return "Okay!"

    def __str__(self):
        return f"{self.name, self.date, self.publisher, self.genre, self.author, self.price}"

some = Books(name=input("Name : "),date=input("Date : "),publisher=input("Publisher : "),
genre=input("Genre : "),author=input("Author : "), price=input("Price : "))
print(some); print(some.change_name()); print(some)

#Third

class Stadium:
    def __init__(self, name, date, country, city, accuracy):
        self.name = name
        self.date = date
        self.country = country
        self.city = city
        self.accuracy = accuracy

    def change_name(self):
        self.ph = input("Enter a name : ")
        return "Okay!"

    def __str__(self):
        return f"{self.name, self.date, self.country, self.city, self.accuracy}"

some = Stadium(name=input("Name : "),date=input("Date : "),country=input("Country : "),
city=input("City : "),accuracy=input("Accuracy : "))
print(some); print(some.change_name()); print(some)
