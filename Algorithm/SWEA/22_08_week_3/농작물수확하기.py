def sum(lst):
    ans = 0
    for l in lst:
        ans += l
    return ans

T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    ans = 0
    for i in range(N):
        if i <= N//2:                                   # 가로 최대 길이까지
            ans += sum(arr[i][N//2-i:N//2-i+(i*2+1)])
        else:                                           # 나머지 중 가운대만
            j = i - N//2
            ans += sum(arr[i][j:N-j])
    print(f'#{t} {ans}')


