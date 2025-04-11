#importa a função menu que controla o sistema principal da biblioteca
from menu import menu

#importa as funções carregar e salvar os dados do arquivo csv
from funçõescsv import carregar_livros, salvar_livros


def main():
    biblioteca = carregar_livros() #chama a função que carrega dados e armazena na variavel biblioteca
    menu(biblioteca) #chama a função menu e a biblioteca é o parametro
    salvar_livros(biblioteca) #salva os dados atualizados da biblioteca no arquivo csv

    """ biblioteca = [
       {"id": 1, "titulo": "1984", "autores": "George Orwell", "editora": "Grupo Companhia das Letras", "ano": 2009, "situação": "Emprestado"},
       {"id": 2, "titulo": "O clube do trico", "autores": "Kate Jacobs", "editora": "Amarilys Editora", "ano": 2010, "situação": "Disponível"}
] """ #estrutura de lista de dicionarios dos livros

#verfica se o arquivo está sendo executado diretamente e não sendo importado com módulo       
if __name__ == "__main__":
     main() #chama a função prinicpal ou seja o main