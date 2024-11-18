from controllers.FinaceController import Finace
from models.Usuarios import Usuarios
from models.ConcetDb import DbConnect

def finace_menu(user):
    print("Bem vindo ao se Controle Finaceiro")
    print("1. Cadastrar")
    print("2. Listar")
    print("3. Editar")
    print("4. Excluir")
    print("0. Sair")

    finace = Finace()

    match int(input("Enter your choice: ")):
        case 1:
            if not finace.getDispesas():
                nome = input("Nome: ")
                valor = input("Valor: ")
                datainit = input("Data Inicial: ")
                datafim = input("Data Final: ")
                usuario = input("Usuario: ")

                finace.addDispesas(nome, valor, datainit, datafim, usuario)
      
        case 0:
            menu()


def menu():
    print("Ola sou Icaro, seja bem vindo")

    name = str(input("Digite seu nome: "))
    email = str(input("Digite seu email: "))
    telefone = str(input("Digite seu telefone: "))
    renda = str(input("Digite sua renda: "))

    newUser = Usuarios(name, email, telefone, renda)

    if not newUser.get_user():
        newUser.insert()

    while True:
        match int(input("1. Finace\n0. Exit\nEnter your choice: ")):
            case 1:
                Finace(newUser)
            case _:
                exit()

if __name__ == "__main__":
    DbConnect().init_dataBase()
    menu()