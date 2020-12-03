trees = open('input.txt').read().splitlines()

x = 0
res = 0
for row in trees:
    xx = x % len(row)
    if row[xx] == '#':
        res += 1
    x += 3

print(res)
