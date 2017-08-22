# Exercícios by Nick Parlante (CodingBat)

# B. string_splosion
# string_splosion('Code') -> 'CCoCodCode'
# string_splosion('abc') -> 'aababc'
# string_splosion('ab') -> 'aab'
def string_splosion(s):
  n = len(s)
  s2 = ''
  for x in range(0,n+1):
    s2 = s2+s[0:x]
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
  print ('String Explosion')
  teste(string_splosion('Code'), 'CCoCodCode')
  teste(string_splosion('abc'), 'aababc')
  teste(string_splosion('ab'), 'aab')
  teste(string_splosion('x'), 'x')
  teste(string_splosion('fade'), 'ffafadfade')
  teste(string_splosion('There'), 'TThTheTherThere')
  teste(string_splosion('Kitten'), 'KKiKitKittKitteKitten')
  teste(string_splosion('Bye'), 'BByBye')
  teste(string_splosion('Good'), 'GGoGooGood')
  teste(string_splosion('Bad'), 'BBaBad')

if __name__ == '__main__':
  main()
