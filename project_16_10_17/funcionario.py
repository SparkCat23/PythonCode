class Funcionario:
    nome = ""
    salario = None

    def __init__(self,n,s):
        self.nome = n
        self.salario = s
    
    def aumentarSalario(self,p):
        self.salario = self.salario + (self.salario * (p/100))
        return self.salario

nome = input("Digite o nome do funcionário:\n")
sal = float(input("Insira o salário:\n"))
F = Funcionario(nome,sal)
P = int(input("Percentual de aumento:\n"))
print("Novo Salário =",F.aumentarSalario(P))