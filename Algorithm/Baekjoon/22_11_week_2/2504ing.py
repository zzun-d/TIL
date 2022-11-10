prob = input()
stack = []
ans = 0
tmp = 1
for p in prob:
    if p == '(':
        stack.append(p)
        tmp *= 2
    elif p == '[':
        stack.append(p)
        tmp *= 3
    elif p == ')':
        
        if stack[-1] == '(':
            ans += tmp
        stack.pop()
        tmp //= 2

    elif p == ']':
        
        if stack[-1] == '[':   
            ans += tmp
        tmp //= 3
        stack.pop()

print(stack)
print(ans, tmp)
if stack:
    print(0)
else:
    print(ans)