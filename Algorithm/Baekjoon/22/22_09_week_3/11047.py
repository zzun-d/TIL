N, K = map(int, input().split())
coins = [int(input()) for _ in range(N)]
coins.sort(reverse=True)
result = 0
while K:
    for c in coins:
        result += K//c
        K = K%c

print(result)