import re

input = open('input.txt').readlines()

rules = {}
mode = 'rx'
res = 0

def buildrx(n):
    s = ""
    has_bar = False
    for part in rules[n]:
        if part in rules:
            s += buildrx(part)
        elif part == "|":
            s = '('+s+'|'
            has_bar = True
        elif part.startswith('"'):
            s += part.strip('"')
        else:
            raise part
    if has_bar:
        s += ')'
    return s


for l in input:
    if l.strip() == '':
        mode = 'data'
        rx0s = buildrx('0')
        print(rx0s)
        rx0 = re.compile("^"+rx0s+'$')
    if mode == 'rx':
        n, val = l.split(':')
        rules[n] = val.strip().split(' ')
    if mode == 'data':
        # print(rx0, l.strip(), rx0.match(l.strip()))
        if rx0.match(l.strip()):
            res += 1

print(res)