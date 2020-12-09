from dataclasses import dataclass

@dataclass
class VM:
    code: list
    acc: int
    ip: int

def run(vm: VM):
    x = set()
    while vm.ip < len(vm.code):
        op, arg = vm.code[vm.ip]
        if op == 'nop':
            vm.ip +=1
        elif op == 'acc':
            vm.acc += arg
            vm.ip +=1
        elif op == 'jmp':
            vm.ip += arg
        else:
            raise op
        if vm.ip in x:
            return False
        else:
            x.add(vm.ip)
    return True

lines = open('input.txt').read().splitlines()
code = [l.split(' ') for l in lines]
code = [(op, int(arg)) for (op, arg) in code]

for i in range(len(code)):
    code1 = code[:]
    if code1[i][0] == 'acc':
        continue
    if code1[i][0] == 'jmp':
        code1[i] = ('nop', code1[i][1])
    elif code1[i][0] == 'nop':
        code1[i] = ('jmp', code1[i][1])
    vm = VM(code1, 0, 0)
    ok = run(vm)
    if ok:
        print(vm.acc)
        break

