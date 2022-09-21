def f(k):
    global mx
    if k == K:
        n = int(''.join(list(map(str, N))))
        mx = max(mx, n)
    else:
        for i in range(len(N)-1):
            for j in range(i+1, len(N)):
                N[i], N[j] = N[j], N[i]
                f(k+1)
                N[i], N[j] = N[j], N[i]


        
T = int(input())
for tc in range(1, T+1):
    N, K = input().split()
    mx = int(N)
    N = list(map(int, list(N)))
    K = int(K)
    f(0)
    print(f'#{tc} {mx}')
