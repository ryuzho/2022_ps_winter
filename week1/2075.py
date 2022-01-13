# N번째 큰 수
import sys
import heapq

N = int(input())
heap = []

for _ in range(N):
    line_input = map(int, sys.stdin.readline().split())
    for num in line_input:
        heapq.heappush(heap,num)
        if len(heap) > N:
            heapq.heappop(heap)
        
        
print(heap[0])
