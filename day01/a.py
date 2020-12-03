data = set(int(x) for x in open('input.txt').read().splitlines())
for x in data:
    if 2020-x in data:
        print(x*(2020-x))
        break

