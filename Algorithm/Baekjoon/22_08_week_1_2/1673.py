while True:
    try:
        n, k = map(int, input().split())
        cnt = 0   # 먹은 치킨 수
        ticket = 0   # 가지고 있는 티켓 수
        while True:
            cnt += n   # 치킨 먹은 수 업데이트
            ticket += n   # 먹은만큼 티켓 변환
            n = ticket // k   # 티켓으로 먹을 수 있는 치킨 수
            ticket = ticket % k   # 남은 티켓 수
            if n == 0:
                break
        print(cnt)
    except EOFError:
        break