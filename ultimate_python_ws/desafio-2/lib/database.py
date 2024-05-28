import sqlite3

class Database():
    def __init__(self, db_file):
        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()

    def execute_query(self, query, params=None):    
        if params:
            return self.cursor.execute(query, params)
        
        return self.cursor.execute(query)