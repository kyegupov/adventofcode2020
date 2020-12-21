
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
    # a2maybei = defaultdict(set)
    # canhave = defaultdict(set)
    # for p1 in pairs:
    #     for i in p1[0]:
    #         for a in p1[1]:
    #             canhave[i].add(a)
    #             a2maybei[a].add(i)

    for p1 in pairs:
        for p2 in pairs:
            if p1 != p2:
                diff_aller = p2[1]
                diff_ingr = p1[0]-p2[0]
                for i in diff_ingr:
                    for a in diff_aller:
                        canthave[i].add(a)
    canhave = defaultdict(set)
    for p1 in pairs:
        for i in p1[0]:
            for a in p1[1]:
                if a not in canthave[i]:
                    canhave[i].add(a)
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


a2i = {}
while len(a2i) < len(all_allergs):
    known = set(a2i.keys())
    for k,v in canhave.items():
        d = v-set(known)
        if len(d) == 1:
            a2i[d.pop()] = k



# print(canthave)
# print(canhave)
print(a2i)

print(','.join(a2i[a] for a in sorted(a2i.keys())))


