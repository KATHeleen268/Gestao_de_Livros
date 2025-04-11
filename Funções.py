#importando a função salvar_livros usada sempre que um dado é alterado na biblioteca salvando assim no csv
from funçõescsv import salvar_livros

#ordem id, titulo, autores, editora, ano, situação

#função de inserir livros que recebe os dados do usario e depois adicona e salva na biblioteca
def inserir_livros(biblioteca):
    id = int(input("Digite o código do livro: ")) #pede o id ao usuario e o recebe como inteiro 
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
        titulo_remover = input("Digite o titulo do livro que você deseja remover: ") #pede o titulo ao usuario par poder comparar e imprimir

    #quando o livro for enoocntrado irá remove-lo da lista e salvar no csv
        for livro in biblioteca:
            if livro["titulo"] == titulo_remover:
                biblioteca.remove(livro)
                salvar_livros(biblioteca)
                print(f"Livro com titulo {titulo_remover} removido com sucesso!")
                return
            #caso não encontre avisa que o livro não existe
        print(f"Nenhum livro com o titulo {titulo_remover} foi encontrado.")


#função que checa a situação do livro
def situacao_livro(biblioteca):
    titulo_situacao = input("Digite o titulo do livro que deseja ver a situação: ").strip().lower() #irá pedir o valor ao usuario e assim os metodos stip que converte tudo para mnusculas

    encontrado = False #flag que auxilia no resultado da busca

    for livro in biblioteca:
        if titulo_situacao in livro["titulo"].strip().lower(): #compara o titulo que o usuario digitou com o que está na biblioteca se for existente irá mostrar sua situação "Disponível" ou "Emprestado"
            print(f"O livro {livro['titulo']} está {livro['situação']}") 
            encontrado = True
            break
             
             #caso não encontre essa mensagem será exibida
    if not encontrado: 
        print("Livro não existe na biblioteca.")

#função de alugar livros ou seja troca a situação de disponivel para emprestado, caso não esteja disponivel
def alugar_livros(biblioteca):
    id_aluguel = int(input("Digite o id do livro que deseja alugar: ")) #pede o id do livro que o usuario deseja alugar 
    
    encontrado = False

# irá procurar o livro e caso encontre só permite alugar o livro se estiver disponivel 
    for livro in biblioteca:
        if livro['id'] == id_aluguel:
            print(f"O livro '{livro['titulo']}' (ID : {livro['id']}) foi encontrado")
            encontrado = True
            if livro["situação"] == "Disponível": #se estiver disponivel, fica emprestado
                livro["situação"] = "Emprestado"
                salvar_livros(biblioteca)
                print(f"O livro '{livro['titulo']}' foi emprestado com sucesso!")
            else:
                print(f"O livro '{livro['titulo']}' já está emprestado.") #caso esteja emprestado já, ele informa
            break
    if not encontrado:
        print("O livro desejado não foi encontrado.")

#função de devolução de livros devolve um livro, mudando sua situação de "Emprestado" para "Disponível"
def devolver_livros(biblioteca):
    id_devolucao = int(input("Digite o ID do livro que deseja devolver: ")) #pede o id do livro desejado ao usuario

    encontrado = False #flag

    for livro in biblioteca:
        if livro['id'] == id_devolucao:
            encontrado = True
            if livro["situação"] == "Emprestado": #se estiver como emprestado será mudado para emprestado
                livro["situação"] = "Disponível"
                print(f"O livro '{livro['titulo']}' foi devolvido com sucesso.")
                salvar_livros(biblioteca) #chama a função de salvar livro 

        else:
            print(f"O livro '{livro['titulo']}' já está disponivel na biblioteca")
        break

    if not encontrado:
        print("Livro não encontrado na biblioteca.")

     
#função de listar os livros de formas geral e especificas
def listar_livros(biblioteca):
    while True: #loop do submenu que só será encerrado quando o usuário escolher a opção de voltar ao menu inicial
        print("1. Listar todos os livros")
        print("2. Listar apenas os livros disponíveis")
        print("3. Listar apenas os livros emprestados")
        print("4. Listar por editora")
        print("5. Listar por ano")
        print("6. Voltar ao menu principal")
        
        opcao1 = input("Qual a listagem que deseja? ") #o sistema pede ao usuario para digitar qual opcao de listagem ele deseja que seja executada
        
        if opcao1 == "1": #listagem geral de todos os livros da biblioteca
            for livro in biblioteca:
                print(livro)
        elif opcao1 == "2": #lista os livros disponiveis
            for livro in biblioteca:
                if livro['situação'] == "Disponível":
                    print(livro)
        elif opcao1 == "3": #lista os livros emprestados
            for livro in biblioteca:
                if livro["situação"] == "Emprestado": 
                    print(livro)
        elif opcao1 == "4": #lista os livros por nome de editora
            editora = input("Digite o nome da editora: ").strip().lower()
            for livro in biblioteca:
                if livro["editora"].strip().lower() == editora:
                    print(livro)
        elif opcao1 == "5": #lista os livros por ano 
            ano = int(input("Digite o ano que deseja: "))
            for livro in biblioteca:
                if livro["ano"] == ano:
                    print(livro)
        elif opcao1 == "6": #retorna ao menu principal
            print("retornando ao menu principal")
            break
        else:
            print("Opção inválida. Tente novamente com um valor válido.")

#função de buscar_livros que permite encontrar um livro pelo id
def buscar_livros(biblioteca):
    try: 
        id_busca = int(input("Digite o id do livro desejado: ")) #pedindo ao usuario o id desejado 
    except ValueError:
        print("ID inválido! Digite apenas números.")
        return

    encontrado = False #flag usada para saber se o livro foi encontrado ou não

    for livro in biblioteca: # se encontrar o livro irá exibir se não irá informar que não existe
        if livro ['id'] == id_busca:
                print(livro)
                encontrado = True
                break

    if not encontrado:
        print("Não existe na biblioteca")
        