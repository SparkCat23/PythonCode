# Exercícios by Nick Parlante (CodingBat)

# E. papagaio
# temos um papagaio que fala alto
# hora é um parâmetro entre 0 e 23
# temos problemas se o papagaio estiver falando
# antes da 7 ou depois das 20
def papagaio(falando, hora):
  if falando==True and hora<7:
    return True
  elif falando==True and hora>20:
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
  print ('Papagaio')
  teste(papagaio(True, 6), True)
  teste(papagaio(True, 7), False)
  teste(papagaio(False, 6), False)
  teste(papagaio(True, 21), True)
  teste(papagaio(False, 21), False)
  teste(papagaio(True, 23), True)
  teste(papagaio(True, 20), False)


if __name__ == '__main__':
  main()
