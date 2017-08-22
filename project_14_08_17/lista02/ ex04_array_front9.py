# Exercícios by Nick Parlante (CodingBat)

# D. array_front9
# verifica se pelo menos um dos quatro primeiros é nove
# array_front9([1, 2, 9, 3, 4]) -> True
# array_front9([1, 2, 3, 4, 9]) -> False
# array_front9([1, 2, 3, 4, 5]) -> False
def array_front9(nums):
  l=len(nums)
  n=[]
  m=0
  if l > 4:
    for x in range(0,4):
      if nums[x]==9:
        return True
  elif l<=4:
    for x in range(0,l):
      if nums[x]==9:
        return True
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
  print ('Array front 9')
  teste(array_front9([1, 2, 9, 3, 4]), True)
  teste(array_front9([1, 2, 3, 4, 9]), False)
  teste(array_front9([1, 2, 3, 4, 5]), False)
  teste(array_front9([9, 2, 3]), True)
  teste(array_front9([1, 9, 9]), True)
  teste(array_front9([1, 2, 3]), False)
  teste(array_front9([1, 9]), True)
  teste(array_front9([5, 5]), False)
  teste(array_front9([2]), False)
  teste(array_front9([9]), True)
  teste(array_front9([]), False)
  teste(array_front9([3, 9, 2, 3, 3]), True)

if __name__ == '__main__':
  main()
