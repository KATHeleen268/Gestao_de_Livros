#ordem id, titulo, autores, editora, ano, situação

#função de inserir livros
def inserir_livros(biblioteca):
    id = input("Digite o código do livro: ")
    titulo = input("Digite o titulo do livro: ")
    autores = input("Digite o nome do(s) autor(a) do livro: ")
    editora = input("digite o nome da editora do livro: ")
    ano = int(input("Digite o ano de lançamento do livro: "))

    novo_livro = {
        "id": id,
        "titulo": titulo,
        "autores": autores,
        "editora": editora,
        "ano": ano,
        "situação": "Disponível"
    }

    biblioteca.append(novo_livro)
    print("Livro inserido com sucesso!")


#função remover o livro
def remover_livros(biblioteca):
        titulo_remover = input("Digite o titulo do livro que você deseja remover: ")

        for livro in biblioteca:
            if livro["titulo"] == titulo_remover:
                biblioteca.remove(livro)
                print(f"Livro com titulo {titulo_remover} removido com sucesso!")
                return
        print(f"Nenhum livro com o titulo {titulo_remover} foi encontrado.")


#função que checa a situação do livro
def situacao_livro(biblioteca):
    titulo_situacao = input("Digite o titulo do livro que deseja ver a situação: ").strip().lower()
    encontrado = False

    for livro in biblioteca:
        if titulo_situacao in livro["titulo"].strip().lower():
            print(f"O livro {livro['titulo']} está {livro['situação']}")
            encontrado = True
            break

    if not encontrado:
        print("Livro não existe na biblioteca.")
     
#função de listar os livros de formas geral e especificas
def listar_livros(biblioteca):
    while True:
        print("1. Listar todos os livros")
        print("2. Listar apenas os livros disponíveis")
        print("3. Listar apenas os livros emprestados")
        print("4. Listar por editora")
        print("5. Listar por ano")
        print("6. Voltar ao menu principal")
        
        opcao1 = input("Qual a listagem que deseja? ")
        
        if opcao1 == "1":
            for livro in biblioteca:
                print(livro)
        elif opcao1 == "2":
            for livro in biblioteca:
                if livro['situação'] == "Disponível":
                    print(livro)
        elif opcao1 == "3":
            for livro in biblioteca:
                if livro["situação"] == "Emprestado": 
                    print(livro)
        elif opcao1 == "4":
            editora = input("Digite o nome da editora: ").strip().lower()
            for livro in biblioteca:
                if livro["editora"].strip().lower() == editora:
                    print(livro)
        elif opcao1 == "5":
            ano = int(input("Digite o ano que deseja: "))
            for livro in biblioteca:
                if livro["ano"] == ano:
                    print(livro)
        elif opcao1 == "6":
            print("retornando ao menu principal")
            break
        else:
            print("Opção inválida. Tente novamente com um valor válido.")

#função de buscar_livros
def buscar_livros(biblioteca):
    try:
        id_busca = int(input("Digite o id do livro desejado: "))
    except ValueError:
        print("ID inválido! Digite apenas números.")
        return

    encontrado = False

    for livro in biblioteca:
        if livro ['id'] == id_busca:
                print(livro)
                encontrado = True
                break

    if not encontrado:
        print("Não existe na biblioteca")
        