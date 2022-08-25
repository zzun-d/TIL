T = int(input())

for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    l = list(map(int, input().split()))
    l.sort()

    boong = [0] * (l[-1]+1)             # 붕어빵 초에 몇개씩 있을 수 있는지

    for i in range(1, l[-1] + 1):       # boong 변수 계산
        if i % M == 0:
            boong[i] = boong[i-1] + K
        else:
            boong[i] = boong[i-1]

    ans = 'Possible'                    # ans 디폴트 파서블

    for t in l:                         # 손님이 방문하는 시간 루프
        if not boong[t]:                    # 그 시간에 붕어빵 없으면 불가능 break
            ans = 'Impossible'
            break
        else:                               # 있으면 하나 팔고 재고 -1
            for i in range(t, (l[-1]+1)):
                boong[i] -= 1

    print(f'#{tc} {ans}')
