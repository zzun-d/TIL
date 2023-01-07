def dfs(n):         # 깊이 우선 탐색
    global ans

    if n >= N:                  # 종료 조건, 탐색하는 행이 최대 인덱스보다 커질 경우
        ans += 1                    # 퀸 놓는 경우의 수 + 1
        return
    
    for i in range(N):          # 모든 열 탐색
        if not visited[i]:          # 해당 열에 퀸이 없으면
            row[n] = i                  # 퀸을 놓음

            if cheak(n):                # 대각선에 퀸 없으면
                visited[i] = True           # visited 갱신
                dfs(n+1)                    # 다음 행으로 이동
                visited[i] = False          # for문의 남은 열 확인을 위한 visited 초기화

def cheak(x):       # 대각선 확인
    for i in range(x):      # 입력된 행 바로 위까지만 탐색
        if abs(row[i] - row[x]) == x-i:     # 기준 행의 퀸 위치와 위쪽 행의 퀸 위치의 열 차이가 행 차이만큼 나면 대각선 
            return False                        # 대각선에 퀸 존재!
    return True                         # 대각선에 퀸 없음!


N = int(input())
row = [0] * N           # 퀸의 위치(행: 인덱스, 열: 인덱스의 값)
ans = 0                 # 경우의 수
visited = [False] * N   # 열에 퀸 존재 확인 리스트

dfs(0)
print(ans)
