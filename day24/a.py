input = open('input.txt').readlines()

dirs = dict(
    e=(+1,-1,0),
    se=(0,-1,+1),
    sw=(-1,0,+1),
    w=(-1,+1,0),
    ne=(+1,0,-1),
    nw=(0,+1,-1),
)

from collections import defaultdict

flipped = defaultdict(bool)

for l in input:
    l = l.strip()
    xyz = (0,0,0)
    i = 0
    while i < len(l):
        if l[i:i+2] in dirs:
            d  = dirs[l[i:i+2]]
            i +=2
        elif l[i] in dirs:
            d  = dirs[l[i]]
            i +=1
        else:
            raise l[i]
        xyz = (xyz[0]+d[0],xyz[1]+d[1],xyz[2]+d[2])
    flipped[xyz]=not flipped[xyz]

print(sum(int(v) for v in flipped.values()))



