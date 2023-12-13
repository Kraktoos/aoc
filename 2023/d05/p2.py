input = open("input.txt", "r").read().strip().split("\n\n")

def get_destination(datas, source):
  for data in datas:
    if source >= data["source"] and source <= data["source"] + data["range"] - 1:
      return data["destination"] + (source - data["source"])
  return source

seeds = input[0].split(": ")[1].split(" ")
sources_to_destinations_array = input[1:]
sources_to_destinations = {}
categories = []

for part in sources_to_destinations_array:
  full = part.splitlines()
  lines = full[1:]

  new_map = []

  for line in lines:
    items = line.split(" ")
    data = {
      "source": int(items[1]),
      "destination": int(items[0]),
      "range": int(items[2])
    }
    new_map.append(data)

  categories.append(full[0].split(" ")[0])
  sources_to_destinations[categories[-1]] = new_map

smallest = 10000000000000000000
for _ in range(len(seeds)//2):
  pair = {
    'start': int(seeds[_*2]),
    'range': int(seeds[_*2+1])
  }
  print(pair)
  for seed_increment in range(pair["range"]):
    last = pair["start"] + seed_increment
    for category in categories:
      last = get_destination(sources_to_destinations[category], last)
    if last < smallest:
      smallest = last

print(smallest)