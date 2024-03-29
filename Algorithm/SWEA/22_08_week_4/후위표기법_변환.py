T = int(input())

for t in range(1, T+1):
    prob = input()
    stack = []
    ans = ''

    for p in prob:

        if p not in ['+', '*']:
            ans += p

        else:
            if p == '+':
                while stack:
                    ans += stack.pop()
                stack.append(p)

            else:
                while stack and stack[-1] == '*':
                    ans += stack.pop()
                stack.append(p)

    while stack:
        ans += stack.pop()

    print(f'#{t} {ans}')

