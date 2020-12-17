input = open('input.txt').readlines()

rules = []

res = 0

mode = 'rules'
for l in input:
    if mode == 'rules':
        if l.strip():
            parts = l.split(': ')[1].split(' ')
            ranges = parts[0], parts[2]
            ranges = [tuple(int(x) for x in r.split('-')) for r in ranges]
            rules.extend(ranges)
        else:
            mode = 'yourt'
            continue
    if mode == 'yourt':
        if l.strip():
            pass
        else:
            mode = 'nearby'
            continue
    if mode == 'nearby':
        if l.startswith('nearby'):
            continue
        if l.strip():
            values = [int(x) for x in l.split(',')]


print(res)