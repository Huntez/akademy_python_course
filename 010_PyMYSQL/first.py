import pymysql
import json
import os.path
try:
    connection = pymysql.connect(
        host="localhost",
        port=3306,
        user="root",
        password="2255",
        database="People",
        cursorclass=pymysql.cursors.DictCursor)
    print("Okay!")
    with connection.cursor() as cursor:
        while True:
            enter = int(input("1-2, 3, 4, 5, 6 : "))
            if enter == 1:
                action = input("Enter : ")
                if "people" not in action:
                    raise Exception("Incorrect table name!")
                if "select" in action:
                    cursor.execute(action)
                    for i in cursor.fetchall():
                        print(i)
                else:
                    raise Exception("Only SELECT query!")
                if "update" in action or "delete" in action and\
                    "where" not in action:
                    raise Exception("Cant delete all rows!")
                else:
                    cursor.execute(action); connection.commit()
                    print("Okay!")
            elif enter == 3:
                uenter = int(input("1 - all, 2 - diap, 3 - by city : "))
                if uenter == 1:
                    cursor.execute("select * from people")
                elif uenter == 2:
                    fdiap = input("First diap : ")
                    sdiap = input("Second diap : ")
                    cursor.execute(f"select * from people between {fdiap} and {sdiap}")
                elif uenter == 3:
                    city = input("Enter city : ")
                    cursor.execute(f"select * from people where city = {city}")
                elif uenter == 4:
                    country = input("Enter country : ")
                    cursor.execute(f"select * from people where country = {country}")
                for i in cursor.fetchall():
                    print(i)
            elif enter == 4:
                  city = input("Enter city : ")
                  country = input("Enter country : ")
                  cursor.execute(f"select * from people where city = {city} and country = {country}")
                  for i in cursor.fetchall():
                    print(i)
            elif enter == 5:
                uenter = int(input("1 - ins, 2 - del : "))
                if uenter == 1:
                    city = input("Enter city : ")
                    country = input("Enter country : ")
                    name = input("Enter name : ")
                    surname = input("Enter surname : ")
                    birthday = input("Enter birthday : ")
                    cursor.execute(f'''insert people (name, surname, city, country, birthday)
values({name}, {surname}, {city}, {country}, {birthday})''')
                elif uenter == 2:
                    country = input("Country for delete : ")
                    cursor.execute("delete from people where country = {country}")
                connection.commit()
            elif enter == 6:
                cursor.execute("select * from people")
                file = open(os.path.join("010_PyMYSQL", "first.json"), "w")
                json.dump(cursor.fetchall(), file)
except Exception as error:
    print(error)