# 요세푸스 문제

N, K = map(int, input().split())
arr = [ str(i) for i in range(1,N+1)]
result = []
index = K-1

while len(result) != N:
    if index >= len(arr):
        index %= len(arr)

    result.append(arr.pop(index))
    index += K-1


print('<'+', '.join(result)+'>')

