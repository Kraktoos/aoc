import re

matrix = open("input.txt").read().strip().splitlines()

temp = "XMAS"
WORD = [x for x in temp]

def check_can(word, i, j, fni, fnj):
  word = word.copy()
  if len(word) == 0:
    return True
  
  current_char = word.pop(0)

  if not (0 <= i < len(matrix)) or not (0 <= j < len(matrix[0])):
    return False

  if current_char != matrix[i][j]:
    return False
  
  if check_can(word, fni(i), fnj(j), fni, fnj):
    return True
  return False

counter = 0
for i in range(len(matrix)):
  for j in range(len(matrix[0])):
    for fn in [
      (lambda x: x, lambda x: x+1),
      (lambda x: x, lambda x: x-1),
      (lambda x: x+1, lambda x: x),
      (lambda x: x-1, lambda x: x),
      (lambda x: x-1, lambda x: x-1),
      (lambda x: x-1, lambda x: x+1),
      (lambda x: x+1, lambda x: x-1),
      (lambda x: x+1, lambda x: x+1),
    ]:
      if check_can(WORD, i, j, *fn):
        counter += 1

print(counter)