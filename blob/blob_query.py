from mysql.connector import Error

from blob.blob_read_write import read_file_blob, write_file_blob
from blob.connection_pool import ConnectionPool


def insert_blob(query, file_name, file_path):
    data = read_file_blob(file_path)
    args = (file_name, data)
    try:
        conn = ConnectionPool.get_instance().get_connection()
        cursor = conn.cursor()
        cursor.execute(query, args)
        conn.commit()
    except Error as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


def update_blob(query, file_name, file_path, no):
    data = read_file_blob(file_path)
    args = (file_name, data, no)
    try:
        conn = ConnectionPool.get_instance().get_connection()
        cursor = conn.cursor()
        cursor.execute(query, args)
        conn.commit()
    except Error as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


def read_blob(query, no, filename):
    try:
        conn = ConnectionPool.get_instance().get_connection()
        cursor = conn.cursor()
        cursor.execute(query, (no,))
        photo = cursor.fetchone()[0]
        write_file_blob(photo, filename)
    except Error as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


def delete_blob(sql, no):
    try:
        conn = ConnectionPool.get_instance().get_connection()
        cursor = conn.cursor()
        cursor.execute(sql, (no,))
        conn.commit()
    except Error as error:
        print(error)
    finally:
        cursor.close()
        conn.close()
