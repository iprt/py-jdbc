import jaydebeapi

drivers_class = {
    "mysql8": "com.mysql.cj.jdbc.Driver",
    "taos2.0.38": "com.taosdata.jdbc.rs.RestfulDriver",
    "dm8": "dm.jdbc.driver.DmDriver"
}

drivers_path = {
    "mysql8": r".drivers/mysql-connector-java-8.0.21.jar",
    "taos2.0.38": r".drivers/taos-jdbcdriver-2.0.38_bundle.jar",
    "dm8": r".drivers/DmJdbcDriver18.jar"
}


class JdbcAction:
    def __init__(self, driver, jdbc_url, username, password, jar_path):
        self.driverName = driver
        self.jdbcUrl = jdbc_url
        self.username = username
        self.password = password
        self.jarPath = jar_path

        self.conn = jaydebeapi.connect(driver, jdbc_url, [username, password], jar_path)

    def execute(self, sql):
        curs = self.conn.cursor()
        curs.execute(sql)
        rows = curs.fetchall()
        # print(result)
        curs.close()
        # self.conn.close()
        return rows

    def close(self):
        self.conn.close()
