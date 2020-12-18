input = open('input.txt').readlines()

res = 0
for line in input:
    root = []
    node = root
    parent_stack = [root]

    for c in line:
        if c >='0' and c <='9':
            if len(node) == 0 or type(node[-1]) != int:
                node.append(int(c))
            else:
                node[-1] = node[-1] * 10 + int(c)
        if c == '(':
            nnode = []
            node.append(nnode)
            parent_stack.append(node)
            node = nnode
        if c == ')':
            node = parent_stack.pop()
        if c == '*':
            node.append('*')
        if c == '+':
            node.append('+')

    def eval(node):
        if type(node) == int:
            return node
        prev = None
        node2 = []
        for x in node:
            if x == '+':
                pass
            elif x == '*':
                node2.append('*')
            else:
                if prev == '+':
                    node2[-1] = (eval(node2[-1]) + eval(x))
                else:
                    node2.append(x)
            prev = x
        if node2[-1] == '*':
            node2.append(node[-1])

        node = node2
        acc = eval(node[0])
        for i in range(1, len(node), 2):
            if node[i] == '+':
                raise '+'
            elif node[i] == '*':
                acc *= eval(node[i+1])
            else:
                raise node[i]
        return acc

    res += eval(root)

print(res)