field = [[x for x in line] for line in open("input.txt", "r").read().strip().splitlines()]

def get_region_set(plant, i, j):
  if i < 0 or i >= len(field) or j < 0 or j >= len(field[0]):
    return set()

  if field[i][j] != plant:
    return set()

  rs = {(i, j)}
  field[i][j] = "."
  for new_i, new_j in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
    rs |= get_region_set(plant, i + new_i, j + new_j)
  
  return rs

def get_n_sides(rs):
  itens_perimetro = []
  for i, j in rs:
    for new_i, new_j in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
      new_tuple = (i + new_i, j + new_j)
      if new_tuple not in rs:
        itens_perimetro.append((new_tuple, (new_i, new_j)))

  n_sides = 0
  for location, direction in itens_perimetro:
    include = True
    for new_i, new_j in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
      i, j = location
      new_tuple = (i + new_i, j + new_j)
      if (new_tuple, direction) in itens_perimetro:
        include = False
        break
      
    if include: n_sides += 1
  return n_sides

total = 0
for i in range(len(field)):
  for j in range(len(field[i])):
    plant = field[i][j]
    if plant == ".":
      continue

    region_set = get_region_set(plant, i, j)
    total += len(region_set) * get_n_sides(region_set)

print(total)