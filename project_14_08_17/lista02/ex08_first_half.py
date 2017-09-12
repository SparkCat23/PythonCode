# Exercícios by Nick Parlante (CodingBat)

# H. first_half
# seja uma string s
# retorna a primeira metade da string
# first_half('WooHoo') -> 'Woo'
# first_half('HelloThere') -> 'Hello'
# first_half('abcdef') -> 'abc'
def first_half(s):
  l=len(s)
  return s[:(l//2)]


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
  print ('First Half')
  teste(first_half('WooHoo'), 'Woo')
  teste(first_half('HelloThere'), 'Hello')
  teste(first_half('abcdef'), 'abc')
  teste(first_half('ab'), 'a')
  teste(first_half(''), '')
  teste(first_half('0123456789'), '01234')
  teste(first_half('kitten'), 'kit')

if __name__ == '__main__':
  main()
