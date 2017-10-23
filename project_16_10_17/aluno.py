class Aluno:
    def __init__(self,nome,curso,insonia):
        self.Nome = nome
        self.Curso = curso
        self.Insonia = insonia
    def estudar(self,horas):
        self.Insonia = self.Insonia + horas
    def dormir(self,horas):
        self.Insonia = self.Insonia - horas

nome = input("Aluno: ")
curso = input("Curso: ")
horas = int(input("Horas sem dormir: "))

aluno = Aluno(nome,curso,horas)
while aluno:
    horas = int(input("Tempo de estudo (em horas):\n"))
    aluno.estudar(horas)
    print("Tempo sem dormir:",str(aluno.Insonia))
    horas = int(input("Tempo dormindo (em horas):\n"))
    aluno.dormir(horas)
    print("Tempo sem dormir:",str(aluno.Insonia))
    if aluno.Insonia <= 0:
        print(aluno.Nome,"está dormindo. VAZA PENTELHO!")
        exit()