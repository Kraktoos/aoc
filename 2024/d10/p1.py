matrix = [[int(x) for x in line] for line in open("input.txt", "r").read().strip().splitlines()]

def qtd_caminhos_ate_9(matrix, curr, i, j):
  todos_os_9s = set()
  if i < 0 or i >= len(matrix) or j < 0 or j >= len(matrix[0]):
    return set()
  if matrix[i][j] != curr:
    return set()
  if curr == 9:
    return {(i, j)}
  for caminho in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
    todos_os_9s |= qtd_caminhos_ate_9(matrix, curr + 1, i + caminho[0], j + caminho[1])
  return todos_os_9s

total = 0
for i in range(len(matrix)):
  for j in range(len(matrix[0])):
    if matrix[i][j] == 0:
      total += len(qtd_caminhos_ate_9(matrix, 0, i, j))
print(total)