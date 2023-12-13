from math import lcm

path, node_list = open("input.txt", "r").read().split("\n\n")

node_list = node_list.splitlines()

nodes = dict()
for node in node_list:
  splitted = node.split(" = ")
  left_and_right = splitted[1].split(", ")
  current = splitted[0]
  nodes[current] = {
    "L": left_and_right[0][1:],
    "R": left_and_right[1][:-1]
  }

current_nodes = []
for node in nodes:
  if node[-1] == "A":
    current_nodes.append(node)

multiples = []
for i in range(len(current_nodes)):
  current_chars = current_nodes[i]
  steps = 0
  break_outer = False
  while True:
    for direction in path:
      if current_chars[-1] == "Z":
        break_outer = True
        break
      steps += 1
      current_chars = nodes[current_chars][direction]
    if break_outer:
      break
  multiples.append(steps)

print(lcm(*multiples))