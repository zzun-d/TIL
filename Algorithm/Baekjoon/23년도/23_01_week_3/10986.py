N, M = map(int, input().split())

ans = 0
lst = [0]*(M+1)
prefix_sum = [0]*(N+1)

for i, n in enumerate(map(int, input().split()), start=1):
    p_num = prefix_sum[i-1] + n
    r_num = p_num % M
    lst[r_num] += 1
    prefix_sum[i] = p_num

for n in lst:
    ans += n*(n-1)/2

print(int(ans) + lst[0])