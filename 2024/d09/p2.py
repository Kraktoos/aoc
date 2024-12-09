initial = [int(x) for x in open("input.txt", "r").read().strip()]

blocks = []
id = 0
for i in range(len(initial)):
  num = initial[i]
  if i % 2 == 0:
    blocks.append([id for _ in range(num)])
    id += 1
  else:
    blocks.append(num)

start = len(blocks) - 1

for i in range(len(blocks) - 1, -1, -1):
  if type(blocks[i]) == list:
    for j in range(0, i):
      if type(blocks[j]) == int and blocks[j] >= len(blocks[i]):
        # block = blocks.pop(i)
        block = blocks[i].copy()
        blocks[i] = len(blocks[i])
        blocks[j] -= len(block)
        blocks.insert(j, block)
        break

i = 0
index = 0
total = 0
while True:
  try:
    if type(blocks[i]) == list:
      for block in blocks[i]:
        total += index * block
        index += 1
    else:
      index += blocks[i]
    i += 1
  except:
    break

print(total)