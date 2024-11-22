import os
from time import sleep
from controllers.FinaceController import Finace
from uuid import uuid4

def finace_menu():
    os.system('cls')
    finace = Finace()
    while True:

        print("Bem vindo ao se Controle Finaceiro")
        print("1. Cadastrar")
        print("2. Listar")
        print("3. Editar")
        print("4. Excluir")
        print("0. Sair")


        match int(input("Enter your choice: ")):
            case 1:
                name = str(input("Digite o nome da despesa: "))
                value = float(input("Digite o valor da despesa: "))
                start_date = str(input("Digite a data de inicio: "))
                end_date = str(input("Digite a data de fim: "))

                if finace.add_dispesa({
                    'id': str(uuid4()),
                    'name': name,
                    'value': value,
                    'start_date': start_date,
                    'end_date': end_date
                }):
                    print("Despesa cadastrada com sucesso")
                else:
                    print("Erro ao cadastrar despesa")

                sleep(1)
                os.system('cls')

            case 2:
                os.system('cls')
                finace.get_all_dispesas()

                input("Pressione Enter para continuar...")
                os.system('cls')

            case 3:
                pass
            case 4:
                pass
            case 0:
                os.system('cls')
                break


def menu():
    print(fr"""
          ,'""`.
         / _  _ \
         |(@)(@)|
         )  __  (
        /,'))((`.\
       (( ((  )) ))      OLA SOU ICARO SEJA BEM VINDO 
        `\ `)(' /'
    """)


    while True:
        match int(input("1. Finace\n0. Exit\nEnter your choice: ")):
            case 1:
                finace_menu()
            case 0:
                exit()
            case _:
                print("Invalid choice")

if __name__ == "__main__":
    menu()