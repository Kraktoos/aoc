pairs = list(map(lambda x : {
  "hand": x.split(" ")[0], 
  "bid": int(x.split(" ")[1])},
  open("input.txt", "r").read().splitlines()))

def get_base_score_from_hand(hand):
  already_in = dict()

  for card in hand:
    if card not in already_in:
      already_in[card] = 1
    else:
      already_in[card] += 1

  multiples = dict()
  for card in already_in:
    if already_in[card] not in multiples:
      multiples[already_in[card]] = 1
    else:
      multiples[already_in[card]] += 1

  if 5 in multiples:
    # Five of a kind
    return 10 ** 17
  if 4 in multiples:
    # Four of a kind
    return 10 ** 16
  if 3 in multiples:
    if 2 in multiples:
      # Full house
      return 10 ** 15
    # Three of a kind
    return 10 ** 14
  if 2 in multiples:
    if multiples[2] == 2:
      # Two pair
      return 10 ** 13
    # One pair
    return 10 ** 12
  # High card
  return 10 ** 11

def get_extra_score_from_hand(hand):
  new_hand = str(hand).replace("2", "02").replace("3", "03").replace("4", "04").replace("5", "05").replace("6", "06").replace("7", "07").replace("8", "08").replace("9", "09")
  return int(new_hand.replace("T", "10").replace("J", "11").replace("Q", "12").replace("K", "13").replace("A", "14"))

def get_score_from_hand(hand):
  return get_base_score_from_hand(hand) + get_extra_score_from_hand(hand)

for pair in pairs:
  pair["score"] = get_score_from_hand(pair["hand"])

sorted_pairs = sorted(pairs, key=lambda k: k["score"])

sum = 0
count = 0
for pair in sorted_pairs:
  count += 1
  sum += count * pair["bid"]

print(sum)