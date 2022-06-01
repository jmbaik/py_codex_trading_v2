import pymysql


class MetStockDB:
    def __init__(self):
        self.conn = pymysql.connect(host='localhost', user='metstock', password='man100', db='codex', charset='utf8')
        self.init_table()

    def __del__(self):
        self.conn.close()

    def init_table(self):
        with self.conn.cursor() as curs:
            sql = """
            CREATE TABLE IF NOT EXISTS balance (
                code VARCHAR(20),
                bid_price bigint(20) not null,
                quantity bigint(20) not null ,
                created_at varchar(14) not null,
                will_clear_at varchar(14),
                PRIMARY KEY (code))
            """
            curs.execute(sql)
        self.conn.commit()

