code = {
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
    for i in range(4, R-4):
        if '1' in arr[i]:
            for j in range(C):
                if arr[i][j] == '1':
                    while arr[i][j+55] == '0':
                        j -= 1
                    s_i = j
                    break
            P = []
            for j in range(s_i, s_i+56, 7):
                P.append(arr[i][j:j+7])
            result = 0
            sm = 0
            for j in range(8):
                if j%2:
                    sm += code[P[j]]

                else:
                    sm += 3*code[P[j]]
                result += code[P[j]]
            if sm%10:
                print(f'#{tc} 0')

            else:
                print(f'#{tc} {result}')

            break