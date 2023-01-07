N, L = map(int, input().split())

t = 0                   # 누적 시간 변수
before_D = 0            # 신호등 사이 거리 변수
sign = [list(map(int, input().split())) for _ in range(N)]      # 신호등 정보 리스트
while sign:             # 신호등 정보가 존재하면 루프
    D, R, G = sign.pop(0)
    t += D - before_D       # 이동 거리만큼 시간 +
    before_D = D            # 이동거리 계산용 이전 신호등 위치 저장

    if t % (R+G) < R:       # 시간을 신호등 사이클로 나눈 나머지를 이용하여 빨간불이면,
        t += R - (t % (R+G))    # 빨간불 남은 지속시간 시간에 더해줌

    if not sign:            # 신호등 정보가 더 이상 존재하지 않으면,
        t += L - D              # 마지막 신호등 위치에서 도착지까지 이동시간 +

    
print(t)