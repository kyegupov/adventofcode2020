x,y = 0,0
wx,wy = 10,-1
for l in open('input.txt').read().splitlines():
    c = l[0]
    n = int(l[1:])
    if c=='N':
        wy-= n
    if c=='E':
        wx+= n
    if c=='S':
        wy+= n
    if c=='W':
        wx-= n
    if c=='F':
        x += wx*n
        y += wy*n
    if c=='L':
        for i in range(n//90):
            t = wx
            wx = wy
            wy = -t
    if c=='R':
        for i in range(n//90):
            t = wx
            wx = -wy
            wy = t
    print(x,y, wx,wy)
print(abs(x)+abs(y))        