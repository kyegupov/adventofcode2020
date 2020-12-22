from collections import deque
from os import stat

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


def game(p1, p2):
    states = set()
    c = 0
    while len(p1) and len(p2):
        state = (tuple(p1), tuple(p2))
        if state in states:
            return 1,p1
        else:
            states.add(state)
        c += 1
        c1 = p1.popleft()
        c2 = p2.popleft()
        # print(c, c1, c2, p1,p2)
        if c1 <= len(p1) and c2 <= len(p2):
            d1 = deque(list(p1)[:c1])
            d2 = deque(list(p2)[:c2])
            pid, _ = game(d1, d2)
            rw = p1 if pid==1 else p2
        else:
            rw = p1 if c1>c2 else p2

        if rw is p1:
            rw.append(c1)
            rw.append(c2)
        else:
            rw.append(c2)
            rw.append(c1)

    return (1,p1) if len(p1) else (2,p2)

pid, curp = game(p1,p2)
print(curp)
curp.reverse()
s = 0
for i,c in enumerate(curp):
    s += (i+1)*c

print(s)