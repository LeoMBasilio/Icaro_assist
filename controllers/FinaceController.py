from models.Dispesas import Dispesas
from models.Usuarios import Usuarios

class Finace(Dispesas):
    def __init__(self, user, dispesas):
        self.dispesas = Dispesas()
        self.usuarios = user

    def getDispesas(self):
        resp = self.dispesas.get_valores()
        if resp:
            result = {
                "user": self.usuarios.get_user(),
                "valor": resp['valor']
            }

            return result
        else:
            return None

    def getUsuarios(self):
        return self.usuarios.get_user()

    def addDispesas(self, nome, valor, datainit, datafim, usuario):
        self.dispesas.addDispesas(nome, valor, datainit, datafim, usuario)

    def addUsuarios(self, nome, email, telefone, renda):
        self.usuarios.addUsuarios(nome, email, telefone, renda)

    def deleteDispesas(self, id):
        self.dispesas.deleteDispesas(id)

    def deleteUsuarios(self, id):
        self.usuarios.deleteUsuarios(id)

    def updateDispesas(self, id, nome, valor, data, usuario):
        self.dispesas.updateDispesas(id, nome, valor, data, usuario)

    def updateUsuarios(self, id, nome, email, senha):
        self.usuarios.updateUsuarios(id, nome, email, senha)
