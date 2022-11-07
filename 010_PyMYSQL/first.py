import pymysql
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
            enter = int(input("1-2, 3, 4, 5 : "))
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
except Exception as error:
    print(error)