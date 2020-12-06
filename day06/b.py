groups = []
acc = None
for l in open('input.txt').read().splitlines() + ['']:
    if l:
        if acc == None:
            acc = set(l)
        else:
            acc = acc.intersection(set(l))
    else:
        groups.append(len(acc))
        acc = None

print(groups)
print(sum(groups))

