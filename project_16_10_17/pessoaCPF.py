class Pessoa:
    # atrib
    # utos e métodos Private são declarados com dois underlines na frente
    __cpf = None

    def __init__(self):
        ...
    
    def getCPF(self):
        return self.__cpf

    def validarCPF(self,cpf):
        if len(cpf) == 11:
            return True
        else:
            return False

    def setCPF(self,cpf):
        if self.validarCPF(cpf):
            self.__cpf = cpf
        else:
            print("CPF inválido")
    
    

p = Pessoa()
p.setCPF('64')

print(p.getCPF)