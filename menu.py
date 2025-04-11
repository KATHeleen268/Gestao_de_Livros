from Funções import inserir_livros, remover_livros, listar_livros, buscar_livros, situacao_livro, alugar_livros, devolver_livros

print("Olá bem vindo a biblioteca")

def menu(biblioteca):
    while True:
        print("1. Inserir livros")
        print("2. Remover livros")
        print("3. Listar livros")
        print("4. Buscar livros")
        print("5. Checar a situação do livro")
        print("6. Alugar livros")
        print("7. Devolver livros")
        print("8. Sair")

        opcao = input("Digite uma opcâo: ")

        if opcao == "1":
                print("Inserindo livros")
                inserir_livros(biblioteca)
        elif opcao == "2":
                print("Removendo livros")
                remover_livros(biblioteca)
        elif opcao == "3":
                print("Listando livros")
                listar_livros(biblioteca)
        elif opcao == "4":
                print("Buscando livros")
                buscar_livros(biblioteca)
        elif opcao == "5":
               print("Checando a situação do livro")
               situacao_livro(biblioteca)
        elif opcao == "6":
               print("Alugando livros")
               alugar_livros(biblioteca)
        elif opcao == "7":
               print("Devolvendo o livro")
               devolver_livros(biblioteca)
        elif opcao == "8":
                print("Saindo do programa")
                break
        else:
            print("Não existe essa opção! Tente novamente com um número válido.")