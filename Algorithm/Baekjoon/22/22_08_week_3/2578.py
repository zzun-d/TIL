def search_ij(arr, n):    # 불러진 번호와 맞는 위치 탐색 함수
    for i in range(5):
        for j in range(5):
            if arr[i][j] == n:
                return i, j
bingo = [0] * 12          # 빙고 여부 체크 리스트
arr = [list(map(int, input().split())) for _ in range(5)]
call_arr = [list(map(int, input().split())) for _ in range(5)]
cnt = 0
for i in range(5):
    for j in range(5):
        call_num = call_arr[i][j]
        x, y = search_ij(arr, call_num)      # 불러진 번호 index
        if x == y:                           # 두 개가 같으면 \ 대각선 +1
            bingo[10] += 1
        if x + y == 4:                       # 두 번호 합해서 4면 / 대각선 +1
            bingo[11] += 1
        bingo[x] += 1                        # 행렬의 행에 해당하는 값 +1
        bingo[y+5] += 1                      # 열에 해당하는 값 +1

        for idx in range(12):                # 빙고 여부 확인
            if bingo[idx] >= 5:
                bingo[idx] = 0
                cnt += 1
        if cnt >= 3:                         # 3 빙고 이상이면 부른 횟수 저장 후 out
            ans = (i*5)+(j+1)
            break
    if cnt >= 3:
        break
print(ans)