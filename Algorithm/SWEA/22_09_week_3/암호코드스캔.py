CODE = {
    '0001101':0,
    '0011001':1,
    '0010011':2,
    '0111101':3,
    '0100011':4,
    '0110001':5,
    '0101111':6,
    '0111011':7,
    '0110111':8,
    '0001011':9,
    }

T = int(input())
for tc in range(1, T+1):
    R, C = map(int, input().split())
    arr = [input() for _ in range(R)]
    f_arr = arr[0]
    for i in arr[0]:
        if i != '0':
            f_arr = ''
            break

    for i in range(R):
        if arr[i] != f_arr and len(set(arr[i])) > 1:
            f_arr = arr[i]
            codes = []
            code = ''
            for j in range(C):
                if arr[i][j] != '0':
                    n = arr[i][j]
                    if n in 'ABCDEF':
                        n = ord(n) - 55
                    else:
                        n = int(n)
                    lst = ''
                    while n:
                        lst += str(n%2)
                        n = n//2
                    code += '0'*(4-len(lst)) + lst[::-1]
                    last_j = j
                    continue
                else:
                    if code:
                        codes.append(code)
                        code = ''
            RESULT = 0
            for cc in codes:
                k = len(cc)//56
                for j in range(-1, -len(cc), -1):
                    if cc[j] == '1':
                        cc = cc[j-(55*k):j+1]
                        if len(cc) > 56:
                            cc = cc[-56:]
                        else:
                            cc = '0'*(56-len(cc)) + cc

                        break

                rst = ''
                for j in range(0, 56*k, k):
                    rst += cc[j]

                result = []
                for j in range(0, 56, 7):
                    result.append(CODE[rst[j:j+7]])
                R = 0
                for j in range(8):
                    if not j%2:
                        R += 3*result[j]
                    else:
                        R += result[j]
                if not R%10:
                    RESULT += sum(result)
            break
    print(f'#{tc} {RESULT}')