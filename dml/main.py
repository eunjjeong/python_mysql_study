import pandas as pd

from dml.Fetch_Query import query_with_fetchmany
from dml.coffee_delete import delete_product
from dml.coffee_insert import insert_product, insert_products
from dml.coffee_procedure import call_sale_stat_sp, call_order_price_by_issale
from dml.coffee_select import query_with_fetchone, query_with_fetchall, query_with_fetchall2, \
    query_with_fetchall_by_code
from dml.coffee_update import update_product
from dml.connection_pool import ConnectionPool
from dml.create_procedure import create_procedure
from dml.transaction_query import transaction_fail1, transaction_fail2, transaction_success


# ctrl + alt + m = 메소드 만들기
def connection_pool_test():
    connection_pool = ConnectionPool.get_instance()
    connection = connection_pool.get_connection()
    print("connection : ", connection)


def fetch_all2_test(sql):
    query_with_fetchall(sql)
    res = query_with_fetchall2(sql)
    print(type(res), 'size = ', len(res))
    # for pno, pname in res:
    #     print(pno, pname)
    query_with_fetchmany(sql)

    # query_with_fetchall(sale_select_sql)
    # res = query_with_fetchall2(sale_select_sql)
    # print(type(res), 'size = ', len(res))
    # for pno, pname in res:
    #     print(pno, pname)
    # query_with_fetchmany(sale_select_sql)


def fetch_one_test():
    query_with_fetchone(product_select_sql)
    query_with_fetchone(sale_select_sql)


def fetch_all_where_test():
    product_select_whiere01 = "select * from product where code = %s"
    res = query_with_fetchall_by_code(product_select_whiere01, 'A001')
    print(res)
    # product_select_whiere02 = "select * from product where code = {}".format('A001')
    # query_with_fetchall(product_select_whiere02)


def insert_test():
    insert_sql = "insert into product values(%s, %s)"
    insert_product(insert_sql, 'C001', '라떼')
    products = [('C002', '라떼2'), ('C003', '라떼3'), ('C004', '라떼4')]
    insert_products(insert_sql, products)
    query_with_fetchall(product_select_sql)


def update_test():
    select_sql_by_code = "select code, name from product where code = '{code}'".format(code='C001')
    query_with_fetchone(select_sql_by_code)
    update_sql = "update product set name = %s where code = %s"
    update_product(update_sql, '라떼수정', 'C001')
    query_with_fetchone(select_sql_by_code)


def delete_test():
    delete_select_sql = "select code, name from product where code like 'C___'"
    res = query_with_fetchall2(delete_select_sql)
    columns_list = ['code', 'name']
    df = pd.DataFrame(res, columns=columns_list)
    print(df)
    delete_sql = "delete from product where code = %s"
    delete_product(delete_sql, 'C004')
    for code, name in (query_with_fetchall2(delete_select_sql)):
        print(code, " ", name)


if __name__ == "__main__":
    connection_pool_test()

    product_select_sql = "select * from product"
    sale_select_sql = "select * from sale"

    # fetch_one_test()
    # fetch_all2_test(product_select_sql)
    # fetch_all2_test(sale_select_sql)

    # where
    # fetch_all_where_test()

    # insert문
    # insert_test()

    # update문
    # update_test()

    # Delete문
    # delete_test()

    # transaction
    # transaction_fail1()
    # transaction_fail2()
    # transaction_success()

    # create_procedure()
    call_sale_stat_sp('proc_sale_stat')
    print()
    call_order_price_by_issale('proc_saledetail_orderby', False)
    print()
    call_order_price_by_issale('proc_saledetail_orderby', True)

