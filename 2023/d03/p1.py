import re

input = open("input.txt", "r").read().strip().splitlines()
sum = 0
w, h = len(input), len(input[0])
adjacents = [[False for x in range(h)] for y in range(w)]

for i in range(w):
  for j in range(h):
    if (not input[i][j].isdigit() and input[i][j] != "."):
      for k in range(3):
        for l in range(3):
          if (i+k-1 != -1 and j+l-1 != -1):
            try:
              if (adjacents[i+k-1][j+l-1] == False):
                adjacents[i+k-1][j+l-1] = True
            except:
              pass

for i, line in enumerate(input):
  last_was_digit = False
  line_parts = re.findall(r'\d+', line)
  crr_line_part = -1
  for j, curr in enumerate(line):
    if (input[i][j].isdigit()):
      if not last_was_digit and adjacents[i][j]:
        crr_line_part += 1
        sum += int(line_parts[crr_line_part])
        last_was_digit = True
      elif not last_was_digit and not adjacents[i][j]:
        try:
          if not input[i][j+1].isdigit():
            crr_line_part += 1
            last_was_digit = True
        except:
          pass
    else:
      last_was_digit = False

print(sum)