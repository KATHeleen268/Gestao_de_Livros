#importando a função salvar_livros usada sempre que um dado é alterado na biblioteca salvando assim no csv
from funçõescsv import salvar_livros

#ordem id, titulo, autores, editora, ano, situação

#função de inserir livros que recebe os dados do usario e depois adicona e salva na biblioteca
def inserir_livros(biblioteca):
    id = int(input("Digite o código do livro: ")) #pede o id ao usuario e o receb como inteiro 
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
    #cria um dicionario com os novos dados e define sua situação inicial como padrão disponivel
    biblioteca.append(novo_livro) 
    salvar_livros(biblioteca)
    print("Livro inserido com sucesso!")


#função remover o livro, que remove um livro da lista, tendo como chave o titulo
def remover_livros(biblioteca):
        titulo_remover = input("Digite o titulo do livro que você deseja remover: ") #pedde o titulo ao usuario par poder comparar e imprimir

        for livro in biblioteca:
            if livro["titulo"] == titulo_remover:
                biblioteca.remove(livro)
                salvar_livros(biblioteca)
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

#função de alugar livros ou seja troca a situação de disponivel para emprestado, caso não esteja disponivel
def alugar_livros(biblioteca):
    id_aluguel = int(input("Digite o id do livro que deseja alugar: "))
    
    encontrado = False

    for livro in biblioteca:
        if livro['id'] == id_aluguel:
            print(f"O livro '{livro['titulo']}' (ID : {livro['id']}) foi encontrado")
            encontrado = True
            if livro["situação"] == "Disponível":
                livro["situação"] = "Emprestado"
                salvar_livros(biblioteca)
                print(f"O livro '{livro['titulo']}' foi emprestado com sucesso!")
            else:
                print(f"O livro '{livro['titulo']}' já está emprestado.")
            break
    if not encontrado:
        print("O livro desejado não foi encontrado.")

#função de devolução de livros
def devolver_livros(biblioteca):
    id_devolucao = int(input("Digite o ID do livro que deseja devolver: "))

    encontrado = False

    for livro in biblioteca:
        if livro['id'] == id_devolucao:
            encontrado = True
            if livro["situação"] == "Emprestado":
                livro["situação"] = "Disponível"
                print(f"O livro '{livro['titulo']}' foi devolvido com sucesso.")
                salvar_livros(biblioteca)
        else:
            print(f"O livro '{livro['titulo']}' já está disponivel na biblioteca")
        break

    if not encontrado:
        print("Livro não encontrado na biblioteca.")

     
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

#função de buscar_livros que permite encontrar um livro pelo id
def buscar_livros(biblioteca):
    try:
        id_busca = int(input("Digite o id do livro desejado: ")) #pedindo ao ussuario o id desejado
    except ValueError:
        print("ID inválido! Digite apenas números.")
        return

    encontrado = False #flag usada para saber se o livro foi encontrado ou não

    for livro in biblioteca:
        if livro ['id'] == id_busca:
                print(livro)
                encontrado = True
                break

    if not encontrado:
        print("Não existe na biblioteca")
        