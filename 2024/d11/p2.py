stones = open("input.txt", "r").read().strip().split(" ")

known_results = {}
def how_many_stones(stone, blinks_left):
  args = (stone, blinks_left)
  if args in known_results:
    return known_results[args]
  if blinks_left == 0:
    return 1
  
  new_blinks_left = blinks_left - 1
  if stone == "0":
    known_results[args] = how_many_stones("1", new_blinks_left)
  elif len(stone) % 2 == 0:
    midpoint = len(stone) // 2
    known_results[args] = how_many_stones(stone[:midpoint], new_blinks_left) + how_many_stones(str(int(stone[midpoint:])), new_blinks_left)
  else:
    known_results[args] = how_many_stones(str(int(stone) * 2024), new_blinks_left)
  return known_results[args]

total = 0
for stone in stones:
  total += how_many_stones(stone, 75)

print(total)