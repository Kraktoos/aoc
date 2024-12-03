import re

content = open("input.txt").read().strip()

results = re.findall(r"mul\(\d+,\d+\)", content)
total = 0
for result in results:
  _, right = result.split("(")
  num1, num2 = (int(x) for x in right[:-1].split(","))
  total += num1 * num2

print(total)