T = int(input())

for tc in range(1, T+1):
    print(f'#{tc}', end=' ')
    num = input()
    bit = []
    for i in num:
        if ord(i) - 65 >= 0:
            n = ord(i)-55
            lst = []
            while n:
                lst.append(str(n%2))
                n = n//2
            bit += '0'*(4-len(lst))
            bit += lst[::-1]
        else:
            n = int(i)
            lst = []
            while n:
                lst.append(str(n % 2))
                n = n // 2
            bit += '0' * (4 - len(lst))
            bit += lst[::-1]

    for i in range(0, len(bit), 7):
        result = 0
        k = 0
        for j in range(min(len(bit)-i-1, 6), -1, -1):
            result += int(bit[i+k])*(2**(j))
            k += 1
        print(result, end=' ')

    print()