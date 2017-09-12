class Account:
    def __init__(self,clients,number,balance):
        self.clients = list<clients>
        self.number = number
        self.balance = balance

    def resume(self):
        print('CC Número: {} | Saldo: {:.2f}'.format(self.number,self.balance))

    def saque(self, value):
        if self.balance >= value:
            self.balance -= value

    def deposito(self,value):
        self.balance += value

    def operacoes(self):
