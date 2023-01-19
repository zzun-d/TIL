import sys

def input():
    return sys.stdin.readline().rstrip()

N, M, K = map(int, input().split())

# arr_B = [[0]*M for _ in range(N)]
# arr_W = [[0]*M for _ in range(N)]
prefix_B = [[0]*(M+1) for _ in range(N+1)]
prefix_W = [[0]*(M+1) for _ in range(N+1)]

for i in range(N):
    colors = input()
    for j in range(M):
        if (i+j)%2 == 0:
            if colors[j] == 'W':
                prefix_W[i+1][j+1] = prefix_W[i+1][j] + prefix_W[i][j+1] - prefix_W[i][j]
                prefix_B[i+1][j+1] = prefix_B[i+1][j] + prefix_B[i][j+1] - prefix_B[i][j] + 1
            else:
                prefix_W[i+1][j+1] = prefix_W[i+1][j] + prefix_W[i][j+1] - prefix_W[i][j] + 1
                prefix_B[i+1][j+1] = prefix_B[i+1][j] + prefix_B[i][j+1] - prefix_B[i][j] 
        else:
            if colors[j] == 'W':
                prefix_W[i+1][j+1] = prefix_W[i+1][j] + prefix_W[i][j+1] - prefix_W[i][j] + 1
                prefix_B[i+1][j+1] = prefix_B[i+1][j] + prefix_B[i][j+1] - prefix_B[i][j]
            else:
                prefix_W[i+1][j+1] = prefix_W[i+1][j] + prefix_W[i][j+1] - prefix_W[i][j] 
                prefix_B[i+1][j+1] = prefix_B[i+1][j] + prefix_B[i][j+1] - prefix_B[i][j] + 1

ans = K**2//2

for i in range(K, N+1):
    if ans == 0:
        break
    for j in range(K, M+1):
        ps_w = prefix_W[i][j] - prefix_W[i][j-K] - prefix_W[i-K][j] + prefix_W[i-K][j-K]
        ps_b = prefix_B[i][j] - prefix_B[i][j-K] - prefix_B[i-K][j] + prefix_B[i-K][j-K]

        ans = min(ans, ps_w, ps_b)

print(ans)
