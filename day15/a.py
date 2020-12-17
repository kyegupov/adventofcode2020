input = [int(x) for x in open('input.txt').read().split(',')]

last = {}
lastn = -1
for i,x in enumerate(input[:-1]):
    last[x] = i
    print(i, x)

lastn = input[-1]
print(len(input)-1, lastn)

for i in range(len(input), 2020):
    if lastn in last:
        x = i - last[lastn]-1
    else:
        x = 0
    last[lastn] = i-1
    lastn = x
    print(i, x)

print(lastn)
