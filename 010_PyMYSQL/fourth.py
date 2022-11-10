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
            cursor.execute(f"select password from Logins where username = '{username}'")
            password_check = cursor.fetchall()
            try:
                if password_check[0]['password'] == password:
                    print("Okay!"); break
                else:
                    print("Bad password!")
            except:
                print("Incorrect user")
        while True:
            enter = int(input("1 - list, 2 - add, 3 - del, 4 - all del, 5 - replace, 6 - show : "))
            if enter == 1:
                cursor.execute("select * from users")
                result = cursor.fetchall()
                for i in result:
                    for j in i:
                        print(j, ":", i[j])
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
                cursor.execute("select * from users")
                result = cursor.fetchall()
                for i in result:
                    print(i['id'], "-", i['name'], i['surname'])
                uenter = int(input("Enter a user id : "))
                cursor.execute(f"delete from users where id = {uenter}")
                connection.commit()
            elif enter == 4:
                cursor.execute(f"delete from users")
                connection.commit()
                print("Okay!")
            elif enter == 5:
                id = input("Enter a user id : ")
                cursor.execute(f"select * from users where id = '{id}'")
                result = cursor.fetchall()
                for i in result:
                     print(i['id'], "-", i['name'], i['surname'])
                uenter = int(input("1 - name, 2 - surname, 3 - info : "))
                if uenter == 1:
                    name = input("Name : ")
                    cursor.execute(f"update users set name = '{name}' where id = '{id}'")
                elif uenter == 2:
                    surname = input("Surname : ")
                    cursor.execute(f"update users set surname = '{surname}' where id = '{id}'")
                elif uenter == 3:
                    info = input("Info : ")
                    cursor.execute(f"update users set info = '{info}' where id = '{id}'")                   
                connection.commit()
            elif enter == 6:
                id = input("Enter a user id : ")
                cursor.execute(f"select * from users where id = '{id}'")
                result = cursor.fetchall()
                uenter = int(input("1 - info, 2 - friends, 3 - publications, 4 - all : "))
                if uenter == 1:
                    print("Info : ", result[0]['info'])
                elif uenter == 2:
                    print("Friends : ", result[0]['friends'])
                elif uenter == 3:
                    print("Publications : ", result[0]['publications'])
                elif uenter == 4:
                    for i in result[0]:
                        print(i, ":", result[0][i])
except Exception as error:
    print(error)