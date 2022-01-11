# 덱

import sys
from collections import deque
deq = deque()

N = int(sys.stdin.readline())

for _ in range(N):
    comm = list(sys.stdin.readline().split())
    
    if comm[0] == 'push_front':
        deq.appendleft(comm[1])
    elif comm[0] == 'push_back':
        deq.append(comm[1])
    elif comm[0] == 'pop_front':
        if len(deq) == 0: print(-1)
        else: print(deq.popleft())
    elif comm[0] == 'pop_back':
        if len(deq) == 0: print(-1)
        else: print(deq.pop())
    elif comm[0] == 'size':
        print(len(deq))
    elif comm[0] == 'empty':
        if len(deq) == 0: print(1)
        else: print(0)
    elif comm[0] == 'front':
        if len(deq) == 0: print(-1)
        else: print(deq[0])
    elif comm[0] == 'back':
        if len(deq) == 0: print(-1)
        else: print(deq[-1])