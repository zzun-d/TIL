for _ in range(1, 11):
    tc = input()
    queue = list(map(int, input().split()))     # queue 생성
    i = 0                                       # 감소시킬 i

    while True:
        q = queue.pop(0) - ((i % 5) + 1)        # 사이클이 5이므로 5로 나눈 나머지 이용
        i += 1

        if q <= 0:                              # 뺀 값이 0 이하면, 0 append 하고 종료
            queue.append(0)
            break
        else:                                   # 아니면 q 값 append
            queue.append(q)

    print(f'#{tc}', *queue)
