import re

content = open("input.txt").read().strip()

after_dos = content.split("do()")
total = 0
for text in after_dos:
  to_execute = text.split("don't()")[0]
  results = re.findall(r"mul\(\d+,\d+\)", to_execute)
  for result in results:
    _, right = result.split("(")
    num1, num2 = (int(x) for x in right[:-1].split(","))
    total += num1 * num2

print(total)