import connections
import pymysql

def connect_to_db(db_name):
    connection = pymysql.connect(
        host=connections.host,
        port=connections.port,
        user=connections.user,
        password=connections.password,
        database=db_name,
        cursorclass=pymysql.cursors.DictCursor)
    return connection