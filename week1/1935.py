# 후위 표기식2

def calc(op, a, b):
    if op == '*':
        return a * b
    elif op == '/':
        return a / b
    elif op == '+':
        return a + b
    elif op == '-':
        return a - b

N = int(input())
postfix = list(input())
operator = ['+','-','*','/']
num = []
for _ in range(N):
    num.append(int(input()))

stack = []

for ch in postfix:
    if ch not in operator:
        stack.append(num[ord(ch)-65])
    else:
        b = stack.pop()
        a = stack.pop()
        stack.append(calc(ch, a, b))

print('{:.2f}'.format(stack[0]))

