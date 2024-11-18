from models.ConcetDb import DbConnect
from models.Usuarios import Usuarios
import uuid

class Dispesas():
    def __init__(self, descricao, valor, datainit, datafim, usuarios):
        self._id = str(uuid.uuid4())
        self._descricao = descricao
        self._valor = valor
        self._datainit = datainit
        self._datafim = datafim
        self._usuarios = usuarios

    def select_all(self):
        conn = DbConnect()
        return conn.fetchall("SELECT * FROM Dispesas")

    def get_valores(self, data):
        conn = DbConnect()
        query = f"SELECT COUNT(valor), user_id FROM Dispesas where user_id = {self._usuarios._id} AND({data} >= datainit and {data} <= datafim)"
        return conn.fetchall(query)

    def insert(self):
        conn = DbConnect()
        query = "INSERT INTO Dispesas (id, descricao, valor, datainit, datafim, user_id) VALUES ('{}', '{}', '{}', '{}', '{}')".format(self._id, self._descricao, self._valor, self._datainit, self._datafim, self._usuarios._id)
        conn.execute(query)