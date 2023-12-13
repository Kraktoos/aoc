input = open("input.txt", "r").read().strip().splitlines()

# pair = (int("".join(input[0].split(" ")[1:])), int("".join(input[1].split(" ")[1:])))
pair = tuple(map(lambda x: int("".join(x.split(" ")[1:])), input[:2]))

total = 0

time = pair[0]
record_distance = pair[1]
for current_attempt in range(time):
  if (current_attempt * (time - current_attempt)) > record_distance:
    total += 1

print(total)