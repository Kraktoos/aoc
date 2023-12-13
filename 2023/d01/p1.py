input = open("input.txt", "r").read().strip().splitlines()
sum = 0

for line in input:
  number = 0
  for i in range(0, len(line), 1):
    if line[i].isdigit():
      number = int(line[i]) * 10
      break

  for i in range(len(line) - 1, -1, -1):
    if line[i].isdigit():
      number += int(line[i])
      break

  sum += number

print(sum)