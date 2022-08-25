T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())

    # 피자 번호와 치즈양을 튜플로 묶어서 저장
    pizza = [(i, c) for i, c in enumerate(list(map(int, input().split())), start=1)]
    baking = []
    for i in range(N):                  # 화덕 용량만큼 피자 넣음
        baking.append(pizza.pop(0))

    while baking:                                   # 구워질 피자가 있으면 계속 구움
        now_p = (baking[0][0], baking[0][1]//2)     # 한바퀴 돈 피자 치즈양 갱신
        baking.pop(0)                               # 리스트에서 제거

        if now_p[1] == 0:                           # 피자의 치즈가 0 이면서,
            if pizza:                                   # 넣을 피자가 남았으면
                baking.append(pizza.pop(0))                 # 화덕에 피자 넣음
        else:                                       # 피자의 치즈가 남았으면 맨뒤로 다시 추가
            baking.append(now_p)


    print(f'#{tc} {now_p[0]}')