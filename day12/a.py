dir = 1
dirs = [(0,-1),(1,0),(0,1),(-1,0)]
x,y = 0,0
for l in open('input.txt').read().splitlines():
    c = l[0]
    n = int(l[1:])
    if c=='N':
        y-= n
    if c=='E':
        x+= n
    if c=='S':
        y+= n
    if c=='W':
        x-= n
    if c=='F':
        x += dirs[dir][0] * n
        y += dirs[dir][1] * n
    if c=='L':
        dir = dir - (n//90)
        if dir < 0:
            dir += 4
    if c=='R':
        dir = dir + (n//90)
        if dir > 3:
            dir -= 4
    print(x,y, dir)
print(abs(x)+abs(y))        