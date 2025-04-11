#importa as funções que estão em outro arqui
from Funções import inserir_livros, remover_livros, listar_livros, buscar_livros, situacao_livro, alugar_livros, devolver_livros

#mensagem de boas vindas
print("Olá bem vindo a biblioteca")

#função de menu principal que receb como parametro a lista de livros e as opcoes disponiveis para interação do usuario
def menu(biblioteca):
    while True: #loop que só será encerrado se o usuario esclher sair
        print("1. Inserir livros")
        print("2. Remover livros")
        print("3. Listar livros")
        print("4. Buscar livros")
        print("5. Checar a situação do livro")
        print("6. Alugar livros")
        print("7. Devolver livros")
        print("8. Sair")

        opcao = input("Digite uma opcâo: ") #o usuario escolhe qual opcao do menu deseja executar

        if opcao == "1":
                print("Inserindo livros")
                inserir_livros(biblioteca)#chama a funçao que insere os livros na biblioteca
        elif opcao == "2":
                print("Removendo livros")
                remover_livros(biblioteca) #chama a função que remove um livro da lista pelo seu titulo
        elif opcao == "3":
                print("Listando livros")
                listar_livros(biblioteca) #chama a função que lista livros e seu submenu onde o usuario escolhe o que quer ver sendo listado
        elif opcao == "4":
                print("Buscando livros")
                buscar_livros(biblioteca) #chama a função que busca um livro especifico pelo id
        elif opcao == "5":
               print("Checando a situação do livro")
               situacao_livro(biblioteca) #chama a funçãoo que irá mostrar ao usuario se o livro esta disponivel ou não
        elif opcao == "6":
               print("Alugando livros")
               alugar_livros(biblioteca) #chama a função que permite ao usuario alugar livros
        elif opcao == "7":
               print("Devolvendo o livro")
               devolver_livros(biblioteca) #chama a função que permite ao usuario fazer a devolução dos livros
        elif opcao == "8":
                print("Saindo do programa") #encerra o programa, saindo do loop wile
                break
        else:
            print("Não existe essa opção! Tente novamente com um número válido.") #se o usuario digitar algum valor invalido, o sistema irá avisar