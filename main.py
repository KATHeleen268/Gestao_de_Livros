from menu import menu

def main():
     biblioteca = [
       {"id": 1, "titulo": "1984", "autores": "George Orwell", "editora": "Grupo Companhia das Letras", "ano": 2009, "situação": "Emprestado"},
       {"id": 2, "titulo": "O clube do trico", "autores": "Kate Jacobs", "editora": "Amarilys Editora", "ano": 2010, "situação": "Disponível"}
]

     menu(biblioteca)   

if __name__ == "__main__":
     main()