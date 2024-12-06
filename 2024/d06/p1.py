matrix = [[x for x in line] for line in open("input.txt", "r").read().strip().splitlines()]

current_pos = (0, 0)
for i in range(len(matrix)):
  for j in range(len(matrix[0])):
    if matrix[i][j] == "^":
      current_pos = (i, j)
      break

going = (-1, 0)

while True:
  matrix[current_pos[0]][current_pos[1]] = "X"

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

xes = 0
for line in matrix:
  for char in line:
    if char == "X":
      xes += 1
print(xes)