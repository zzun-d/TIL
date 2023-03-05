import sys

def input():
    return sys.stdin.readline().rstrip()

N = int(input())
nums = []
for _ in range(N):
    nums.append(int(input()))
nums.sort()

new_lst = [nums[i+1] - nums[i] for i in range(N-1)]
numbers = []
for num in new_lst:
    ans = set([1, num])
    for i in range(2, int(num**0.5) + 2):
        if num % i == 0:
            ans.add(i)
            ans.add(num//i)
    numbers.append(ans)

result = numbers[0]
for n_set in numbers:
    result &= n_set

print(*sorted(list(result))[1:])