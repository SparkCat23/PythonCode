# Exercícios by Nick Parlante (CodingBat)

# B. alunos_problema
# temos dois alunos a e b
# a_sorri e b_sorri indicam se a e b sorriem
# temos problemas quando ambos estão sorrindo ou ambos não estão sorrindo
# retorne True quando houver problemas
def alunos_problema(a_sorri, b_sorri):
  if a_sorri==b_sorri:
    return True
  else:
    return False


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
  print ('Alunos problema')
  teste(alunos_problema(True, True), True)
  teste(alunos_problema(False, False), True)
  teste(alunos_problema(True, False), False)
  teste(alunos_problema(False, True), False)


if __name__ == '__main__':
  main()
