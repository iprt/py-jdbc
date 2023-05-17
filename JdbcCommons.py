import jaydebeapi

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
