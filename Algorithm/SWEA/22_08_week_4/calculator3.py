
for t in range(1, 11):
    _ = input()
    prob = input()
    stack_num = []
    stack_cal = []
    hu_we = ''
    for p in prob:
        if p not in ['+', '*', ')', '(']:
            stack_num.append(int(p))

            if stack_cal and stack_cal[-1] == '*':
                n1 = stack_num.pop()
                n2 = stack_num.pop()
                c = stack_cal.pop()
                stack_num.append(n1 * n2)

        else:

            if p == ')':
                c = stack_cal.pop()
                while c != '(':
                    n1 = stack_num.pop()
                    n2 = stack_num.pop()
                    stack_num.append(n1 + n2)
                    c = stack_cal.pop()

                if stack_cal and stack_cal[-1] == '*':
                    n1 = stack_num.pop()
                    n2 = stack_num.pop()
                    c = stack_cal.pop()
                    stack_num.append(n1 * n2)

            else:
                stack_cal.append(p)

    print(f'#{t} {stack_num[0]}')







