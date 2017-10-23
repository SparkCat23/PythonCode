class Livro:
    def __init__(self,n,a,p,preco):
        self.nome = n
        self.autor = a
        self.pages = p
        self.preco = preco

    def getPreco(self):
        preco = self.preco
        return preco

    def setPreco(self,preco):
        self.preco = preco

def main():
    livro = Livro("Lord of the Rings","Tolkien","534 páginas","R$134.00")
    print(livro.nome,"\n",livro.autor,"\n",livro.pages,"\n")
    print(livro.getPreco())
    novoPreco = input("Novo Preço:\n")
    livro.setPreco(novoPreco)
    print(livro.getPreco())

if __name__ == '__main__':
    main()