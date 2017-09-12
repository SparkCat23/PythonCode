from televisaoClass import Televisao

tv_sala = Televisao(1,6)
tv_sala.ligada = True
tv_sala.canal = 5

print('canal',tv_sala.canal)
canais = []
for x in range(tv_sala.cMin,tv_sala.cMax + 1):
    canais.append(x)

command = input('digite [+] para aumentar de canal e [-] para diminuir de canal. Selecione digitando um número. Digite [x] para desligar.')
while command != 'x':
    if command == '+':
        tv_sala.aumenta_canal()
    elif command == '-':
        tv_sala.diminui_canal()
    elif int(command) in canais:
        tv_sala.select_canal(int(command))
    else:
        print('Canal não encontrado')
    command = input('.')