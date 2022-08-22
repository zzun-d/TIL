T = int(input())

for t in range(1, T+1):
    prob = input()
    stack_num = []
    stack_cal = []
    f_cal = False

    for p in prob:

        if p not in ['+', '*']:
            stack_num.append(p)

            if f_cal:




        else:
            stack_cal.append(p)


