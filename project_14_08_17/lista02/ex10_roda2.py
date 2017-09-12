# Exercícios by Nick Parlante (CodingBat)

# J. roda2
# rodar uma string s duas posições
# a string possui pelo menos 2 caracteres
# roda2('Hello') -> 'lloHe'
# roda2('Hi') -> 'Hi'
def roda2(s):
  l = len(s)
  if l >= 2:
    return s[2:]+s[:2]


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
  print ('Roda 2')
  teste(roda2('Hello'), 'lloHe')
  teste(roda2('python'), 'thonpy')
  teste(roda2('Hi'), 'Hi')
  teste(roda2('code'), 'deco')
  teste(roda2('cat'), 'tca')
  teste(roda2('12345'), '34512')
  teste(roda2('Chocolate'), 'ocolateCh')
  teste(roda2('bricks'), 'icksbr')

if __name__ == '__main__':
  main()
