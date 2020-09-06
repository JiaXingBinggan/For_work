cards = ['s3', 's5', 's1', 's4', 's13', 'h1', 'p3', 'p2', 'q5', 'q4', 'q9', 'k2', 'k1']

priorities = {'k': 4, 's': 3, 'h': 2, 'p': 1, 'q': 0}

buckets = [[] for _ in range(5)]

for card in cards:
    buckets[priorities[card[0]]].append([card[0], int(card[1:])])

for item in buckets:
    item.sort(key=lambda s: s[1])
print(buckets)
res = []
for i in range(len(buckets) - 1, -1, -1):
    for item in buckets[i]:
        item[1] = str(item[1])
        res.append(''.join(item))

print(res)
