from collections import defaultdict
board = defaultdict(lambda x: '.')

lines = open('input.txt').read().splitlines()
for y,l in enumerate(lines):
    for x,c in enumerate(l):
        board[(x,y)] = c

while True:
    board2 = board.copy()
    for y in range(len(lines)):
        for x in range(len(lines[0])):
            occu = 0
            for dy in range(-1, 2):
                for dx in range(-1, 2):
                    if (dx != 0 or dy != 0) and board.get((x+dx,y+dy))=='#':
                        occu +=1
            # print(x,y,occu)
            if board[(x,y)] == 'L' and occu == 0:
                board2[(x,y)] = '#'
            elif board[(x,y)] == '#' and occu >= 4:
                board2[(x,y)] = 'L'
    if board == board2:
        break
    else:
        board = board2

for y in range(len(lines)):
    o = ''
    for x in range(len(lines[0])):
        o += board[(x,y)]
    print(o)



print(sum(1 for v in board.values() if v=='#'))







