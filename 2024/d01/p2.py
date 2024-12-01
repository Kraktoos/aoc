from collections import Counter

lists = open("input.txt").read().strip().splitlines()
left, right = [], []
for item in lists:
  current = item.split("   ")
  left.append(int(current[0]))
  right.append(int(current[1]))

right_counted = Counter(right)
similarity = 0
for item in left:
  similarity += item * right_counted[item]

print(similarity)