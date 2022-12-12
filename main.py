# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import jaydebeapi

from JdbcCommons import JdbcAction, driver_class, drivers_path


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def local_mysql_test():
    url = 'jdbc:mysql://172.100.1.100/zhuzhenjie?characterEncoding=utf-8&autoReconnect=true&failOverReadOnly=false' \
          '&useSSL=false&serverTimezone=Asia/Shanghai '

    user = 'root'
    password = 'Root@123#'

    driver = 'com.mysql.cj.jdbc.Driver'

    jar_file = r'.drivers/mysql-connector-java-8.0.21.jar'

    sql_str = 'show databases'

    conn = jaydebeapi.connect(driver, url, [user, password], jar_file)

    curs = conn.cursor()
    curs.execute(sql_str)
    result = curs.fetchall()

    print(result)

    curs.close()
    conn.close()


def action_demo():
    action = JdbcAction(driver_class["mysql8"],
                        "jdbc:mysql://172.100.1.100/zhuzhenjie?characterEncoding=utf-8&autoReconnect=true"
                        "&failOverReadOnly=false&useSSL=false&serverTimezone=Asia/Shanghai",
                        "root", "Root@123#",
                        drivers_path["mysql8"])
    rows = action.execute("""
        show tables
    """)
    print(rows)
    action.close()


def taos26_test():
    action = JdbcAction(driver_class["taos2.0.38"],
                        "jdbc:TAOS-RS://10.250.5.10:6041/demo",
                        "root", "taosdata",
                        drivers_path["taos2.0.38"])
    rows = action.execute("""
        show databases;
    """)
    for row in rows:
        print(row)

    action.close()


if __name__ == '__main__':
    taos26_test()
