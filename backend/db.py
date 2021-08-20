import sqlite3


class DBLoader:
    def __init__(self,):
        conn = sqlite3.connect("cbdb_20201110.db")
        self.c = conn.cursor()

    def extract(self, query: str):
        self.c.execute(query)
        return self.c.fetchall()
