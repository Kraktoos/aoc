initial = [int(x) for x in open("input.txt", "r").read().strip()]

blocks = []
id = 0
for i in range(len(initial)):
  num = initial[i]
  if i % 2 == 0:
    for i in range(num):
      blocks.append(id)
    id += 1
  else:
    for i in range(num):
      blocks.append(-1)

start = len(blocks) - 1

for i in range(len(blocks)):
  if blocks[i] == -1:
    for j in range(start, -1, -1):
      if blocks[j] != -1:
        blocks[i], blocks[j] = blocks[j], blocks[i]
        if j != len(blocks) - 1:
          start = j + 1
        break

blocks = list(filter(lambda x: x != -1, blocks))

total = 0
for i, block in enumerate(blocks):
  total += i * block
print(total)