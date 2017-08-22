# Exercícios by Nick Parlante (CodingBat)

# I. troca
# seja uma string s
# se s tiver tamanho <= 1 retorna ela mesma
# caso contrário troca a primeira e última letra
# troca('code') -> 'eodc'
# troca('a') -> 'a'
# troca('ab') -> 'ba'
def troca(s):
  n=len(s)
  if n<=1:
    return s
  else:
    s = s[n-1]+s[1:n-1]+s[0]
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
  print ('Troca letras')
  teste(troca('code'), 'eodc')	    
  teste(troca('a'), 'a')
  teste(troca('ab'), 'ba')
  teste(troca('abc'), 'cba')
  teste(troca(''), '')
  teste(troca('Chocolate'), 'ehocolatC')
  teste(troca('nythoP'), 'Python')
  teste(troca('hello'), 'oellh')


if __name__ == '__main__':
  main()
