# 괄호

import sys

T = int(sys.stdin.readline())

for _ in range(T):
    stack = []
    flag = 0
    
    paren = list(sys.stdin.readline().strip())
    
    for p in paren:
        if p == '(':
            stack.append(1)
        elif p == ')':
            if len(stack) == 0:
                flag = 1
                break
            else:
                stack.pop()

    if flag == 0 and len(stack) == 0:
        print("YES")
    else: print("NO")
