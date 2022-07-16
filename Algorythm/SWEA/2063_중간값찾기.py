N = int(input())
nums = list(map(int, input().split()))
nums.sort()
print(nums[N//2])