N, K = map(int, input().split())
# lst = list(map(int, input().split()))
lst = [0] * (N+1)

for i, n in enumerate(map(int, input().split())):
    lst[i+1] = lst[i] + n

ans = []

for i in range(N-K+1):
    ans.append(lst[i+K] - lst[i])

print(max(ans))