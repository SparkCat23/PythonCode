# Exercícios by Nick Parlante (CodingBat)

# F. make_tags
# make_tags('i', 'Yay'), '<i>Yay</i>'
# make_tags('i', 'Hello'), '<i>Hello</i>'
# make_tags('cite', 'Yay'), '<cite>Yay</cite>'
def make_tags(tab, word):
  return '<'+tab+'>'+word+'</'+tab+'>'


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
  print ('Make Tags')
  teste(make_tags('i', 'Yay'), '<i>Yay</i>')
  teste(make_tags('i', 'Hello'), '<i>Hello</i>')
  teste(make_tags('cite', 'Yay'), '<cite>Yay</cite>')
  teste(make_tags('address', 'here'), '<address>here</address>')
  teste(make_tags('body', 'Heart'), '<body>Heart</body>')
  teste(make_tags('i', 'i'), '<i>i</i>')
  teste(make_tags('i', ''), '<i></i>')

if __name__ == '__main__':
  main()
