conteudo = open("input.txt", "r").read().strip().split("\n\n")

right_of_list, sequences = [tuple(x.split("|")) for x in conteudo[0].splitlines()], [x.split(",") for x in conteudo[1].splitlines()]

left_of = {}
for before, after in right_of_list:
  left_of[after] = left_of.get(after, []) + [before]

total = 0
for sequence in sequences:
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