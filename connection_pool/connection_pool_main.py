import inspect
from connection_pool.connection_pool_study import DatabaseConnectionPool


def connect_pool01():
    print("\n== {}() ==".format(inspect.stack()[0][3]))
    connection = DatabaseConnectionPool.get_instance().get_connection()
    print(type(connection), connection)
    connection.close()


if __name__ == '__main__':
    for i in range(10):
        connect_pool01()