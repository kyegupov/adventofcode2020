trees = open('input.txt').read().splitlines()

slopes = ((1,1), (3,1), (5,1), (7,1), (1,2))
ress = []
for dx, dy in slopes:
    x=0
    res=0
    for y, row in enumerate(trees):
        if y%dy==0:
            xx = x % len(row)
            if row[xx] == '#':
                res += 1
            x += dx
    ress.append(res)

print(ress)
a = 1
for r in ress:
    a *= r

print(a)