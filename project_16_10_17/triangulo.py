class triangulo:
    ladoA = None
    ladoB = None
    ladoC = None

    def __init__(self,a,b,c):
        A = False
        B = False
        C = False
        if abs(b-c) < a and a < (b+c):
            A = True
        if abs(a-c) < b and b < (a+c):
            B = True
        if abs(a-b) < c and c < (a+b):
            C = True
        if A and B and C:
            self.ladoA = a
            self.ladoB = b
            self.ladoC = c
        else:
            print("Triângulo não pôde ser formado")
            exit()

    def calcularPerimetro(self,A,B,C):
        a = A
        b = B
        c = C
        return (a+b+c)

    def getLadoMaior(self,A,B,C):
        maior = []
        maior.append(A)
        maior.append(B)
        maior.append(C)
        maior.sort
        return maior[2]

print("Criação de triângulo. Informe os lados")
a = int(input("Lado A:\n"))
b = int(input("Lado B:\n"))
c = int(input("Lado C:\n"))

TRI = triangulo(a,b,c)
PER = TRI.calcularPerimetro(TRI.ladoA,TRI.ladoB,TRI.ladoC)
MAIOR = TRI.getLadoMaior(TRI.ladoA,TRI.ladoB,TRI.ladoC)

print("Perímetro:",PER,"\n")
print("Lado Maior:",MAIOR,"\n")