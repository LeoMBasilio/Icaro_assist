from models.DataBaseModel import Database
class Finace:
    def __init__(self):
        self.db = Database('db/finace.db')
        self.table = {
            'table': 'finace',
            'columns': {
                'id': 'TEXT PRIMARY KEY',
                'name': 'TEXT',
                'value': 'REAL',
                'start_date': 'TEXT',
                'End_date': 'TEXT'
            }
        }

        self.db.create_table(self.table['table'], self.table['columns'])

    def add_dispesa(self, values):
        return self.db.insert_values(self.table['table'], values)
    
    def get_all_dispesas(self):
        despesas = self.db.get_all(self.table['table'])
        print('Despesas Cadastradas')
        print(f'{"id".ljust(36)} | {"Nome".ljust(25)} | {"Valor".ljust(25)} | {"Data de Inicio".ljust(25)} | Data de Fim')
        for i in despesas:
            print(f'{i[0]} | {i[1].ljust(25)} | {str(i[2]).ljust(25)} | {i[3].ljust(25)} | {i[4]}')
            

    def get_dispesa(self, condition):
        pass
