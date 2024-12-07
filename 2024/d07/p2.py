lines = [x.split(": ") for x in open("input.txt", "r").read().strip().splitlines()]
data = [(int(line[0]), list(map(int, line[1].split(" ")))) for line in lines]

total = 0
for excepted_result, numbers in data:
  current_results = {numbers[0]}
  for number in numbers[1:]:
    old_results = current_results.copy()
    current_results.clear()
    for curr in old_results:
      current_results.add(curr + number)
      current_results.add(curr * number)
      current_results.add(int(str(curr) + str(number))) # nice change
  for actual_result in current_results:
    if actual_result == excepted_result:
      total += actual_result
      continue
print(total)