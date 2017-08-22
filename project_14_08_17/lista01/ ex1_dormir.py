# Exercícios by Nick Parlante (CodingBat)

# A. dormir
# dia_semana é True para dias na semana
# feriado é True nos feriados
# você pode ficar dormindo quando é feriado ou não é dia semana
# retorne True ou False conforme você vá dormir ou não
def dormir(dia_semana, feriado):
  if feriado==True or dia_semana==False:
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
  print ('Oba! Hoje vou ficar dormindo!')
  teste(dormir(False, False), True)
  teste(dormir(True, False), False)
  teste(dormir(False, True), True)
  teste(dormir(True, True), True)


if __name__ == '__main__':
  main()
