histories = list(map(lambda x: list(map(int, x.split())), open("input.txt", "r").read().strip().splitlines()))

total_sequences = []
for line in histories:
  sequences = [line]

  while sum(sequences[-1]) != 0:
    sequences.append([])
    for i in range(len(sequences[-2]) - 1):
      sequences[-1].append(sequences[-2][i+1] - sequences[-2][i])
  
  total_sequences.append(sequences)

sum = 0
for sequence in total_sequences:
  number = 0
  for list in sequence:
    number += list[-1]
  sum += number

print(total_sequences)
print(sum)