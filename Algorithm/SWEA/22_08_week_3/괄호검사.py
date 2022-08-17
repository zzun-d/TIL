T = int(input())

for t in range(1, T+1):
    stack = []      # 여는 괄호 넣을 스택
    S = input()
    ans = 1         # ans default는 1
    for s in S:
        if s == '(':        # 여는 괄호면 스택에 포함
            stack.append(s)
        else:
            if stack:           # 여는 괄호가 아니고, 스택이 존재하면 pop
                stack.pop()
            else:               # 스택이 존재하지 않으면 잘못된 괄호열
                ans = 0
                break
    if stack:   # 스택에 여는 괄호가 남아있으면 잘못된 괄호열
        ans = 0
    print(f'#{t} {ans}')

