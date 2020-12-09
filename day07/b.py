from collections import defaultdict
lines = open('input.txt').read().splitlines()


kids = defaultdict(dict)
for l in lines:
    words = l.split(' ')
    outer = tuple(words[:2])
    inner = [words[4+i:4+3+i] for i in range(0, len(words)-4, 4)]
    for i in inner:
        count = i[0]
        if count != 'no':
            kids[outer][tuple(i[1:])] = int(count)



def process(dad):
    c = 0
    for k, v in kids[dad].items():
        c += v * (1+process(k))
    return c

res = process(('shiny','gold'))

# print(cont)
print(res)
