from re import findall
from math import gcd

unformatted_sections = [x.splitlines() for x in open("input.txt", "r").read().strip().split("\n\n")]

sections = []
for usection in unformatted_sections:
  sections.append((tuple(map(int, findall("\d+", usection[0]))), tuple(map(int, findall("\d+", usection[1]))), tuple(map(int, findall("\d+", usection[2])))))

total = 0
for (ax, ay), (bx, by), (gx, gy) in sections:
  min_steps = float("+inf")
  for i in range(101):
    for j in range(101):
      resulting_x = ax * i + bx * j
      resulting_y = ay * i + by * j
      if resulting_x != gx or resulting_y != gy:
        continue
      steps_taken = 3 * i + j
      if steps_taken < min_steps:
        min_steps = steps_taken
  if type(min_steps) is int:
    total += min_steps

print(total)