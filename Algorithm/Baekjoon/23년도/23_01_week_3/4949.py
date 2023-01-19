import sys

def input():
    return sys.stdin.readline().rstrip()

while True:
    S = input()
    if S == '.':
        break
    
    stack = []
    for s in S:
        if s == ')':
            if not stack or stack.pop() != '(':
                print('no')
                break
        elif s == ']':
            if not stack or stack.pop() != '[':
                print('no')
                break
        elif s in ['(', '[']:
            stack.append(s)
    else:
        if stack:
            print('no')
        else:
            print('yes')
            