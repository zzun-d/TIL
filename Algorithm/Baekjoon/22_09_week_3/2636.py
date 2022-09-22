from collections import deque

# 바깥과 연결된 공기를 arr에 2로 바꾸는 함수
def air(s):
    queue = deque([(s, s)])
    arr[s][s] = 2               # 반복횟수 줄이기 위한 s변수 도입
    visited = [[0]*C for _ in range(R)]
    while queue:
        i, j = queue.popleft()
        for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            ni = i + di
            nj = j + dj

            if 0+s <= ni < R-s and 0+s <= nj < C-s and not visited[ni][nj]:
                visited[ni][nj] = 1
                if arr[ni][nj] != 1:            # 치즈가 아니면서 바깥과 연결된 공기면 2로 변환
                    arr[ni][nj] = 2
                    queue.append((ni, nj))      # queue에 추가
                elif arr[ni][nj] == 1:          # 치즈이면,
                    cheese.append((ni, nj))     # 녹을 치즈 목록에 좌표 추가

# 치즈 녹이는 함수
def melting():
    for i, j in cheese:
        arr[i][j] = 0

R, C = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(R)]
cheese = True
S = 0
c_history = []          # 녹은 치즈 갯수 저장 리스트
while cheese:
    cheese = []
    air(S)                      # 바깥공기 2로 변환
    S += 1                      # 영역 좁히기
    melting()                   # 치즈 녹이기
    c_history.append(len(cheese))       # 녹은 치즈 기록

print(len(c_history) - 1)       # 치즈 녹인 횟수(c_history의 마지막은 항상 0이므로 갯수 하나 뺌)
print(c_history[-2])            # 기록에 남은 마지막 치즈 갯수(위랑 마찬가지)
