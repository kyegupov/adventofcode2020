input = open('input.txt').read().splitlines()

req = set(['byr','iyr','eyr','hgt','hcl','ecl','pid'])

s = set()
res = 0
for l in input + ['']:
    if l:
        a = l.split(' ')
        for aa in a:
            k,v=aa.split(':')
            s.add(k)
    else:
        if s.intersection(req) == req:
            res += 1
        s=set()

print(res)