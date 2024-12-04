import re

matrix = open("input.txt").read().strip().splitlines()

def in_matrix(i, j):
  if not (0 <= i < len(matrix)) or not (0 <= j < len(matrix[0])):
    return False
  return True

def check_can(letter, i, j):
  if letter != matrix[i][j]:
    return False
  
  operacoes_principal = (
    lambda x, y: (x - 1, y + 1),
    lambda x, y: (x + 1, y - 1)
  )

  operacoes_secundaria = (
    lambda x, y: (x + 1, y + 1),
    lambda x, y: (x - 1, y - 1)
  )

  to_use_principal = ["M", "S"]
  for operacao in operacoes_principal:
    if in_matrix(*operacao(i, j)):
      result = operacao(i, j)
      char = matrix[result[0]][result[1]]
      if char in to_use_principal:
        to_use_principal.remove(char)
  to_use_secundaria = ["M", "S"]
  for operacao in operacoes_secundaria:
    if in_matrix(*operacao(i, j)):
      result = operacao(i, j)
      char = matrix[result[0]][result[1]]
      if char in to_use_secundaria:
        to_use_secundaria.remove(char)

  if to_use_principal == to_use_secundaria == []:
    return True
  return False

counter = 0
for i in range(len(matrix)):
  for j in range(len(matrix[0])):
    if check_can("A", i, j):
      counter += 1

print(counter)