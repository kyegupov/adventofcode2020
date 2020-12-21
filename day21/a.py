
from typing import DefaultDict
from collections import defaultdict

input = open('input.txt').readlines()

pairs = []
for line in input:
    ingrs, allergs = line.strip().strip(')').split(' (contains ')
    pairs.append((set(ingrs.split(' ')), set(allergs.split(', '))))

canthave = defaultdict(set)
canhave = defaultdict(set)
all_allergs = set()
discarded = set()
for p1 in pairs:
    for i in p1[0]:
        for a in p1[1]:
            canhave[i].add(a)
        all_allergs.update(p1[1])

count = 0
while True:
    for p1 in pairs:
        for p2 in pairs:
            if p1 != p2:
                diff_aller = p2[1]
                diff_ingr = p1[0]-p2[0]
                for i in diff_ingr:
                    for a in diff_aller:
                        canthave[i].add(a)
    newd = False
    for k,v in canthave.items():
        if v == all_allergs and k not in discarded:
            discarded.add(k)
            newd = True
            for i,p in enumerate(pairs):
                for ing in p[0]:
                    if ing == k:
                        count += 1
                pairs[i] = (p[0]-set([k]), p[1])
    if not newd:
        break

print(discarded)


print(count)