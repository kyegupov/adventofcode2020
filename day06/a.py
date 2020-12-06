groups = []
acc = set()
for l in open('input.txt').read().splitlines() + ['']:
    if l:
        acc.update(set(l))
    else:
        groups.append(len(acc))
        acc = set()

print(sum(groups))

