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
        "ano": ano
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
        print(f"Nenhum filme com o titulo {titulo_remover} foi encontrado.")