import re
from math import prod

robots = open("input.txt", "r").read().splitlines()

w, h = 101, 103
seconds = w * h

curr_min = (float("inf"), float("inf"))

for sec_att in range(1, seconds):
  matrix = [[0 for _ in range(w)] for __ in range(h)]
  for robot in robots:
    px, py, vx, vy = map(int, re.findall(r"([+-]?\d+)", robot))
    px = ((px+1) + vx * sec_att) % w - 1
    py = ((py+1) + vy * sec_att) % h - 1
    matrix[py][px] += 1

  break_all = False
  for l in matrix:
    for item in l:
      if item not in {0, 1}:
        break_all = True
        break
    if break_all: break

  if break_all: continue

  print(sec_att)
  break