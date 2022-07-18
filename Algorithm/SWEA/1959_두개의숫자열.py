T = int(input())
for i in range(T):
    n, m = list(map(int, input().split()))
    Ai = list(map(int, input().split()))
    Bi = list(map(int, input().split()))
    answer = []
    if n < m:
        for j in range(m-n+1):
            num = 0
            for k in range(n):
                num += Ai[k] * Bi[j+k]
            answer.append(num)
        print(f'#{i+1} {max(answer)}')
    else:
        for j in range(n-m+1):
            num = 0
            for k in range(m):
                num += Bi[k] * Ai[j+k]
            answer.append(num)
        print(f'#{i+1} {max(answer)}')