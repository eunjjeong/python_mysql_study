from mysql.connector import Error
from dml.connection_pool import ConnectionPool

# 하나씩 가져와서 비교하고 print
def query_with_fetchone(sql):
    try:
        conn = ConnectionPool.get_instance().get_connection()
        cursor = conn.cursor()
        cursor.execute(sql)
        row = cursor.fetchone()
        while row is not None:
            print(type(row), " : ", row)
            row = cursor.fetchone()
    except Error as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

# 전체다 가져와서 print
def query_with_fetchall(sql):
    try:
        conn = ConnectionPool.get_instance().get_connection()
        cursor = conn.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        print('Total Row(s):', cursor.rowcount)
        for row in rows:
            print(type(row), " ", row)
    except Error as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


def query_with_fetchall2(sql):
    try:
        conn = ConnectionPool.get_instance().get_connection()
        cursor = conn.cursor()
        cursor.execute(sql)
        return cursor.fetchall()
    except Error as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


def query_with_fetchall_by_code(sql, code):
    args = (code,)
    try:
        conn = ConnectionPool.get_instance().get_connection()
        cursor = conn.cursor()
        cursor.execute(sql, args)
        return cursor.fetchall()
    except Error as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


