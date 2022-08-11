N = int(input())

idx = [i for i in range(1, N+1)]
nums = list(map(int, input().split()))
ans = []
now = 0
for i, num in enumerate(nums):
    if N-i < now + num or 0 > now + num: