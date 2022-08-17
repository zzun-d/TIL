T = int(input())
for t in range(1, T+1):
    arr = [list(input()) for _ in range(5)]
    ans = ''
    i = j = 0
    while j < 15:
        if len(arr[i%5]) > j:
            ans += arr[i%5][j]
        i += 1
        if i%5==0:
            j+=1
    print(f'#{t} {ans}')

