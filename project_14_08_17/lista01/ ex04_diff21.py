# Exercícios by Nick Parlante (CodingBat)

# D. diff21
# dado um inteiro n retorna a diferença absoluta entre n e 21
# porém se o número for maior que 21 retorna dobro da diferença absoluta
# diff21(19) -> 2
# diff21(25) -> 8
# dica: abs(x) retorna o valor absoluto de x
def diff21(n):
  if n > 21:
    return (abs(21-n)*2)
  else:
    return (21-n)


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
  print ('Diff21')
  teste(diff21(19), 2)
  teste(diff21(10), 11)
  teste(diff21(21), 0)
  teste(diff21(22), 2)
  teste(diff21(25), 8)
  teste(diff21(30), 18)


if __name__ == '__main__':
  main()
