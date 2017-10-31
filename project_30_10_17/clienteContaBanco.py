class Cliente():
    def __init__(self,nome,tel):
        self.__nome = nome
        self.__tel = tel

class Conta():
    def __init__(self,clientes,numero,saldo):
        self.__clientes = clientes
        self.__numero = numero
        self.__saldo = saldo
        self.operacoes = []

    def resumo(self):
        print('Conta: {} - Saldo: {}'.format(self.__numero,self.__saldo))

    def saque(self,valor):
        if self.__saldo >= valor:
            self.__saldo -= valor
            self.operacoes.append(('Saque -',valor))

    def deposito(self,valor):
        self.__saldo += valor
        self.operacoes.append(('Depósito -',valor))

    def extrato(self):
        print('Extrato da conta: ',self.__numero)
        for o in self.operacoes:
            print(o[0], o[1])
        print('Saldo atual =', self.__saldo)

    def __repr__(self):
        return 'Conta: '+self.__numero+'--'+self.__saldo+';'

class Banco():
    def __init__(self,nome):
        self.nome = nome
        self.clientes = []
        self.contas = []

    def abreConta(self,conta):
        self.contas.append(conta)

    def listaContas(self):
        return self.contas


#Criação de objetos Cliente
johnson = Cliente('Johnson','99999-9999')
robson = Cliente('Robson','88888-8888')

# objetos Conta criados
c1 = Conta([johnson,robson],123456,5000)
c1.resumo()
c1.deposito(3000)
c1.saque(4000)
c1.resumo()
c1.extrato()

#objeto Banco
b1 = Banco('banco Impacta')
b1.abreConta(123456)