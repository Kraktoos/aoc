# I still don't get part 2

import re

robots = open("input.txt", "r").read().splitlines()

w, h = 101, 103
seconds = 5000

for sec_att in range(seconds):
  matrix = [[0 for _ in range(w)] for __ in range(h)]
  for robot in robots:
    px, py, vx, vy = map(int, re.findall(r"([+-]?\d+)", robot))
    px = ((px+1) + vx * sec_att) % w - 1
    py = ((py+1) + vy * sec_att) % h - 1
    matrix[py][px] += 1


  top_left =  [matrix[i][:w // 2] for i in range(h // 2)]
  top_right = [matrix[i][w // 2+1:] for i in range(h // 2)]
  bot_left =  [matrix[i][:w // 2] for i in range(h // 2+1, h)]
  bot_right = [matrix[i][w // 2+1:] for i in range(h // 2+1, h)]
  sum_top_left = sum([sum(x) for x in top_left])
  sum_top_right = sum([sum(x) for x in top_right])
  sum_bot_left = sum([sum(x) for x in bot_left])
  sum_bot_right = sum([sum(x) for x in bot_right])

  if sum_bot_left == sum_bot_right and sum_top_left == sum_top_right and sum_bot_left > sum_top_left:
    for l in matrix:
      print(("".join([str(x) for x in l])).replace("0", "."))
    
    print("")


  # print(prod([sum([sum(x) for x in top_left]), sum([sum(x) for x in top_right]), sum([sum(x) for x in bot_left]), sum([sum(x) for x in bot_right])]))