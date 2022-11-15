import connections
import pymysql

try:
    connection = pymysql.connect(
        host=connections.host,
        port=connections.port,
        user=connections.user,
        password=connections.password,
        database="Telebot",
        cursorclass=pymysql.cursors.DictCursor)
except Exception as error:
    print(error)

class authorization:
    def __init__(self, user, password):
        self.user = user
        self.password = password

    def login_to_db(self):
        try:
            with connection.cursor() as cursor:
                cursor.execute(f'''select password from logins 
                where user = "{self.user}"''')
                if cursor.fetchall()[0]['password'] == self.password:
                    return True
                else:
                    return False
        except Exception as error:
            print(error)
        finally:
            pass
        
    def registration_to_db(self):
        try:
            with connection.cursor() as cursor:
                cursor.execute(f'''select count(*) from logins
                where user = "{self.user}"''')
                if cursor.fetchall()[0]['count(*)'] == 0:
                    cursor.execute(f'''insert logins (user, password)
                    values ("{self.user}", "{self.password}")''')
                    return True
                else:
                    return False
        except Exception as error:
            print(error)
        finally:
            connection.commit()

class check_authorization:
    def __init__(self, message_chat_id):
        self.message_chat_id = message_chat_id
        
    def check_message_chat_id_in_bd(self):
        try:
            with connection.cursor() as cursor:
                cursor.execute(f'''select count(*) from message_chat_id where
                id = "{self.message_chat_id}"''')
                if cursor.fetchall()[0]['count(*)'] == 1:
                    return True
        except Exception as error:
            print("Error")
        finally:
            pass

    def add_message_chat_id_to_db(self):
        try:
            with connection.cursor() as cursor:
                cursor.execute(f'''insert message_chat_id (id, autorization_check)
                values ({self.message_chat_id}, false)''')
                return True
        except Exception as error:
            print(error)
        finally:
            connection.commit()

    def authorization_update(self):
        try:
            with connection.cursor() as cursor:
                cursor.execute(f'''update message_chat_id set autorization_check = true
                where id = "{self.message_chat_id}"''')
                return True
        except Exception as error:
            print(error)
        finally:
            connection.commit()
    
    def authorization_check(self):
        try:
            with connection.cursor() as cursor:
                if self.check_message_chat_id_in_bd():
                    cursor.execute(f'''select autorization_check from 
                    message_chat_id where id = "{self.message_chat_id}"''')
                    if cursor.fetchall()[0]['autorization_check'] == 1:
                        return True
                    else:
                        return False
                else:
                    self.add_message_chat_id_to_db()
                    self.authorization_check()
        except Exception as error:
            print(error)
        finally:
            connection.commit()
    
    