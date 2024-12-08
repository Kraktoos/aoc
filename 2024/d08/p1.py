matrix = [[c for c in x] for x in open("input.txt", "r").read().splitlines()]
final_matrix = [[0 for _ in x] for x in matrix]

def in_matrix(i, j):
  return 0 <= i < len(matrix) and 0 <= j < len(matrix[0])

for i1 in range(len(matrix)):
  for j1 in range(len(matrix[0])):

    for i2 in range(len(matrix)):
      for j2 in range(len(matrix[0])):
        if matrix[i1][j1] == matrix[i2][j2] and not (i1 == i2 and j1 == j2) and matrix[i1][j1] != ".":
          diff_i, diff_j = i2 - i1, j2 - j1

          go_to_i1 = i1 - diff_i
          go_to_j1 = j1 - diff_j
          go_to_i2 = i2 + diff_i
          go_to_j2 = j2 + diff_j

          if in_matrix(go_to_i1, go_to_j1):
              final_matrix[go_to_i1][go_to_j1] = 1
          if in_matrix(go_to_i2, go_to_j2):
              final_matrix[go_to_i2][go_to_j2] = 1

print(sum([x for xs in final_matrix for x in xs]))