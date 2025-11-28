carrinho = []
def adicionar_livro(carrinho):
    while True:
        nomeLivro = input("Digite o nome do livro para adicionar ao carrinho ou sair: ")
        if nomeLivro == 'sair':
            break
        
        carrinho.append(nomeLivro)
        print(f"📘 Livro '{nomeLivro}' adicionado ao carrinho com sucesso!" )
    
    print(f"Seu carrinho {carrinho}")
        
adicionar_livro(carrinho)