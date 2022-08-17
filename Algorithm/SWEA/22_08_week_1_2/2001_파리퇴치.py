T = int(input())
for i in range(T):
    N, M = list(map(int, input().split()))
    fly_map = [list(map(int, input().split())) for j in range(N)]
    kill_counts = []
    for j in range((N-M+1)):
        for k in range(N-M+1):
            kill_count = 0
            for l in range(M):
                kill_count += sum(fly_map[j+l][k:k+M])
            kill_counts.append(kill_count)
    print(f'#{i+1} {max(kill_counts)}')
        