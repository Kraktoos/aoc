import copy

matrix = [[x for x in line] for line in open("input.txt", "r").read().strip().splitlines()]

def get_right_turn(going):
  if going[0] == -1:
    return (0, 1)
  elif going[0] == 1:
    return (0, -1)
  elif going[1] == -1:
    return (-1, 0)
  elif going[1] == 1:
    return (1, 0)

n_times_until_probably_loop = len(matrix) ** 3

def will_finish(curr_matrix, starting_pos, starting_going):
  curr_matrix = copy.deepcopy(curr_matrix)
  going = starting_going

  count_times = 0
  while True:
    curr_matrix[starting_pos[0]][starting_pos[1]] = "X"
    count_times += 1

    if starting_pos[0] + going[0] <= -1 or starting_pos[0] + going[0] >= len(curr_matrix[0]) or starting_pos[1] + going[1] <= -1 or starting_pos[1] + going[1] >= len(curr_matrix):
      break

    if curr_matrix[starting_pos[0] + going[0]][starting_pos[1] + going[1]] == "#":
      going = get_right_turn(going)

    starting_pos = (starting_pos[0] + going[0], starting_pos[1] + going[1])

    if count_times >= n_times_until_probably_loop:
      return False

  return True

current_pos = (0, 0)
for i in range(len(matrix)):
  for j in range(len(matrix[0])):
    if matrix[i][j] == "^":
      current_pos = (i, j)
      break

going = (-1, 0)
total = 0
for i in range(len(matrix)):
  for j in range(len(matrix[0])):
    if matrix[i][j] == ".":
      matrix[i][j] = "#"
      if not will_finish(matrix, current_pos, going):
        total += 1
      matrix[i][j] = "."
  print(i)

print(total)