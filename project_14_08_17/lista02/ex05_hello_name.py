# Exercícios by Nick Parlante (CodingBat)

# E. hello_name
# seja uma string name
# hello_name('Bob') -> 'Hello Bob!'
# hello_name('Alice') -> 'Hello Alice!'
# hello_name('X') -> 'Hello X!'
def hello_name(name):
  return 'Hello '+name+'!'


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
  print ('Hello Name')
  teste(hello_name('Bob'), 'Hello Bob!')
  teste(hello_name('Alice'), 'Hello Alice!')
  teste(hello_name('X'), 'Hello X!')
  teste(hello_name('Hello'), 'Hello Hello!')

if __name__ == '__main__':
  main()
