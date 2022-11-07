class People:
    def __init__(self, name, age, ph, ct, co, ha, gmail):
        self.name = name
        self.age = age
        self.ph = ph
        self.ct = ct
        self.co = co
        self.ha = ha
        self.gmail = gmail

    def change_phone(self):
        self.ph = input("Enter a phone : ")
        return "Congrutulations!"

    def change_gmail(self):
        self.gmail = input("Enter a gmail : ")
        return "Congrutulations!"
    
    def test_number(self):
        if self.ph.startswith("+380") == True and len(self.ph) == 13:
            return "Okay"
        else:
            return self.change_phone()
    
    def test_gmail(self):
        if self.gmail.startswith("@") == False and self.gmail.endswith("@gmail.com") == True:
            return "OkaY!"
        else:
            return self.change_gmail()

    def __str__(self):
        return f"{self.name, self.age, self.ph, self.ct, self.co, self.ha, self.gmail}"

some = People(name="Some",age="23",ph="+38067255083",ct="city",co="Ukraine",ha="street", gmail="admin@gmail.com")
print(some); print(some.test_number()); print(some.test_gmail()); print(some)
