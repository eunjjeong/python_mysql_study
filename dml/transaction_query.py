from mysql.connector import Error
from dml.connection_pool import ConnectionPool


def transaction_fail1():
    try:
        print('Connecting to MySQL database...')
        conn = ConnectionPool.get_instance().get_connection()
        print(type(conn))
        conn.autocommit = False
        cursor = conn.cursor()
        insert_sql = "Insert into product values(%s, %s)"
        cursor.execute(insert_sql, ('A001', '아메리카노')) # 이미 존재하므로 예외발생
        cursor.execute(insert_sql, ('C004', '라떼4'))
        print("Record 2 product successfully ")
        conn.commit()
    except Error as error:
        print("Failed to update record to database rollback: {}".format(error))
        conn.rollback()
    finally:
        if conn.is_connected():
            conn.autocommit = True
            cursor.close()
            conn.close()
            print("connection is closed")


def transaction_fail2():
    try:
        print('Connecting to MySQL database...')
        conn = ConnectionPool.get_instance().get_connection()
        print(type(conn))
        conn.autocommit = False
        cursor = conn.cursor()
        insert_sql = "Insert into product values(%s, %s)"
        cursor.execute(insert_sql, ('D001', '아메리카노 Set'))
        cursor.execute(insert_sql, ('C001', '라떼1')) # 이미 존재하므로 예외발생
        print("Record 2 product successfully ")
        conn.commit()
    except Error as error:
        print("Failed to update record to database rollback: {}".format(error))
        conn.rollback()
    finally:
        if conn.is_connected():
            conn.autocommit = True
            cursor.close()
            conn.close()
            print("connection is closed")


def transaction_success():
    try:
        print('Connecting to MySQL database...')
        conn = ConnectionPool.get_instance().get_connection()
        print(type(conn))
        conn.autocommit = False
        cursor = conn.cursor()
        insert_sql = "Insert into product values(%s, %s)"
        cursor.execute(insert_sql, ('D001', '아메리카노 Set'))
        cursor.execute(insert_sql, ('C005', '라떼5'))
        print("Record 2 product successfully ")
        conn.commit()
    except Error as error:
        print("Failed to update record to database rollback: {}".format(error))
        conn.rollback()
    finally:
        if conn.is_connected():
            conn.autocommit = True
            cursor.close()
            conn.close()
            print("connection is closed")
