import sqlite3

class database:
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cursor = self.conn.cursor()
    
    def get_all(self, table):
        self.cursor.execute("select * from ", table)
        return self.cursor.fetchall()

    def insert_values(self, table, values):
        try:
            key = ''
            value = ''
            for i in values:
                key += f'{i}, '
                value += f'{values[i]}, '
            
            query = f'''
                INSERT INTO {table}({key[:-2]}) VALUES ({value[:-2]});
            '''

            if self.cursor.execute(query):
                self.conn.commit()
                return True
            return False
        except Exception as e:
            return e
        
    def update_values(self, table, values, condition):
        try:
            key = ''
            where = ''
            for i in values:
                key += f'{i} = {values[i]}, '

            for i in condition:
                where += f' where {condition[i]}' if i == 'where' else ''

            query = f'''
                UPDATE {table} SET ({key[:-2]}){where}
            '''

            if self.cursor.execute(query):
                self.conn.commit()
                return True
            return False    
        except Exception as e:
            return e        
    
    def delete_values(self, table, condition):
        try:
            where = ''
            for i in condition:
                where += f' where {condition[i]}' if i == 'where' else ''

            query = f'''
                DELETE FROM {table} {where}
            '''

            if self.cursor.execute(query):
                self.conn.commit()
                return True
            return False
            
        except Exception as e:
            return e
    
