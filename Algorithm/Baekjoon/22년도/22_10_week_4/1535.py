def f(n, hp_sm, happy_sm):
    global mx

    if hp_sm >= 100:                # 사용 체력이 100 이상이면 종료
        return

    if n >= N:                      # 모든 사람의 경우의 수까지 확인했으면 mx 갱신
        mx = max(mx, happy_sm)
        return

    f(n+1, hp_sm + hp[n], happy_sm + happy[n])  # 인사 하기
    f(n+1, hp_sm, happy_sm)                     # 인사 안하기    

N = int(input())
hp = list(map(int, input().split()))
happy = list(map(int, input().split()))
mx = 0                                          # 기쁨 최댓값
f(0, 0, 0)
print(mx)