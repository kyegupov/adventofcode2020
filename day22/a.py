from collections import deque

input = open('input.txt').readlines()

p1 = deque()
p2 = deque()

curp = p1
for l in input:
    if l.startswith('Player 1'):
        curp = p1
        continue
    if l.startswith('Player 2'):
        curp = p2
        continue
    if l.strip():
        curp.append(int(l))

print(p1,p2)

c = 0
while len(p1) and len(p2):
    c += 1
    c1 = p1.popleft()
    c2 = p2.popleft()
    if c1 > c2:
        p1.append(c1)
        p1.append(c2)
    else:
        p2.append(c2)
        p2.append(c1)
    # print(c, c1, c2, p1,p2)

s = 0
curp = p1 if len(p1) else p2
curp.reverse()
for i,c in enumerate(curp):
    s += (i+1)*c

print(s)