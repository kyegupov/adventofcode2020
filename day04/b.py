input = open('input.txt').read().splitlines()
import re
hgt = re.compile('^(\d+)(cm|in)$')
hcl = re.compile('^#[0-9a-f]{6}$')
ecl = re.compile('^amb|blu|brn|gry|grn|hzl|oth$')
pid = re.compile('^[0-9]{9}$')

def hgtv(x):
    m = hgt.match(x)
    if m and m.group(2)=='cm':
        x = m.group(1)
        return int(x)>=150 and int(x)<=193
    if m and m.group(2)=='in':
        x = m.group(1)
        return int(x)>=59 and int(x)<=76


req = {
    'byr': lambda x: int(x) >=1920 and int(x)<=2002,
    'iyr': lambda x: int(x) >=2010 and int(x)<=2020,
    'eyr': lambda x: int(x) >=2020 and int(x)<=2030,
    'hgt': hgtv,
    'hcl': lambda x: hcl.match(x),
    'ecl': lambda x: ecl.match(x),
    'pid': lambda x: pid.match(x),
}

s = set()
res = 0
reqk = set(req.keys())
for l in input + ['']:
    if l:
        a = l.split(' ')
        for aa in a:
            k,v=aa.split(':')
            # print(k, k in req, req[k](v))
            if k in req:
                if req[k](v):
                    s.add(k)
                else:
                    print(k,v)
    else:
        # print(s)
        if s.intersection(reqk) == reqk:
            res += 1
        s=set()

print(res)