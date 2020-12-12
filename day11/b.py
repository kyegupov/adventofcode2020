from collections import defaultdict
board = defaultdict(lambda: 'X')

lines = open('input.txt').read().splitlines()
for y,l in enumerate(lines):
    for x,c in enumerate(l):
        board[(x,y)] = c

while True:
    print('iter')
    changed = False
    board2 = board.copy()
    for y in range(len(lines)):
        # print(y)
        for x in range(len(lines[0])):
            occu = 0
            for dy in range(-1, 2):
                for dx in range(-1, 2):
                    if (dx != 0 or dy != 0):
                        for k in range(1,99999999999999):
                            c = board[x+k*dx,y+k*dy]
                            # print('c', x+k*dx,y+k*dy, c)
                            if c =='#':
                                occu += 1
                                break
                            if c == 'X' or c=='L':
                                break
            # print(x,y,occu)
            if board[(x,y)] == 'L' and occu == 0:
                board2[(x,y)] = '#'
            elif board[(x,y)] == '#' and occu >= 5:
                board2[(x,y)] = 'L'
            if board2[(x,y)] != board[(x,y)]:
                changed = True
    if not changed:
        break
    else:
        board_old = board
        board = board2

# for y in range(len(lines)):
#     o = ''
#     for x in range(len(lines[0])):
#         o += board_old[(x,y)]
#     print(o)
# print('===========')

for y in range(len(lines)):
    o = ''
    for x in range(len(lines[0])):
        o += board[(x,y)]
    print(o)



print(sum(1 for v in board.values() if v=='#'))







