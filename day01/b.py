data = set(int(x) for x in open('input.txt').read().splitlines())
for x in data:
    for y in data:
        if 2020-x-y in data:
            print(x*y*(2020-x-y))
            break

