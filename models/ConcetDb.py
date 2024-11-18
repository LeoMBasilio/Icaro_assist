import sqlite3

class DbConnect:
    def __init__(self):
        self.con = sqlite3.connect('IacaroDb.db')
        self.cursor = self.con.cursor()

    def init_dataBase(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS Dispesas (id TEXT PRIMARY KEY, descricao TEXT NOT NULL, valor REAL NOT NULL, datainit TEXT NOT NULL, datafim TEXT NOT NULL, user_id TEXT NOT NULL)")
        self.cursor.execute("CREATE TABLE IF NOT EXISTS Usuarios (id TEXT PRIMARY KEY, nome TEXT NOT NULL, email TEXT NOT NULL, telefone TEXT NOT NULL, renda REAL NOT NULL)")
        self.con.commit()
        self.con.close()

    def execute(self, query):
        self.cursor.execute(query)
        self.con.commit()

    def fetchall(self, query):
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def fetchone(self, query):
        self.cursor.execute(query)
        return self.cursor.fetchone()
    
    def close(self):
        self.con.close()