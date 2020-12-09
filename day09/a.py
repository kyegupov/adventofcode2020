inp = [int(x) for x in open('input.txt').read().splitlines()]

for i in range(25, len(inp)):
    ok = False
    for x in range(i-25, i-1):
        for y in range(x+1,i):
            if inp[x]+inp[y]==inp[i]:
                ok = True
                break
        if ok:
            break
    if not ok:
        print(inp[i])
        break



