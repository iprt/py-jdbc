# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import jaydebeapi
import os

from commons.JdbcCommons import JdbcAction
from drivers.Constant import drivers_class, drivers_path


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def local_mysql_test():
    url = 'jdbc:mysql://dev.iproute.org/mysql' \
          '?characterEncoding=utf-8' \
          '&autoReconnect=true' \
          '&failOverReadOnly=false' \
          '&useSSL=false' \
          '&serverTimezone=Asia/Shanghai'

    user = 'root'
    password = 'root'

    driver = 'com.mysql.cj.jdbc.Driver'

    jar_file = r'.drivers/mysql-connector-java-8.0.21.jar'

    # sql_str = 'show databases'
    sql_str = 'select user,host from user;'
    conn = jaydebeapi.connect(driver, url, [user, password], jar_file)

    curs = conn.cursor()
    curs.execute(sql_str)
    result = curs.fetchall()

    # print(result)
    for row in result:
        print(row)

    curs.close()
    conn.close()


def action_demo():
    action = JdbcAction(drivers_class["mysql8"],
                        "jdbc:mysql://dev.iproute.org/mysql?characterEncoding=utf-8&autoReconnect=true"
                        "&failOverReadOnly=false&useSSL=false&serverTimezone=Asia/Shanghai",
                        "root", "root",
                        drivers_path["mysql8"])
    first_sql = 'show tables'
    print("first sql is ===>", first_sql)
    rows = action.execute(first_sql)
    # print(rows)
    for row in rows:
        print(row)

    second_sql = 'select user,host from user;'
    print("second sql is ===>", second_sql)
    rows = action.execute(second_sql)
    for row in rows:
        print(row)

    action.close()


def taos26_test():
    action = JdbcAction(drivers_class["taos2.0.38"],
                        "jdbc:TAOS-RS://10.250.5.10:6041/demo",
                        "root", "taosdata",
                        drivers_path["taos2.0.38"])
    rows = action.execute("""
        show databases;
    """)

    for row in rows:
        print(row)
    action.close()


def taos31_test():
    action = JdbcAction(drivers_class["taos3.1.0"],
                        "jdbc:TAOS-RS://dev.iproute.org:6041/iot_data",
                        "root", "taosdata",
                        drivers_path["taos3.1.0"]
                        )
    rows = action.execute("""
        select * from wf_sba order by `time` desc limit 10
    """)
    for row in rows:
        print(row)
    action.close()


if __name__ == '__main__':
    # set JAVA_HOME env
    os.environ["JAVA_HOME"] = "./jre"
    local_mysql_test()
    # taos26_test()
    # action_demo()
    # taos31_test()
