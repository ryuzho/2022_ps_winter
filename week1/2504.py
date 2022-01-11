# 괄호의 값
import sys
paren = sys.stdin.readline().strip()
stack = []
paren_list = ['(',')','[',']']

for i in paren:
    if len(stack)>1 and stack[-1] not in paren_list and stack[-2] not in paren_list:
        num1 = stack.pop()
        num2 = stack.pop()
        stack.append(num1+num2)

    if i == '(':
        stack.append('(')
    elif i == ')':
        if len(stack)!= 0 and stack[-1] == '(':
            stack.pop()
            stack.append(2)
        elif len(stack)>1 and stack[-1] not in paren_list and stack[-2] == '(':
            num = stack.pop()
            stack.pop()
            stack.append(num*2)
        else:
            print(0)
            break

    if i == '[':
        stack.append('[')
    elif i == ']':
        if len(stack)!=0 and stack[-1] == '[':
            stack.pop()
            stack.append(3)
        elif len(stack)>1 and stack[-1] not in paren_list and stack[-2] == '[':
            num = stack.pop()
            stack.pop()
            stack.append(num*3)
        else:
            print(0)
            break
    
else: 
    for i in stack:
        if i in paren_list:
            print(0)
            break
    else: print(sum(stack))
