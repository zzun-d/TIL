T = int(input())

for tc in range(1, T+1):
    num = float(input())
    t = 0
    rst = ''

    i = 1
    while num and t < 13:
        if num >= 2**(-i):
            rst += '1'
            num -= 2 ** (-i)
        else:
            rst += '0'
        t += 1
        i += 1

    if t >= 13:
        print(f'#{tc} overflow')
    else:
        print(f'#{tc} {rst}')

