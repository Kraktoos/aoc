from functools import cache
stones = open("input.txt", "r").read().strip().split(" ")

@cache
def how_many_stones(stone, blinks_left):
  if blinks_left == 0:
    return 1
  if stone == "0":
    return how_many_stones("1", blinks_left - 1)
  if len(stone) % 2 == 0:
    midpoint = len(stone) // 2
    return how_many_stones(stone[:midpoint], blinks_left - 1) + how_many_stones(str(int(stone[midpoint:])), blinks_left - 1)
  return how_many_stones(str(int(stone) * 2024), blinks_left - 1)

print(sum([how_many_stones(stone, 75) for stone in stones]))