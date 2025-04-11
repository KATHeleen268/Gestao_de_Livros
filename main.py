from menu import menu
from funçõescsv import carregar_livros, salvar_livros
biblioteca = carregar_livros()

def main():
     biblioteca = [
       {"id": 1, "titulo": "1984", "autores": "George Orwell", "editora": "Grupo Companhia das Letras", "ano": 2009, "situação": "Emprestado"},
       {"id": 2, "titulo": "O clube do trico", "autores": "Kate Jacobs", "editora": "Amarilys Editora", "ano": 2010, "situação": "Disponível"}
]

     menu(biblioteca)
     salvar_livros(biblioteca)   

if __name__ == "__main__":
     main()