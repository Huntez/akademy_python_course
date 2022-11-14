import connections
import pymysql

connection = pymysql.connect(
    host=connections.host,
    port=connections.port,
    user=connections.user,
    password=connections.password,
    database="Telebot",
    cursorclass=pymysql.cursors.DictCursor)

class authorization:
    def __init__(self, user, password):
        self.user = user
        self.password = password

    def login_to_db(self):
        with connection.cursor() as cursor:
            cursor.execute(f'''select password from logins 
            where user = "{self.user}"''')
            if cursor.fetchall()[0]['password'] == self.password:
                return True
            else:
                return False
        
    def registration_to_db(self):
        with connection.cursor() as cursor:
            cursor.execute(f'''select count(*) from logins
            where user = "{self.user}"''')
            if cursor.fetchall()[0]['count(*)'] == 0:
                cursor.execute(f'''insert logins (user, password)
                values ("{self.user}", "{self.password}")''')
                connection.commit()
                return True
            else:
                return False
        