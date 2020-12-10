input = [int(x) for x in open('input.txt').read().splitlines()]


input.sort()
input = input + [input[-1]+3]

sols = {0:1}

for inp in input:
    sols[inp] = sum(sols.get(inp-i, 0) for i in range(1, 4))
print(sols[input[-1]])