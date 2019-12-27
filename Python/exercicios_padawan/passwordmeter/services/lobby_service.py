import time
from random import randint

peoples = []


def menu_password_meter():
    print(f'\n1 - Cadastrar uma Pessoa\n2 - Listar pessoas Cadastradas')

    opção = int(input("\nEu: "))
    if opção == 1:
        cadastro()

    if opção == 2:
        listar()


def cadastro():
    id = str(randint(0,100))
    print(f'Seu ID: {id}')
    nome = input("\nNome: ")
    senha = input("Senha: ")
    idade = int(input("Idade: "))
    genero = int(input(f'\nGenero:\n1 - Masculino | 2 - Feminino: '))

    if genero == 1:
        genero = 'Masculino'

    if genero == 2:
        genero = 'Feminino'

    # peoples.append({"Id": id,
    #                    "Nome": nome,
    #                    "Senha": senha,
    #                    "Idade": idade,
    #                    "Genero": genero}
    #                    )
    with open('bd.txt', "a") as Banco:
        Banco.write(f"{id};{nome};{senha};{idade};{genero}")

    print(f'Cadastrando {nome}...')
    time.sleep(2.5)
    menu_password_meter()


def listar():
    print(f'\n1 - Encontrar um Usuario\n2 - Excluir um Usuario\n3 - Voltar')
    opção = int(input("\nEu: "))

    if opção == 1:
        procurar = input('Digite o ID: ')
        for i in peoples:
            if procurar == i["Id"]:
                print(f'Pessoa com o ID: {i["Id"]}, Corresponde para {i["Nome"]}')
                print(f'\n1 - Realizar alguma ação neste usuario\n2 - Voltar')

                if opção == 1:
                    pass
                if opção == 2:
                    listar()
    if opção == 2:
        remove = input('Informe-nós o ID: ')
        for i in peoples:
            if remove == i["Id"]:
                print(peoples)
    if opção == 3:
        menu_password_meter()

# def alteracao_user():
#     print(f'{}\n1 - Alterar dados\n2 - Sair')
#     opção = int(input("\nEu: "))
#
#     if opção == 1:
#         alteracao = input('Digite o ID')
#         for i in peoples:
#             if alteracao == i["Id"]:
#                 print(f'Sua atual senha: {i["Senha"]}')