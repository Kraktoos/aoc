conteudo = open("input.txt", "r").read().strip().split("\n\n")

right_of_list, sequences = [tuple(x.split("|")) for x in conteudo[0].splitlines()], [x.split(",") for x in conteudo[1].splitlines()]

right_of, left_of = {}, {}
for before, after in right_of_list:
  right_of[before] = right_of.get(before, []) + [after]
  left_of[after] = left_of.get(after, []) + [before]

total = 0

right_sequences = []
for sequence in sequences:
  seen = set()
  can_add = True
  for element in sequence:
    seen.add(element)
    if element in left_of.keys():
      for el in left_of[element]:
          if el not in seen and el in sequence:
            can_add = False
            break
  if can_add:
    right_sequences.append(sequence)

incorrect_sequences = [x for x in sequences if x not in right_sequences]

for i in range(20):
  for sequence in incorrect_sequences:
    seen = set()
    for element in sequence:
      seen.add(element)
      if element in left_of.keys():
        for el in left_of[element]:
          if el not in seen and el in sequence:
            sequence[sequence.index(el)], sequence[sequence.index(element)] = sequence[sequence.index(element)], sequence[sequence.index(el)]

total = 0
for sequence in incorrect_sequences:
  seen, can_add = set(), True
  for element in sequence:
    seen.add(element)
    if element in left_of.keys():
      for el in left_of[element]:
          if el not in seen and el in sequence:
            can_add = False
            break
  if can_add:
    total += int(sequence[len(sequence)//2])

print(total)