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
        if vm.ip in x:
            print(vm.acc)
            break
        else:
            x.add(vm.ip)

lines = open('input.txt').read().splitlines()
code = [l.split(' ') for l in lines]
code = [(op, int(arg)) for (op, arg) in code]

run(VM(code, 0, 0))

