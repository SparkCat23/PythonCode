# Exercícios by Nick Parlante (CodingBat)

# I. sem_pontas
# seja uma string s de pelo menos dois caracteres
# retorna uma string sem o primeiro e último caracter
# sem_pontas('Hello') -> 'ell'
# sem_pontas('python') -> 'ytho'
# sem_pontas('coding') -> 'odin'
def sem_pontas(s):
  l = len(s)
  return s[1:l-1]


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
  print ('Sem Pontas')
  teste(sem_pontas('Hello'), 'ell')
  teste(sem_pontas('Python'), 'ytho')
  teste(sem_pontas('coding'), 'odin')
  teste(sem_pontas('code'), 'od')
  teste(sem_pontas('ab'), '')
  teste(sem_pontas('Chocolate!'), 'hocolate')
  teste(sem_pontas('kitten'), 'itte')
  teste(sem_pontas('woohoo'), 'ooho')

if __name__ == '__main__':
  main()
