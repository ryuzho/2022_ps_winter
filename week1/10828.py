# 스택

import sys

N = int(sys.stdin.readline())
commands = []
stack = []
for _ in range(N):
    commands.append(list(sys.stdin.readline().split()))

for comm in commands:

    if comm[0] == 'push':
        stack.append(comm[1])
    elif comm[0] == 'pop':
        if len(stack) == 0: print(-1)
        else: print(stack.pop(-1))
    elif comm[0] == 'size':
        print(len(stack))
    elif comm[0] == 'empty':
        if len(stack) == 0: print(1)
        else: print(0)
    elif comm[0] == 'top':
        if len(stack) == 0: print(-1)
        else: print(stack[-1])