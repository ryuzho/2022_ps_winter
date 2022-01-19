# 괄호 제거
import sys
from itertools import combinations

form = list(sys.stdin.readline().strip())
index_stack = []
pairs_dict = {}
answer = []    

n = 0
for i in range(len(form)):
    if form[i] == '(':
        index_stack.append(i)
    elif form[i] == ')':
        pairs_dict[n] = [index_stack.pop(),i]
        n += 1

comb = []
for i in range(len(pairs_dict)):
    comb.extend(list(combinations(pairs_dict.keys(),i+1)))
        

for i in comb:
    temp = []
    index = []
    for j in i:
        index.extend(pairs_dict[j])
    for k in range(len(form)):
        if k not in index:
            temp.append(form[k])
    
    answer.append(''.join(temp))

answer = list(set(answer))
answer.sort()
for i in answer:
    print(i)
