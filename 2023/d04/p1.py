input = open("input.txt", "r").read().strip().splitlines()
sum = 0

scores = dict()

crrGame = 1
for line in input:
  winning = line.split("|")[0].strip().split(":")[1].strip().split(" ")
  numbers = line.split("|")[1].strip().split(" ")

  for n in numbers:
    if n in winning and n != "":
      if crrGame not in scores:
        scores[crrGame] = 1
      else:
        scores[crrGame] *= 2

  crrGame += 1

for game in scores:
  sum += scores[game]

print(sum)