class Pessoa:
    nome = None
    idade = None

    def __init__(self, nome="",idade=0):
        self.nome = nome
        self.idade = idade
    
class PessoaFisica(Pessoa):#class ClassName(SuperClass): permite acesso aos membros da superclasse
    #Construtor da classe pai é chamado através da classe filha
    def __init__(self,cpf,nome="",idade=0):
        Pessoa.__init__(self,nome,idade)
        self.cpf = cpf

class PessoaJuridica(Pessoa):
    def __init__(self, cnpj, nome="", idade=0):
        Pessoa.__init__(self,nome, idade)
        self.cnpj = cnpj

a = Pessoa()
p1 = PessoaFisica(a,"Paulo",44)
p1.cpf = "12345678901"
print(p1.cpf)