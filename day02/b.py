lines = open('input.txt').read().splitlines()

res = 0
for l in lines:
    rul, ex = l.split(':')
    rng, ltr = rul.split(' ')
    x,y = (int(a) for a in rng.split('-'))
    ex = ex.strip()

    if (ex[x-1]==ltr) != (ex[y-1]==ltr):
        res+=1

print(res)
