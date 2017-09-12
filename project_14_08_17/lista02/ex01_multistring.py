# Exercícios by Nick Parlante (CodingBat)

# A. multstring
# seja uma string s e um inteiro positivo n
# retorna uma string com n cópias da string original
# multstring('Hi', 2) -> 'HiHi'
def multstring(s, n):
  s2=''
  for x in range(0,n):
    s2=s2+s
  return s2

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
  print ('Multstring')
  teste(multstring('Hi', 2), 'HiHi')
  teste(multstring('Hi', 3), 'HiHiHi')
  teste(multstring('Hi', 1), 'Hi')
  teste(multstring('Hi', 0), '')
  teste(multstring('Hi', 5), 'HiHiHiHiHi')
  teste(multstring('Oh Boy!', 2), 'Oh Boy!Oh Boy!')
  teste(multstring('x', 4), 'xxxx')
  teste(multstring('', 4), '')
  teste(multstring('code', 2), 'codecode')
  teste(multstring('code', 3), 'codecodecode')

if __name__ == '__main__':
  main()
