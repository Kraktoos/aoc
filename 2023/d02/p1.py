input = open("input.txt", "r").read().strip().splitlines()
sum = 0

max_set = dict()

max_set["red"] = 12
max_set["green"] = 13
max_set["blue"] = 14

curr_game = 0
for line in input:
  curr_game += 1
  important_info = line.split(":")[-1].strip()
  rounds = important_info.split(";")
  over = False
  for round in rounds:
    if (over):
      break
    round = round.strip().split(",")
    for color_combo in round:
      color_combo = color_combo.strip().split(" ")
      if int(color_combo[0]) > max_set[color_combo[1]]:
        over = True
        break
  if (not over):
    sum += curr_game

print(sum)