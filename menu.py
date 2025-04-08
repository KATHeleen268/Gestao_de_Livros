from Funções import inserir_livros, remover_livros

print("Olá bem vindo a biblioteca")

def menu(biblioteca):
    while True:
        print("1. Inserir livros")
        print("2. Remover livros")
        print("3. Listar livros")
        print("4. Buscar livros")
        print("5. Sair")

        opcao = input("Digite uma opcâo: ")

        if opcao == "1":
                print("Inserindo livros")
                inserir_livros(biblioteca)
        elif opcao == "2":
                print("Removendo livros")
                remover_livros(biblioteca)
        elif opcao == "3":
                print("Listando livros")
        elif opcao == "4":
                print("Buscando livros")
        elif opcao == "5":
                print("Saindo do programa")
                break
        else:
            print("Não existe essa opção! Tente novamente com um número válido.")