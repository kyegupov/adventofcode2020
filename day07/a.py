from collections import defaultdict
lines = open('input.txt').read().splitlines()


dad = defaultdict(set)
for l in lines:
    words = l.split(' ')
    outer = tuple(words[:2])
    inner = [tuple(words[4+1+i:4+3+i]) for i in range(0, len(words)-4, 4)]
    for i in inner:
        dad[i].add(outer)


cont = set()
queue = set([('shiny','gold')])
while len(queue):
    b = queue.pop()
    for bb in dad[b]:
        if bb in cont:
            continue
        cont.add(bb)
        queue.add(bb)

# print(cont)
print(len(cont))
