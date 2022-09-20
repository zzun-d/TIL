passward = {'001101':0, '010011':1, '111011':2, '110001':3, '100011':4, '110111':5, '001011':6, '111101':7, '011001':8, '101111':9}


T = int(input())

for tc in range(1, T+1):
    nums = input()
    lst = []
    for i in nums:
        if ord(i) - 64 < 0:
            n = int(i)
            l = []
            while n:
                l.append(str(n%2))
                n = n//2
            lst += '0'*(4-len(l))
            lst += l[::-1]
        else:
            n = ord(i) - 55
            l = []
            while n:
                l.append(str(n%2))
                n = n//2
            lst += '0' * (4 - len(l))
            lst += l[::-1]
    i = 0
    rst = []
    while True:
        ward = ''.join(lst[i:i+6])

        while passward.get(ward) != None:
            rst.append(passward[ward])
            i += 6
            ward = ''.join(lst[i:i+6])

        if rst:
            break
        i += 1
    print(f'#{tc}', *rst)



