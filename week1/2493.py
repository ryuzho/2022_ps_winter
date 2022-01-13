# 탑
import sys

N = int(input())
towers = list(map(int, sys.stdin.readline().split()))

result = []
stack = [[0,0]]

for i in range(len(towers)):

        if stack[-1][1] < towers[i]:
            while stack and stack[-1][1] < towers[i]:
                stack.pop()
            if len(stack) == 0:
                result.append(0)
            else:
                result.append(stack[-1][0]+1)
            stack.append([i, towers[i]])
        else:
            result.append(stack[-1][0]+1)
            stack.append([i, towers[i]])

print(' '.join(map(str, result)))


