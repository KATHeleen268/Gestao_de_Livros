import csv

ARQUIVO_CSV = "biblioteca.csv" #nome do  arquivo, váriavel fixa, ou seja uma constante

#função carregar livros
def carregar_livros():
    biblioteca = []
    try:
        with open(ARQUIVO_CSV, newline='', encoding='utf-8') as arquivo_livros:
             leitor_csv = csv.DictReader(arquivo_livros)
             for livros_csv in leitor_csv:
                 livro = {
                     "id": int(livros_csv["id"]),
                     "titulo": livros_csv["titulo"],
                     "autores": livros_csv["autores"],
                     "editora": livros_csv["editora"],
                     "ano": int(livros_csv["ano"]),
                     "situação": livros_csv["situação"]
                 }
                 biblioteca.append(livro)
    except FileNotFoundError:
        print("Arquivo CSV não foi encontrado. a biblioteca irá iniciar vazia.")
    return biblioteca

#função salvar livros
def salvar_livros(biblioteca):
    with open(ARQUIVO_CSV, mode='w', newline='', encoding='utf-8') as arquivo_livros:
        campos_biblioteca = ["id", "titulo", "autores", "editora", "ano", "situação"]
        registro_biblioteca = csv.DictWriter(arquivo_livros, fieldnames=campos_biblioteca)
        registro_biblioteca.writeheader()
        for livro in biblioteca:
            registro_biblioteca.writerow(livro)