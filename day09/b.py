inp = [int(x) for x in open('input.txt').read().splitlines()]
cum = [0]
for i in inp:
    cum.append(cum[-1]+i)

for i in range(len(inp)-1):
    for j in range(1, len(inp)):
        if cum[j]-cum[i] == 14360655:
            slice = inp[i:j]
            print(slice)
            print(sum(slice))
            print(min(slice)+max(slice))



