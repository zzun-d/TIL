def dfs(arr, x, y=0):
    cnt = 0
    ans = x
    while y < 99:                               # 끝에 도달 할 때 까지 루프
        if x + 1 < 100 and arr[y][x+1]:             # 오른쪽에 길이 있으면 없어질 때까지 이동
            while x + 1 < 100 and arr[y][x+1]:
                cnt += 1
                x += 1

        elif x - 1 >= 0 and arr[y][x-1]:            # 왼쪽에 길이 있으면 없어질 때까지 이동
            while x - 1 >= 0 and arr[y][x-1]:
                cnt += 1
                x -= 1
        cnt += 1                                    # 왼쪽 혹은 오른쪽으로 이동이 끝난 후 아래로 한칸 이동
        y += 1
    return ans, cnt                             # 출발지점, 이동거리 반환

for _ in range(10):
    t = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]
    step = 10000                    # 초기 step(max값)

    for i in range(100):
        if ladder[0][i]:                # 시작지점이 1이면
            ans, cnt = dfs(ladder, i, 0)    # dfs 탐색
            if step > cnt:                  # step 값보다 짧은 이동거리면 갱신
                result = ans
                step = cnt
    print(f'#{t} {result}')

