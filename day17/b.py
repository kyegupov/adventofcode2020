input = open('input.txt').readlines()

a = set()
for y,l in enumerate(input):
    for x,c in enumerate(l):
        if c == '#':
            a.add((x,y,0,0))

for k in range(6):
    a1 = a.copy()
    dims = []
    for d in range(4):
        dmin = min([b[d] for b in a])
        dmax = max([b[d] for b in a])
        dims.append((dmin, dmax))
    for x in range(dims[0][0]-1, dims[0][1]+2):
        for y in range(dims[1][0]-1, dims[1][1]+2):
            for z in range(dims[2][0]-1, dims[2][1]+2):
                for w in range(dims[3][0]-1, dims[3][1]+2):
                    neighbours = 0
                    for dx in range(-1, 2):
                        for dy in range(-1, 2):
                            for dz in range(-1, 2):
                                for dw in range(-1, 2):
                                    if dx != 0 or dy != 0 or dz != 0 or dw != 0:
                                        if (x+dx,y+dy,z+dz,w+dw) in a:
                                            neighbours += 1
                    if (x,y,z,w) in a:
                        if neighbours <2 or neighbours > 3:
                            a1.remove((x,y,z,w))
                    else:
                        if neighbours == 3:
                            a1.add((x,y,z,w))
    a = a1

print(len(a1))