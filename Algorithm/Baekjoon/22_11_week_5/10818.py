N = int(input())
nums = map(int, input().split())
mx = -1000000
mn = 1000000
for num in nums:
    if num > mx:
        mx = num
    if num < mn:
        mn = num

print(mn, mx)
