# Exercícios by Nick Parlante (CodingBat)

# G. extra_end
# seja um string s com no mínimo duas letras
# retorna três vezes as duas últimas letras
# extra_end('Hello'), 'lololo'
# extra_end('ab'), 'ababab'
# extra_end('Hi'), 'HiHiHi'  
def extra_end(s):
  l=len(s)
  s2=''
  if l >= 2:
    s2=s[l-2:]+s[l-2:]+s[l-2:]
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
  print ('Extra End')
  teste(extra_end('Hello'), 'lololo')
  teste(extra_end('ab'), 'ababab')
  teste(extra_end('Hi'), 'HiHiHi')
  teste(extra_end('Candy'), 'dydydy')
  teste(extra_end('Code'), 'dedede')

if __name__ == '__main__':
  main()
