from models.ConcetDb import DbConnect
import uuid

class Usuarios:
    def __init__(self, nome, email, telefone, renda):
        self.id = str(uuid.uuid4())
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.renda = renda

    def get_user(self):
        conn = DbConnect()
        query = "SELECT * FROM Usuarios where id = '{}' or email = '{}'".format(self.id, self.email)
        return conn.fetchall(query)
    
    def insert(self):
        conn = DbConnect()
        query = "INSERT INTO Usuarios (id, nome, email, telefone, renda) VALUES ('{}', '{}', '{}', '{}', '{}')".format(self.id, self.nome, self.email, self.telefone, self.renda)
        conn.execute(query)

    def update_telefone(self, telefone):
        conn = DbConnect()
        query = "UPDATE Usuarios SET telefone = '{}' WHERE id = '{}'".format(telefone, self.id)
        conn.execute(query)

    def update_email(self, email):
        conn = DbConnect()
        query = "UPDATE Usuarios SET email = '{}' WHERE id = '{}'".format(email, self.id)
        conn.execute(query)

    def update_renda(self, renda):
        conn = DbConnect()
        query = "UPDATE Usuarios SET renda = '{}' WHERE id = '{}'".format(renda, self.id)
        conn.execute(query)

    def delete(self):
        conn = DbConnect()
        query = "DELETE FROM Usuarios WHERE id = '{}'".format(self.id)
        conn.execute(query)