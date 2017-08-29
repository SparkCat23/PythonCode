dic_vazio = {}
alunos = {11111:"NPC1",22222:"NPC2"}
aluno = {'nome':'NPC1','idade':'13'}

print(dic_vazio)
print(alunos[11111],alunos[22222])
print(aluno['idade'])

alunos[22222] = 'NPC3'

print(alunos[11111],alunos[22222])

alunos[33333] = 'NPC4'

print(alunos[11111],alunos[22222],alunos[33333])
print(len(alunos))

del alunos[11111]

print(alunos)

n=11111
ecziste = n in alunos
if not (ecziste) :
    print(str(n),'faleçeu!')

chaves = alunos.keys()
print(chaves)
valor = alunos.values()
print(valor)
itens = alunos.items()
print(itens)

print(11111,alunos.get(11111,'non ecziste'))

alunos.clear()
print(alunos)

alunos = {11111:"NPC1",22222:"NPC2",33333:"NPC3",44444:"NPC4"}

for key in alunos:
    print(alunos[key])
for key,value in alunos.items():
    print(key,':',value)

agenda = {
    'NPC1':{
        'telefone':['5555-5555','4444-4444'],
        'email':'npc1@gmail.com'
        },
    'NPC2':{
        'telefone':'1235-1235',
        'email':'npc2@gmail.com'},
    'NPC3':{
        'telefone':'9999-9999',
        'email':'npc3@gmail.com'}
}
print(agenda)