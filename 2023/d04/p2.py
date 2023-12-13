input = open("input.txt", "r").read().strip().splitlines()
sum = 0

scratchpads = dict()

crrGame = 1
for card in input:
  winning = card.split("|")[0].strip().split(":")[1].strip().split(" ")
  numbers = card.split("|")[1].strip().split(" ")

  if crrGame not in scratchpads:
    scratchpads[crrGame] = 1

  crr_winning_count = 0
  for n in numbers:
    if n in winning and n != "":
      crr_winning_count += 1
  
  for i in range(crr_winning_count):
    new_card = crrGame + i + 1
    if new_card not in scratchpads:
      scratchpads[new_card] = 1
    scratchpads[new_card] += scratchpads[crrGame]

  crrGame += 1

for game in scratchpads:
  if (game <= len(input)):
    sum += scratchpads[game]

print(sum)