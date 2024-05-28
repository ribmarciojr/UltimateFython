import sqlite3

class Database():
    def __init__(self, db_file):
        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()

    def execute_query(self, query, params=None):    
        if params:
            return self.cursor.execute(query, params)
        
        return self.cursor.execute(query)
    
    def users_table_init(self):
        self.execute_query(("""CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY NOT NULL,
            name TEXT NOT NULL, 
            password TEXT NOT NULL 
        )"""))