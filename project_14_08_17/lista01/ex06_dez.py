# Exercícios by Nick Parlante (CodingBat)

# F. dez
# dados dois inteiros a e b
# retorna True se um dos dois é 10 ou a soma é 10
def dez(a, b):
  if a==10 or b==10 or (a+b)==10:
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
  print ('Dez')
  teste(dez(9, 10), True)
  teste(dez(9, 9), False)
  teste(dez(1, 9), True)
  teste(dez(10, 1), True)
  teste(dez(10, 10), True)
  teste(dez(8, 2), True)
  teste(dez(8, 3), False)
  teste(dez(10, 42), True)
  teste(dez(12, -2), True)


if __name__ == '__main__':
  main()
