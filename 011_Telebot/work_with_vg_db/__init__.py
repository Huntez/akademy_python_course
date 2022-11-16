import pymysql
from mysql_connect import connect_to_db

class work_with_vegetables_db:
    def __init__(self, db_name):
        self.connection = connect_to_db(db_name)
    
    def select_without_filters(self):
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(f'''select * from vegetables''')
                return '\n'.join([f'''id : {i['id']}, name : {i['name']}, cost : {i['cost']}'''
                for i in cursor.fetchall()])
        except Exception as error:
            print(error)

    def select_with_filter(self, filter):
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(f'''select {filter} from vegetables''')
                return '\n'.join([f'''{filter} : {i[f'{filter}']}'''
                for i in cursor.fetchall()])
        except Exception as error:
            print(error)

    def add_to_db(self, name, cost):
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(f'''select count(*) from vegetables
                where name = "{name}"''')
                if cursor.fetchall()[0]['count(*)'] == 0:
                    cursor.execute(f'''insert vegetables(name, cost)
                    values ('{name}','{cost}')''')
                    self.connection.commit()
                    return True
                else:
                    return False
        except Exception as error:
            print(error)

    def del_from_db(self, id):
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(f'''delete from vegetables where
                id = {id}''')
                self.connection.commit()
        except Exception as error:
            print(error)
        