stones = open("input.txt", "r").read().strip().split(" ")

for _ in range(25):
  new_stones = []
  for stone in stones:
    if stone == "0":
      new_stones.append("1")
    elif len(stone) % 2 == 0:
      midpoint = len(stone) // 2
      new_stones.append(stone[:midpoint])
      new_stones.append(str(int(stone[midpoint:])))
    else:
      new_stones.append(str(int(stone) * 2024))
  stones = new_stones

print(len(new_stones))