from collections import deque
input = open('input.txt').read()

cups = [int(i) for i in input]
prev = cups[0]
nxt = {}
for c in cups[1:]:
    nxt[prev] = c
    prev = c
nxt[prev] = cups[0]

mc =  max(cups)

c = cups[0]
for move in range(100):

    # print(move, c)
    n1 = nxt[c]
    n2 = nxt[n1]
    n3 = nxt[n2]
    # remove 3
    c2 = nxt[n3]
    nxt[c] = c2

    tgt = c - 1
    while True:
        if tgt == 0:
            tgt = mc
        if tgt == n1 or tgt == n2 or tgt == n3:
            tgt = tgt - 1
        else:
            break

    # print(tgt)

    nxt[n3] = nxt[tgt]
    nxt[tgt] = n1

    # next cup
    c = c2


x = nxt[1]
chars = []
while True:
    chars.append(str(x))
    x = nxt[x]
    if x == 1:
        break
print(''.join(chars))


