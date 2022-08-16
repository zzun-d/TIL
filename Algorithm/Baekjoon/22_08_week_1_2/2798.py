n, m = map(int, input().split())
nums = list(map(int, input().split()))

sum_list = []

# 모든 경우의 수 탐색, 세 카드의 합이 m을 넘지 않는 경우 sum_list에 추가
for i in range(n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            if nums[i] + nums[j] + nums[k] <= m:
                sum_list.append(nums[i] + nums[j] + nums[k])

print(max(sum_list))