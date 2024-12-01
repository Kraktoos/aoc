lists = open("input.txt").read().strip().splitlines()
left, right = [], []
for item in lists:
  current = item.split("   ")
  left.append(int(current[0]))
  right.append(int(current[1]))

left.sort()
right.sort()

total = 0
while len(left) > 0:
  first = left.pop(0)
  second = right.pop(0)
  total += abs(first - second)

print(total)