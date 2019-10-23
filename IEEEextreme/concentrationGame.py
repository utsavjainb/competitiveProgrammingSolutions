import random
from collections import defaultdict

n = int(input())

deck = [x + 1 for x in range(n)] * 2
random.shuffle(deck)

card_cache = defaultdict(set)


for values in (range(1, 2*n+1, 2)):
    select1 = values
    select2 = values + 1
    print(select1, select2, sep=" ")
    line = input()
    if line == "MATCH":
        continue
    else:
        line = line.split()
        cards = [int(x) for x in line]
        card1 = cards[0]
        if len(cards) == 2:
            card2 = cards[1]
        card_cache[card1].add(select1)
        card_cache[card2].add(select2)

for key, value in card_cache.items():
    select1 = value.pop()
    select2 = value.pop()
    print(select1, select2, sep=" ")
    input()
print(-1)




