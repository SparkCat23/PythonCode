# Gustavo Zaik - 1700591
# Luka Gabriel - 1700709
# Jhonatan Rafael - 1700646

def incluirNovoNome(nome,tel):
    Ag[nome] = tel
    return Ag

def incluirTelefone(nome,tel):
    if nome in Ag.keys():
        Ag[nome] = Ag[nome]+','+tel
    else:
        opt = input('Nome não encontrado. Desejas incluir?\n')
        if opt == 'sim':
            nome = input('Digite seu nome: ')
            tel = input('Digite seus telefones(separar por vírgula): ')
            incluirNovoNome(nome,tel)
        else:
            return Ag
    return Ag

def excluirTelefone(nome,tel):
    if nome in Ag:
        tell = Ag[nome]
        lista = tell.split(',')
        if len(lista) == 1:
            del Ag[nome]
        else:
            lista.pop(lista.index(tel))
            tell2 = lista[0]
            for x in range(1,len(lista)):
                tell2 = tell2+','+lista[x]
            Ag[nome] = tell2
    else:
        print('Nome não encontrado')

def excluirNome(nome):
    if nome not in Ag.keys():
        print('Nome não encontrado')
    else:
        del Ag[nome]

def consultarNome(nome):
    if nome in Ag:
        print(Ag[nome])
    else:
        print('Nome não encontrado')

Ag = {}
while True:
    opc = int(input('''
Escolha uma opção:

   1 - Incluir Novo Nome
   2 - Excluir Número
   3 - Consultar Nome
   4 - Incluir Número
   5 - Excluir Nome
   6 - Sair

: '''))
    if opc == 5:
        nome = input('Digite seu nome: ')
        excluirNome(nome)
    elif opc == 1:
        nome = input('Digite seu nome: ')
        tel = input('Digite seus telefones(separar por vírgula): ')
        incluirNovoNome(nome,tel)
    elif opc == 2:
        nome = input('Digite seu nome: ')
        tel = input('Digite o telefone: ')
        excluirTelefone(nome,tel)
    elif opc == 3:
        nome = input('Digite seu nome: ')
        consultarNome(nome)
    elif opc == 4:
        nome = input('Digite seu nome: ')
        tel = input('Digite o telefone: ')
        incluirTelefone(nome,tel)
    else:
        break