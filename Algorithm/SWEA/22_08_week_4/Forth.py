T = int(input())

for t in range(1, T+1):
    prob = input().split()
    stack = []

    for p in prob:
        if p not in ['+', '-', '*', '/', '.']:      # p가 숫자면 stack에 append
            stack.append(int(p))

        else:                                       # . 이면 stack 숫자 출력
            if p == '.':
                if len(stack) > 1:
                    print(f'#{t} error')
                else:
                    print(f'#{t}', stack[0])

            else:
                if len(stack) >= 2:                 # 연산자면서 연산할 숫자가 2개 이상 존재하면, 연산
                    n2 = stack.pop()
                    n1 = stack.pop()

                    if p == '+':
                        stack.append(n1 + n2)

                    elif p == '-':
                        stack.append(n1 - n2)

                    elif p == '*':
                        stack.append(n1 * n2)

                    elif p == '/':
                        stack.append(n1 // n2)

                else:                               # 연산할 숫자가 부족하면 error 출력, break
                    print(f'#{t} error')
                    break

