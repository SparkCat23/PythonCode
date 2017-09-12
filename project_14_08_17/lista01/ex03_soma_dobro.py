# Exercícios by Nick Parlante (CodingBat)

# C. soma_dobro
# dados dois números inteiros retorna sua soma
# porém se os números forem iguais retorna o dobro da soma
# soma_dobro(1, 2) -> 3
# soma_dobro(2, 2) -> 8
def soma_dobro(a, b):
  if a==b:
    return (a+b)*2
  else:
    return (a+b)


# Este é uma simples funcao teste() usado na main() para mostrar
# o que cada funcao implementada devolve vs. o que realmente 
# deve-se devolver.
def teste(obtido, esperado):
  if obtido == esperado:
    prefixo = ' Parabéns!'
  else:
    prefixo = ' Ainda não'
  print ('%s obtido: %s esperado: %s' % (prefixo, repr(obtido), repr(esperado)))

def main():
  print ('Soma dobro')
  teste(soma_dobro(1, 2), 3)
  teste(soma_dobro(3, 2), 5)
  teste(soma_dobro(2, 2), 8)
  teste(soma_dobro(-1, 0), -1)
  teste(soma_dobro(0, 0), 0)
  teste(soma_dobro(0, 1), 1)


if __name__ == '__main__':
  main()
