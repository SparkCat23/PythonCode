# Exercícios by Nick Parlante (CodingBat)

# C. array_count9
# conta quantas vezes aparece o 9 numa lista nums
def array_count9(nums):
  n=0
  for x in nums:
    n=nums.count(9)

  return n


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
  print ('Array count 9')
  teste(array_count9([1, 99, 9]), 1)
  teste(array_count9([1, 9, 9]), 2)
  teste(array_count9([1, 9, 9, 3, 9]), 3)
  teste(array_count9([1, 2, 3]), 0)
  teste(array_count9([]), 0)
  teste(array_count9([4, 2, 4, 3, 1]), 0)
  teste(array_count9([9, 2, 99, 3, 1]), 1)

if __name__ == '__main__':
  main()
