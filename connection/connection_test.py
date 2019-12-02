from mysql.connector import MySQLConnection, Error

# ctrl + alt + o : 안쓰는 import 정리
def connect():
    try:
        conn = MySQLConnection(host='localhost',
                                       database='mysql',
                                       user='root',
                                       password='rootroot')
        print(conn)
    except Error as e:
        print(e)