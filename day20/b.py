from collections import defaultdict
from pprint import pprint
input = open('input.txt').readlines()

tiles = {}
tile = None

for l in input:
    if l.startswith('Tile'):
        tile = int(l.split(' ')[1].strip().strip(':'))
        tiles[tile] = []
    if l.startswith('.') or l.startswith('#'):
        tiles[tile].append(l.strip())

tile_edges = {}
edge_to_tile_side_flip = defaultdict(list)
for num, tile in tiles.items():
    left = ''.join(l[0] for l in tile)
    right = ''.join(l[-1] for l in tile)
    tile_edges[num] = [tile[0], right, tile[-1][::-1], left[::-1]]
    for i in range(4):
        for flip in (0,1):
            ii = i
            if flip and (i==0 or i==2):
                ii = (i+2)%4
            edge = tile_edges[num][ii]
            if flip:
                edge = edge[::-1]
            edge_to_tile_side_flip[edge].append((num, i, flip))

def get_edge(tnum_rot_flip, side):
    tnum, rot, flip = tnum_rot_flip
    i = (side - rot) %4
    if flip and (i==0 or i==2):
        i = (i+2)%4
    edge = tile_edges[tnum][i]
    if flip:
        edge = edge[::-1]
    return edge

def render(tnum_rot_flip):
    tnum, rot, flip = tnum_rot_flip
    tile = tiles[tnum][:]
    if flip:
        tile = tile[::-1]
    for i in range(rot):
        tile = [''.join(line[x] for line in tile[::-1]) for x in range(len(tile[0]))]
    return tile


import math
nx, ny = int(math.sqrt(len(tiles))),int(math.sqrt(len(tiles)))


pprint(len(edge_to_tile_side_flip))
# pprint(render((2621,0,0)))
# print('-')
# pprint(render((2621,0,1)))
# print(get_edge((2621,0,0),1))
# print(get_edge((2621,0,1),1))
# raise(x)

image = None

def lay(y, x, used_tiles):
    global image
    if image:
        return
    candidates = None
    top = None
    left = None
    if y > 0:
        prev_bottom=get_edge(laid[y-1][x], 2)
        top = prev_bottom[::-1]
        candidates = set()
        for (num, side, flip) in edge_to_tile_side_flip[top]:
            # assert get_edge((num, (0-side%4), flip), 0) == top
            if num not in used_tiles:
                candidates.add((num, (0-side)%4, flip))

    if x > 0:
        prev_right=get_edge(laid[y][x-1], 1)
        left = prev_right[::-1]
        candidates2 = set()
        for (num, side, flip) in edge_to_tile_side_flip[left]:
            # assert get_edge((num, (3-side%4), flip), 3) == left
            if num not in used_tiles:
                candidates2.add((num, (3-side)%4, flip))
        if candidates:
            candidates = candidates.intersection(candidates2)
        else:
            candidates = candidates2
    # if y > 0 and x > 4:

    for c in candidates:
        # print(y,x,c)
        laid[y][x] = c
        used_tiles.add(c[0])
        xx = x + 1
        yy = y
        if xx >= nx:
            xx = 0
            yy = y+1
        if yy == ny:
            # pprint(laid)
            image = []
            for yy in range(y+1):
                for row in range(1, len(tiles[laid[0][0][0]])-1):
                    out = []
                    for xx in range(nx):
                        if laid[yy][xx]:
                            out.append(render(laid[yy][xx])[row][1:-1])
                    image.append(''.join(out))

            return
        else:
            lay(yy, xx, used_tiles)
        used_tiles.remove(c[0])

laid = []
for y in range(ny):
    laid.append([None] * nx)
for i, tnum in enumerate(tiles):
    # print(i)
    for rot in range(4):
        for flip in range(2):
            laid[0][0]=(tnum,rot,flip)
            lay(0, 1, set([tnum]))

pprint(image)

nessie = '''                  #
#    ##    ##    ###
 #  #  #  #  #  #   '''.splitlines()
for flip in range(2):
    for rot in range(4):
        monsters = 0
        for dy in range(len(image)-len(nessie)):
            for dx in range(len(image[0])-len(nessie[0])):
                ok = True
                for y, row in enumerate(nessie):
                    for x, c in enumerate(row):
                        if c == '#' and image[y+dy][x+dx]!='#':
                            ok = False
                if ok:
                    monsters += 1
        if monsters:
            tot = sum(sum(1 for c in row if c=='#') for row in image)
            nes = sum(sum(1 for c in row if c=='#') for row in nessie)
            print(tot-monsters* nes)
        image = [''.join(line[x] for line in image[::-1]) for x in range(len(image[0]))]
    image = image[::-1]