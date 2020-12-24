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

board = defaultdict(bool)

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
    board[xyz]=not board[xyz]

print(sum(int(v) for v in board.values()))
for day in range(100):
    board2 = board.copy()
    minx = min(t[0] for t in board)
    maxx = max(t[0] for t in board)
    miny = min(t[1] for t in board)
    maxy = max(t[1] for t in board)
    for x in range(minx-1, maxx+2):
        for y in range(miny-1, maxy+2):
            z = 0-x-y
            neigh = 0
            for d in dirs.values():
                xyz = (x+d[0],y+d[1],z+d[2])
                if board[xyz]:
                    neigh += 1
            if board[(x,y,z)]:
                if neigh == 0 or neigh > 2:
                    board2[(x,y,z)] = False
            else:
                if neigh == 2:
                    board2[(x,y,z)] = True

    board = board2
    print(day+1, sum(int(v) for v in board.values()))




