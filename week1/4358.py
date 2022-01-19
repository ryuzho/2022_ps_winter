# 생태학
import sys
input = sys.stdin.readline

dict = {}
n = 0
while True:
    tree = input().strip()
    if not tree:
        break
    if tree in dict:
        dict[tree] += 1
    else:
        dict[tree] = 1
    n += 1

tree_list = list(dict.keys())
tree_list.sort()

for tree in tree_list:
    print('{} {:.4f}'.format(tree,100*(dict[tree]/n)))
    