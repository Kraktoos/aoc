import re

input = open("input.txt", "r").read().strip().splitlines()
sum = 0
w, h = len(input), len(input[0])
gears = dict()

def adjacent_gear(x, y):
  for i in range(3):
    for j in range(3):
      try:
        if (input[x+i-1][y+j-1] == "*"):
          return str(x+i-1) + ":" + str(y+j-1)
      except:
        pass
  return False

for i, line in enumerate(input):
  last_was_digit = False
  line_parts = re.findall(r'\d+', line)
  crr_line_part = -1
  for j, curr in enumerate(line):
    if (input[i][j].isdigit()):
      if not last_was_digit and adjacent_gear(i, j) != False and ((adjacent_gear(i, j) in gears) or (adjacent_gear(i, j) not in gears)):
        crr_line_part += 1
        if adjacent_gear(i, j) not in gears:
          gears[adjacent_gear(i, j)] = line_parts[crr_line_part]
        else:
          gears[adjacent_gear(i, j)] += "/" + line_parts[crr_line_part]
        last_was_digit = True
      elif not last_was_digit and not adjacent_gear(i, j):
        try:
          if not input[i][j+1].isdigit():
            crr_line_part += 1
            last_was_digit = True
        except:
          pass
    else:
      last_was_digit = False

for key in gears:
  crr_gear = gears[key].split("/")
  if len(crr_gear) == 2:
    sum += int(crr_gear[0]) * int(crr_gear[1])

print(sum)