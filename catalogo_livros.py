listaLivros = [
    {"id": "1", "titulo": "O Hobbit", "autor": "J.R.R. Tolkien", "descricao": "descrição livro 1.....", "preco": 49.90},
    {"id": "2", "titulo": "Dom Casmurro", "autor": "Machado de Assis", "descricao": "descrição livro 2.....", "preco": 39.90},
    {"id": "3", "titulo": "1984", "autor": "George Orwell", "descricao": "descrição livro 3.....", "preco": 59.90},
    {"id": "4", "titulo": "A Menina que Roubava Livros", "autor": "Markus Zusak", "descricao": "descrição livro 4.....", "preco": 44.90},
    {"id": "5", "titulo": "O Pequeno Príncipe", "autor": "Antoine de Saint-Exupéry", "descricao": "descrição livro 5.....", "preco": 29.90},
]

def exibir_catalogo(lista_livros):
    print("\nCatálogo de livros: ")
    print("--------------------------------------")
    for livro in lista_livros:
        print(f"ID: {livro['id']}")
        print(f"Titulo: {livro['titulo']}")
        print(f"Autor: {livro['autor']}")
        print(f"Descrição: {livro['descricao']}")
        print(f"Preco: {livro['preco']}")
        print("--------------------------------------")
        
exibir_catalogo(listaLivros)