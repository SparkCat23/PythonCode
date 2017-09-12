# Exercícios by Nick Parlante (CodingBat)

# G. dista10
# seja um inteiro n
# retorna True se a diferença absoluta entre n e 100 ou n e 200
# for menor ou igual a 10
# dista10(93) -> True
# dista10(90) -> True
# dista10(89) -> False
def dista10(n):
  if abs(100-n)<=10:
    return True
  elif abs(200-n)<=10:
    return True
  else:
    return False


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
  print ('Dista 10')
  teste(dista10(93), True)
  teste(dista10(90), True)
  teste(dista10(89), False)
  teste(dista10(110), True)
  teste(dista10(111), False)
  teste(dista10(121), False)
  teste(dista10(0), False)
  teste(dista10(5), False)
  teste(dista10(191), True)
  teste(dista10(189), False)
  teste(dista10(190), True)
  teste(dista10(200), True)
  teste(dista10(210), True)
  teste(dista10(211), False)
  teste(dista10(290), False)


if __name__ == '__main__':
  main()
