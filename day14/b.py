input = open('input.txt').readlines()
mem = {}
mask = ""
for l in input:
    if l.startswith('mask'):
        mask = l.split(' = ')[1].strip()
    if l.startswith('mem'):
        val = int(l.split(' = ')[1])
        addr = int(l.split('[')[1].split(']')[0])
        bit = 1
        floats = []
        for bv in mask[::-1]:
            if bv == '1':
                addr |= bit
            if bv == 'X':
                floats.append(bit)
            bit *= 2
        for i in range(2**len(floats)):
            for j,f in enumerate(floats):
                bv = i & (1<<j)
                if bv:
                    addr |= f
                else:
                    addr |= f
                    addr -= f
                mem[addr] = val
        mem[addr]=val
print(mem)
print(sum(mem.values()))