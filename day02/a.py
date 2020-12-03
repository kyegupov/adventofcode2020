lines = open('input.txt').read().splitlines()

res = 0
for l in lines:
    rul, ex = l.split(':')
    rng, ltr = rul.split(' ')
    x,y = (int(a) for a in rng.split('-'))
    ex = ex.strip()
    lcount = len([c for c in ex if c==ltr])
    if lcount >=x and lcount <= y:
        res+=1

print(res)
