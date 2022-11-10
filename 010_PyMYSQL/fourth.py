import pymysql
try:
    connection = pymysql.connect(
        host="localhost",
        port=3306,
        user="root",
        password="2255",
        database="Social_network",
        cursorclass=pymysql.cursors.DictCursor)
    print("Okay!")
    with connection.cursor() as cursor:
        while True:
            try:
                username = input("Enter a username : ")
                password = input("Enter a password : ")
            except Exception as error:
                print(error)
            cursor.execute(f"select login from Logins where username = '{username}'")
            password_check = cursor.fetchall()
            try:
                if password_check[0].get('login') == password:
                    print("Okay!"); break
                else:
                    print("Bad password!")
            except:
                print("Incorrect user")
        while True:
            enter = int(input("1 - list, 2 - add, 3 - del, 4 - all del, 5 - replace : "))
            if enter == 1:
                cursor.execute("select * from koshikDB.koshik")
                result = cursor.fetchall()
                for i in result:
                    print(i.get('id'), ":", i.get('product'))             
            elif enter == 2:
                name = input("Name : ")
                surname = input("Surname : ")
                info = input("Info : ")
                friends = input("Friends : ")
                publications = input("Publications : ")
                cursor.execute(f'''insert users (name, surname, info, friends, publications)
                values ('{name}', '{surname}', '{info}', '{friends}', '{publications}')''')
                connection.commit()
            elif enter == 3:
                cursor.execute("select * from koshikDB.koshik")
                result = cursor.fetchall()
                for i in result:
                    print(i.get('id'), ":", i.get('product'))
                uenter = int(input("Enter a product id : "))
                cursor.execute(f"delete from koshikDB.koshik where id = {uenter}")
                connection.commit()
            elif enter == 4:
                cursor.execute(f"delete from koshikDB.koshik")
                connection.commit()
            elif enter == 5:
                cursor.execute("select * from koshikDB.koshik")
                result = cursor.fetchall()
                for i in result:
                    print(i.get('id'), ":", i.get('product'))
                replace_id = input("Enter id of product : ")
                replace = input("Enter for replace : ")
                cursor.execute(f"update koshik set product = '{replace}' where id = '{replace_id}'")
                connection.commit()
            elif enter == 6:
                select = int(input("1, 2, 3 : ")) # Select action from another two tasks  
                if select == 1:
                    find_product = input("Enter a product name : ")
                    cursor.execute(f"select * from koshik where product = '{find_product}'")
                elif select == 2:
                    cursor.execute(f"select * from koshik where id = (select max(id) from koshik)")
                result = cursor.fetchall()
                for i in result:
                  print(i.get('id'), ":", i.get('product'))
except Exception as error:
    print(error)