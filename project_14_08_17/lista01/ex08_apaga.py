# Exercícios by Nick Parlante (CodingBat)

# H. apaga
# seja uma string s e um inteiro n
# retorna uma nova string sem a posição n
# apaga('kitten', 1) -> 'ktten'
# apaga('kitten', 4) -> 'kittn'
def apaga(s, n):
  s = s[:n]+s[n+1:]
  return s
  

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
  print ('Apaga')
  teste(apaga('kitten', 1), 'ktten')
  teste(apaga('kitten', 0), 'itten') 
  teste(apaga('kitten', 4), 'kittn')
  teste(apaga('Hi', 0), 'i')
  teste(apaga('Hi', 1), 'H')
  teste(apaga('code', 0), 'ode')
  teste(apaga('code', 1), 'cde')
  teste(apaga('code', 2), 'coe')
  teste(apaga('code', 3), 'cod')
  teste(apaga('chocolate', 8), 'chocolat')


if __name__ == '__main__':
  main()
