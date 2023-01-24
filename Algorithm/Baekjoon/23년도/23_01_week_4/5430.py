from collections import deque

T = int(input())

for _ in range(T):
    P = input()
    N = int(input())
    lst = deque(input()[1:-1].split(','))
    R_cnt = 0
    for p in P:
        if p == 'R':
            R_cnt += 1
        elif p == 'D' and N > 0:
            N -= 1
            if R_cnt % 2 == 0:
                lst.popleft()
            else:
                lst.pop()
        else:
            print('error')
            break
    else:
        if R_cnt % 2 == 1:
            lst.reverse()
        ans = ','.join(lst)
        print('[' + ans + ']')