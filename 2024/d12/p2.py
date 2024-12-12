# I couldn't do it... Oh well

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
        itens_perimetro.append(new_tuple)
  
  points = 0
  while len(itens_perimetro) > 0:
    i, j = itens_perimetro[-1]
    # print("First", itens_perimetro)
    # find lowest point or the point in the most right
    if itens_perimetro.count((i, j)) >= 2:
      current_max = itens_perimetro.count((i, j))

      height = i-1
      while (height, j) in itens_perimetro:
        height -= 1
      height = i
      while (height, j) in itens_perimetro:
        if itens_perimetro.count((height, j)) > current_max:
          current_max = itens_perimetro.count((height, j))
        itens_perimetro = list(filter(lambda x: x != (height, j), itens_perimetro))
        height += 1
      itens_perimetro.append((height, j))

      width = j-1
      while (height, width) in itens_perimetro:
        width -= 1
      width = j
      while (height, width) in itens_perimetro:
        if itens_perimetro.count((height, width)) > current_max:
          current_max = itens_perimetro.count((height, width))
        itens_perimetro = list(filter(lambda x: x != (height, width), itens_perimetro))
        width += 1

      height -= 1
      width -= 1

      points += current_max-1
      continue

    height = i-1
    while (height, j) in itens_perimetro:
      height -= 1
    height = i
    while (height, j) in itens_perimetro:
      itens_perimetro.remove((height, j))
      height += 1
    itens_perimetro.append((height, j))

    width = j-1
    while (height, width) in itens_perimetro:
      width -= 1
    width = j
    while (height, width) in itens_perimetro:
      itens_perimetro.remove((height, width))
      width += 1

    height -= 1
    width -= 1

    # final_set.add((height, width))
    points += 1
    # print("Second", height, width)
    # print("Final: ", final_set)

  return points



  # print(itens_perimetro)
  # print(len(itens_perimetro))

  # return 1

  # n_sides = 0
  # for location, direction in itens_perimetro:
  #   include = True
  #   for new_i, new_j in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
  #     i, j = location
  #     new_tuple = (i + new_i, j + new_j)
  #     if (new_tuple, direction) in itens_perimetro:
  #       include = False
  #       break
      
  #   if include: n_sides += 1
  # return n_sides

total = 0
for i in range(len(field)):
  for j in range(len(field[i])):
    plant = field[i][j]
    if plant == ".":
      continue

    region_set = get_region_set(plant, i, j)
    total += len(region_set) * get_n_sides(region_set)

print(total)