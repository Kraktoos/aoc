input = open("input.txt", "r").read().strip().splitlines()
sum = 0

curr_game = 0
for line in input:
  curr_game += 1
  important_info = line.split(":")[-1].strip()
  rounds = important_info.split(";")
  over = False
  max = dict()
  max["blue"] = 0
  max["red"] = 0
  max["green"] = 0
  for round in rounds:
    if (over):
      break
    round = round.strip().split(",")
    for color_combo in round:
      color_combo = color_combo.strip().split(" ")
      if int(color_combo[0]) > max[color_combo[1]]:
        max[color_combo[1]] = int(color_combo[0])
  total_max = max["blue"] * max["red"] * max["green"]
  sum += total_max

print(sum)