N = int(input())

ans = ['*'*N for _ in range(N)]
n = 1
cnt = 1
while N > n:
    for i in range(n, N, n*3):
        for j in range(n):
            ans[i+j] = (ans[i+j][:n] + ' '*n + ans[i+j][:n]) * round(N / 3**cnt)
    cnt += 1
    n *= 3
for a in ans:
    print(a)
