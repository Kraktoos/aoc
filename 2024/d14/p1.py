import re
from math import prod

robots = open("input.txt", "r").read().splitlines()

w, h = 101, 103
matrix = [[0 for _ in range(w)] for __ in range(h)]
seconds = 100

for robot in robots:
  px, py, vx, vy = map(int, re.findall(r"([+-]?\d+)", robot))
  px = ((px+1) + vx * seconds) % w - 1
  py = ((py+1) + vy * seconds) % h - 1
  matrix[py][px] += 1

top_left =  [matrix[i][:w // 2] for i in range(h // 2)]
top_right = [matrix[i][w // 2+1:] for i in range(h // 2)]
bot_left =  [matrix[i][:w // 2] for i in range(h // 2+1, h)]
bot_right = [matrix[i][w // 2+1:] for i in range(h // 2+1, h)]

print(prod([sum([sum(x) for x in top_left]), sum([sum(x) for x in top_right]), sum([sum(x) for x in bot_left]), sum([sum(x) for x in bot_right])]))