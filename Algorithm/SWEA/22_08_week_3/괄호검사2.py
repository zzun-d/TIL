T = int(input())
for t in range(1, T+1):
    S = input()
    stack = []      # 여는 괄호 넣을 스택
    ans = 1         # ans default
    b_dict = {'}': '{', ']': '[', ')': '('}

    for s in S:
        if s in ['{', '[', '(']:                # s가 여는 괄호면 stack에 추가
            stack.append(s)

        # s가 닫는 괄호인데 stack에 마지막 요소가 해당 괄호의 여는 괄호가 아니면 ans = 0
        elif s in ['}', ']', ')']:
            if not stack or (stack and stack.pop() != b_dict[s]):
                ans = 0
                break

    if stack:       # stack이 존재하면 닫히지 않은 괄호 존재, ans = 0
        ans = 0
    print(f'#{t} {ans}')