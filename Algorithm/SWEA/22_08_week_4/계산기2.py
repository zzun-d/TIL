for t in range(1, 11):
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




