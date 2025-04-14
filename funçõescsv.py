#Importa o módulo CSv para leitura e escrita em arquivos.csv
import csv

ARQUIVO_CSV = "biblioteca.csv" #nome do  arquivo, váriavel fixa, ou seja uma constante

#função carregar livros do arquivo  csv e retornar como uma lista de dicionario
def carregar_livros():
    biblioteca = [] #inicaliza a lista que armazena os livros carregados

    try:
        #abre os arquivos csv para leitura
        with open(ARQUIVO_CSV, newline='', encoding='utf-8') as arquivo_livros:
             leitor_csv = csv.DictReader(arquivo_livros)
             for livros_csv in leitor_csv:
                 #converte os arquivos do csv para o formato correto e armazena em um novo dicionario
                 livro = {
                     "id": int(livros_csv["id"]), #converte o valor para inteiro
                     "titulo": livros_csv["titulo"],
                     "autores": livros_csv["autores"],
                     "editora": livros_csv["editora"],
                     "ano": int(livros_csv["ano"]), # converte o valor para inteiro
                     "situação": livros_csv["situação"]
                 }
                 biblioteca.append(livro) #adiciona o livro formatado a lista principal
    except FileNotFoundError:
        #se o arquivo não for encontrado, ele irá informar e retornar a biblioteca vazia
        print("Arquivo CSV não foi encontrado. a biblioteca irá iniciar vazia.")
    return biblioteca #retorna a lista de livros carregados

#função salvar a lista de livros no arquivo csv, sobrescrevendo o conteudo anterior
def salvar_livros(biblioteca):
    #abre o arquivo csv no modo de escrita 
    with open(ARQUIVO_CSV, mode='w', newline='', encoding='utf-8') as arquivo_livros:
        #define os nomes da colunas que devem ser os mesmos nomes que os nomes das chaves dos dicionarios
        campos_biblioteca = ["id", "titulo", "autores", "editora", "ano", "situação"]
        registro_biblioteca = csv.DictWriter(arquivo_livros, fieldnames=campos_biblioteca)
        registro_biblioteca.writeheader() #escreve a primeira linha com os nomes das coluna

        #escreve cada livro da lista como uma linha do arquivo
        for livro in biblioteca:
            registro_biblioteca.writerow(livro) #salva cada dicionario como uma linha do csv