from mysql.connector import Error
from dml.connection_pool import ConnectionPool


def update_product(sql, name, code):
    args = (name, code)
    try:
        conn = ConnectionPool.get_instance().get_connection()
        cursor = conn.cursor()
        cursor.execute(sql, args)
        conn.commit()
    except Error as error:
        print(error)
    finally:
        cursor.close()
        conn.close()