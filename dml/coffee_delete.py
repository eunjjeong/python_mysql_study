from mysql.connector import Error

from dml.connection_pool import ConnectionPool


def delete_product(sql, code):
    try:
        conn = ConnectionPool.get_instance().get_connection()
        cursor = conn.cursor()
        cursor.execute(sql, (code,))
        conn.commit()
    except Error as error:
        print(error)
    finally:
        cursor.close()
        conn.close()