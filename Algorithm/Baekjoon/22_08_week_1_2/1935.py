N = int(input())
S = list(input())
S.reverse()

alp = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
num = []
alp_num = {alp[i]:int(input()) for i in range(N)}
while S:
    if S[-1] in ['-','+','*','/']:
        if S[-1] == '-':
            p1 = num.pop()
            p2 = num.pop()
            num.append(p2 - p1)
        elif S[-1] == '+':
            p1 = num.pop()
            p2 = num.pop()
            num.append(p2 + p1)
        elif S[-1] == '*':
            p1 = num.pop()
            p2 = num.pop()
            num.append(p2 * p1)
        else:
            p1 = num.pop()
            p2 = num.pop()
            num.append(p2 / p1)
        S.pop()
    else:
        num.append(alp_num[S.pop()])
print(f'{num[0]:.2f}')