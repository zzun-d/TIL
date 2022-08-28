for t in range(1):
    _ = input()
    prob = input()
    stack = []
    trans = ''
    
    for p in prob:

        if p not in ['+', '*']:
            trans += p

        else:
            if p == '+':
                while stack:
                    trans += stack.pop()
                stack.append(p)

            else:
                while stack and stack[-1] == '*':
                    trans += stack.pop()
                stack.append(p)

    while stack:
        trans += stack.pop()

    for p in trans:

        if p not in ['+', '*']:
            stack.append(p)
        
        else:
            if p == '*':
                stack.append(int(stack.pop()) * int(stack.pop()))
            else:
                stack.append(int(stack.pop()) + int(stack.pop()))
    
    print(f'#{t} {stack[0]}')




