from mysql.connector import Error, errorcode
from dml.connection_pool import ConnectionPool

PROCEDURE_NAME = 'proc_sale_stat'
PROCEDURE_SRC = """
        CREATE PROCEDURE proc_sale_stat()
        BEGIN
            select sum(@saleprice := price*saleCnt) sale_price,
                    sum(@addtax := ceil(@saleprice/11)) addtax_price,
                    sum(@supprice := @saleprice - @addtax) supply_price,
                    sum(@marPrice := round(@supprice * (marginRate/100))) margin_price
            from sale s join product p on s.code = p.code;
        END 
        """

def create_procedure():
    try:
        conn = ConnectionPool.get_instance().get_connection()
        cursor = conn.cursor()
        cursor.execute(PROCEDURE_SRC)
        print("CREATE PROCEDURE {}".format(PROCEDURE_NAME))
    except Error as err:
        # print(err)
        if err.errno == errorcode.ER_SP_ALREADY_EXISTS:
            cursor.execute("DROP PROCEDURE {}".format(PROCEDURE_NAME))
            print("DROP PROCEDURE {}".format(PROCEDURE_NAME))
            cursor.execute(PROCEDURE_SRC)
            print("CREATE PROCEDURE {}".format(PROCEDURE_NAME))
        else:
            print(err.msg)
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
