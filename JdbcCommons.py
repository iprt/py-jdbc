import jaydebeapi

driver_class = {
    "mysql8": "com.mysql.cj.jdbc.Driver",
    "dm8": "dm.jdbc.driver.DmDriver",
    "taos2.0.8": "com.taosdata.jdbc.rs.RestfulDriver"
}

drivers_path = {
    "mysql8": r".drivers/mysql-connector-java-8.0.21.jar",
    "taos2.0.38": r".drivers/taos-jdbcdriver-2.0.38_bundle.jar",
    "dm8": r".drivers/DmJdbcDriver18.jar"
}


class JdbcAction:
    def __init__(self, driver, jdbcUrl, username, password, jarPath):
        self.driverName = driver
        self.jdbcUrl = jdbcUrl
        self.username = username
        self.password = password
        self.jarPath = jarPath

        self.conn = jaydebeapi.connect(driver, jdbcUrl, [username, password], jarPath)

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
