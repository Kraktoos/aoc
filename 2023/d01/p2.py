input = open("input.txt", "r").read().strip().splitlines()
sum = 0

digits = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

for line in input:
  number = 0
  break_flag = False
  for i in range(0, len(line), 1):
    if line[i].isdigit():
      number = int(line[i]) * 10
      break_flag = True
    else:
      for j in range(i, len(line), 1):
        for k, digit in enumerate(digits):
          if digit == line[i:j]:
            number = (k+1) * 10
            break_flag = True
    if (break_flag):
      break

  break_flag = False
  for i in range(len(line) - 1, -1, -1):
    if line[i].isdigit():
      number += int(line[i])
      break_flag = True
    else:
      for j in range(len(line), i, -1):
        for k, digit in enumerate(digits):
          if digit == line[i:j]:
            number += k + 1
            break_flag = True
    if (break_flag):
      break

  sum += number

print(sum)