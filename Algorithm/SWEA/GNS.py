T = int(input())
for t in range(1, T+1):
    _, N = input().split()
    N = int(N)
    lst = input().split()
    num_list = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']
    ONE = TWO = THR = FOR = FIV = SIX = SVN = EGT = NIN = ZRO = 0
    for n in lst:
        if n[0] == 'Z':
            ZRO += 1
        elif n[0] == 'O':
            ONE += 1
        elif n[0] == 'T':
            if n[1] == 'W':
                TWO += 1
            else:
                THR += 1
        elif n[0] == 'F':
            if n[1] == 'O':
                FOR += 1
            else:
                FIV += 1
        elif n[0] == 'S':
            if n[1] == 'I':
                SIX += 1
            else:
                SVN += 1
        elif n[0] == 'E':
            EGT += 1
        else:
            NIN += 1
    cnt_lst = [ZRO, ONE, TWO, THR, FOR, FIV, SIX, SVN, EGT, NIN]
    ans = []
    for i in range(10):
        ans += [num_list[i]] * cnt_lst[i]
    print(f'#{t}')
    print(*ans)

