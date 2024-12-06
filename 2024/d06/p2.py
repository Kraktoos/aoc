from copy import deepcopy

matrix = [[x for x in line] for line in open("input.txt", "r").read().strip().splitlines()]
original_matrix = deepcopy(matrix)

current_pos = (0, 0)
for i in range(len(matrix)):
  for j in range(len(matrix[0])):
    if matrix[i][j] == "^":
      matrix[i][j] = "u"
      current_pos = (i, j)
      break

going = (-1, 0)

while True:
  match going:
    case (-1, 0):
      matrix[current_pos[0]][current_pos[1]] = "u"
    case (1, 0):
      matrix[current_pos[0]][current_pos[1]] = "d"
    case (0, -1):
      matrix[current_pos[0]][current_pos[1]] = "l"
    case (0, 1):
      matrix[current_pos[0]][current_pos[1]] = "r"

  if current_pos[0] + going[0] <= -1 or current_pos[0] + going[0] >= len(matrix[0]) or current_pos[1] + going[1] <= -1 or current_pos[1] + going[1] >= len(matrix):
    break

  if matrix[current_pos[0] + going[0]][current_pos[1] + going[1]] == "#":
    if going[0] == -1:
      going = (0, 1)
    elif going[0] == 1:
      going = (0, -1)
    elif going[1] == -1:
      going = (-1, 0)
    elif going[1] == 1:
      going = (1, 0)
  

  current_pos = (current_pos[0] + going[0], current_pos[1] + going[1])

def can_solve(new_matrix, cpos, cgoing):
  visited = set()

  while True:
    next_row, next_col = cpos[0] + cgoing[0], cpos[1] + cgoing[1]

    if next_row < 0 or next_row >= len(matrix) or next_col < 0 or next_col >= len(matrix[0]):
      return True
    
    state = (cpos, cgoing)
    if state in visited:
      return False
    visited.add(state)

    if new_matrix[next_row][next_col] == "#":
      if cgoing[0] == -1:
        cgoing = (0, 1)
      elif cgoing[0] == 1:
        cgoing = (0, -1)
      elif cgoing[1] == -1:
        cgoing = (-1, 0)
      elif cgoing[1] == 1:
        cgoing = (1, 0)
    else:
      cpos = (next_row, next_col)

current_pos = (0, 0)
for i in range(len(original_matrix)):
  for j in range(len(original_matrix[0])):
    if original_matrix[i][j] == "^":
      original_matrix[i][j] = "u"
      current_pos = (i, j)
      break
going = (-1, 0)
solved_matrix = deepcopy(matrix)

total = 0
for i in range(len(original_matrix)):
  for j in range(len(original_matrix[0])):
    if solved_matrix[i][j] in ["u", "d", "l", "r"] and original_matrix[i][j] == ".":
      original_matrix[i][j] = "#"
      if not can_solve(original_matrix, current_pos, going):
        total += 1
      original_matrix[i][j] = "."

print(total)