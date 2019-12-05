from mysql.connector import Error
from dml.connection_pool import ConnectionPool


def iter_row(cursor, size=5):
    while True:
        rows = cursor.fetchmany(size)
        if not rows:
            break
        for row in rows:
            yield row


def query_with_fetchmany(sql):
    try:
        conn = ConnectionPool.get_instance().get_connection()
        cursor = conn.cursor()
        cursor.execute(sql)
        for row in iter_row(cursor, 5):
            print(type(row), " ", row)
    except Error as e:
        print(e)
    finally:
        cursor.close()
        conn.close()