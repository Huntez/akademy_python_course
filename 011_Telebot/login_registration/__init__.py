import connections
import pymysql
from mysql_connect import connect_to_db

class authorization:
    def __init__(self, user, password, db_name):
        self.user = user
        self.password = password
        self.connection = connect_to_db(db_name)

    def login_to_db(self):
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(f'''select password from logins 
                where user = "{self.user}"''')
                if cursor.fetchall()[0]['password'] == self.password:
                    return True
                else:
                    return False
        except Exception as error:
            print(error)
        finally:
            self.connection.close()
        
    def registration_to_db(self):
        try:
            with self.connection.cursor() as cursor:
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
            self.connection.commit()
            self.connection.close()

class check_authorization:
    def __init__(self, message_chat_id, db_name):
        self.message_chat_id = message_chat_id
        self.connection = connect_to_db(db_name)
        
    def check_message_chat_id_in_bd(self):
        try:
            with self.connection.cursor() as cursor:
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
            with self.connection.cursor() as cursor:
                cursor.execute(f'''insert message_chat_id (id, autorization_check)
                values ({self.message_chat_id}, false)''')
                return True
        except Exception as error:
            print(error)
        finally:
            self.connection.commit()

    def authorization_update(self, state):
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(f'''update message_chat_id set autorization_check = {state}
                where id = "{self.message_chat_id}"''')
                return True
        except Exception as error:
            print(error)
        finally:
            self.connection.commit()
            self.connection.close()
    
    def authorization_check(self):
        try:
            with self.connection.cursor() as cursor:
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
            self.connection.commit()
            self.connection.close()
    
    