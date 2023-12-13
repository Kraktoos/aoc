input = open("input.txt", "r").read().strip().splitlines()

times = list(map(int, filter(None, input[0].split(" ")[1:])))
distance = list(map(int, filter(None, input[1].split(" ")[1:])))

pairs = []
for i in range(len(times)):
  pairs.append((times[i], distance[i]))

total = 1

for pair in pairs:
  current_total = 0
  time = pair[0]
  record_distance = pair[1]
  for current_attempt in range(time):
    if (current_attempt * (time - current_attempt)) > record_distance:
      current_total += 1
  total *= current_total

print(total)