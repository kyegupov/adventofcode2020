input = [int(x) for x in open('input.txt').read().splitlines()]

input.sort()
input = [0] + input + [input[-1]+3]
d1 = 0
d3 = 0
for i in range(1, len(input)):
    if input[i]-input[i-1] == 1:
        d1 += 1
    if input[i]-input[i-1] == 3:
        d3 += 1        
print(d1*d3)