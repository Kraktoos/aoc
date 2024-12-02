lines = [[int(y) for y in x.split()] for x in open("input.txt").read().strip().splitlines()]

safe_count = 0
for curr in lines:

  for line in [curr[0:i] + curr[i+1:len(curr)] for i in range(len(curr))]:
    last = line[0]
    increasing = line[1] > line[0]
    failed = False
    for number in line[1:]:
      if increasing and 1 <= number - last <= 3:
        pass
      elif not increasing and 1 <= last - number <= 3:
        pass
      else:
        failed = True
        break

      last = number
    if not failed:
      safe_count += 1
      break

print(safe_count)