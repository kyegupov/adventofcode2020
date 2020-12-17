input = open('input.txt').readlines()

rules = {}
yourt = None
othert = []

res = 0

mode = 'rules'
for l in input:
    if mode == 'rules':
        if l.strip():
            name, rparts = l.split(': ')
            rparts = rparts.split(' ')
            ranges = rparts[0], rparts[2]
            ranges = tuple(tuple(int(x) for x in r.split('-')) for r in ranges)
            rules[name] = ranges
        else:
            mode = 'yourt'
            continue
    if mode == 'yourt':
        if l.startswith('your'):
            continue
        if l.strip():
            yourt = [int(x) for x in l.split(',')]
        else:
            mode = 'nearby'
            continue
    if mode == 'nearby':
        if l.startswith('nearby'):
            continue
        if l.strip():
            values = [int(x) for x in l.split(',')]
            all_valid = True
            for v in values:
                valid = False
                for rul in rules.values():
                    for r in rul:
                        if v >= r[0] and v <= r[1]:
                            valid = True
                            break
                if not valid:
                    all_valid = False
            if all_valid:
                othert.append(values)


lrules = list(rules.items())

okrules = []
for i in range(len(yourt)):
    okrules.append(set(lrules))

for ot in othert + [yourt]:
    for i, val in enumerate(ot):
        toremove = set()
        for rul in okrules[i]:
            valid = False
            for rng in rul[1]:
                if val >= rng[0] and val <= rng[1]:
                    valid = True
                    break
            if not valid:
                toremove.add(rul)
                print(i, val, rul)
        okrules[i] -= toremove

rulpos = {}
while len(rulpos) < len(yourt):
    for i, okr in enumerate(okrules):
        if len(okr) == 1:
            only = okr.pop()
            rulpos[i] = only
            for j in range(len(okrules)):
                okrules[j].discard(only)

res = 1
for i, rul in rulpos.items():
    if rul[0].startswith('departure'):
        res *= yourt[i]

print(res)
