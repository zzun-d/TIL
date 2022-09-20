T = int(input())

for tc in range(1, T+1):
    n, prob = input().split()
    result = ''
    for i in prob:
        if ord(i) - 64 < 0:
            n = int(i)
            l = []
            while n:
                l.append(str(n%2))
                n = n//2
            rst = '0'*(4 - len(l)) + ''.join(l[::-1])
            result += rst
        else:
            n = ord(i) - 55
            l = []
            while n:
                l.append(str(n % 2))
                n = n // 2
            rst = '0' * (4 - len(l)) + ''.join(l[::-1])
            result += rst
    print(f'#{tc} {result}')