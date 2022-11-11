import pymysql
try:
    connection = pymysql.connect(
        host="localhost",
        port=3306,
        user="root",
        password="2255",
        database="Social_Network_Rework",
        cursorclass=pymysql.cursors.DictCursor)
    print("Okay!")
    with connection.cursor() as cursor:
        while True:
            try:
                username = input("Enter a username : ")
                password = input("Enter a password : ")
            except Exception as error:
                print(error)
            cursor.execute(f"select password from logins where username = '{username}'")
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
            if enter == 1: # print all users in DB
                cursor.execute("select * from users")
                for i in cursor.fetchall():
                    for j in i:
                        print(j, ":", i[j])
            elif enter == 2: # adding user to DB
                uenter = int(input("1 - add user, 2 - publications or friends : "))
                if uenter == 1:
                    name = input("Name : ")
                    surname = input("Surname : ")
                    info = input("Info : ")
                    cursor.execute(f'''insert users (name, surname, info)
                    values ('{name}', '{surname}', '{info}')''')
                    cursor.execute("select max(id) from users")
                    print("User id -", cursor.fetchall()[0]['max(id)'])
                elif uenter == 2:
                    id = int(input("Enter a user id : "))
                    cursor.execute(f"select count(id) from users where id = '{id}'")
                    if cursor.fetchall()[0]['count(id)'] == 1:                
                        uenter = int(input("1 - publications, 2 - friends : "))
                        if uenter == 1:
                            publication = input("Enter a publication : ")
                            cursor.execute(f'''insert publications (id, publication)
                            values('{id}', '{publication}')''')
                        elif uenter == 2:
                            friend = input("Enter a friend : ")
                            cursor.execute(f'''insert friends (id, friend)
                            values('{id}', '{friend}')''')                            
                    else:
                        print("User dont exist!")   
                connection.commit()
            elif enter == 3:
                cursor.execute("select * from users")
                for i in cursor.fetchall():
                    print(i['id'], "-", i['name'], i['surname'])
                uenter = int(input("Enter a user id : "))
                cursor.execute(f"delete from users where id = {uenter}")
                cursor.execute(f"delete from publications where id = '{uenter}'")
                cursor.execute(f"delete from friends where id = '{uenter}'")
                connection.commit()
            elif enter == 4:
                cursor.execute(f"delete from users")
                cursor.execute(f"delete from publications")
                cursor.execute(f"delete from friends")
                connection.commit()
                print("Okay!")
            elif enter == 5:
                id = input("Enter a user id : ")
                cursor.execute(f"select * from users where id = '{id}'")
                for i in cursor.fetchall():
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
                id = int(input("Enter a user id : "))
                cursor.execute(f"select count(id) from users where id = '{id}'")
                if cursor.fetchall()[0]['count(id)'] == 1:                
                    uenter = int(input("1 - all user info, 2 - friends, 3 - publications : "))
                    if uenter == 1:
                        cursor.execute(f"select * from users where id = '{id}'")
                    elif uenter == 2:
                        cursor.execute(f"select friend from friends where id = '{id}'")
                    elif uenter == 3:
                        cursor.execute(f"select publication from publications where id = '{id}'")
                    result = cursor.fetchall()
                    for i in result:
                         for j in i:
                             print(j, ":", i[j])
                else:
                    print("User dont exist!")   
except Exception as error:
    print(error)