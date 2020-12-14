input = open('input.txt').readlines()
mem = {}
mask = ""
for l in input:
    if l.startswith('mask'):
        mask = l.split(' = ')[1].strip()
    if l.startswith('mem'):
        val = int(l.split(' = ')[1])
        addr = l.split('[')[1].split(']')[0]
        bit = 1
        for bv in mask[::-1]:
            if bv == '1':
                val |= bit
                # print(bv, bit)
            if bv == '0':
                val |= bit
                val -= bit
                # print(bv, bit)
            bit *= 2
        mem[addr]=val
print(mem)
print(sum(mem.values()))