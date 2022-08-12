import sys
from collections import deque
def input():
    return sys.stdin.readline().rstrip()


N = int(input())
nums = deque(map(int, input().split()))
bal_num = [(i, nums[i-1]) for i in range(1, N+1)]
ans = deque()
boom = 0

for i in range(1, N):
    print(i, boom)
    print(bal_num)

    idx, mv = bal_num.pop(boom)
    if boom >= 0:
        bal_num = bal_num[boom:] + bal_num[:boom]
    else:
        bal_num = bal_num[boom+1:] + bal_num[:boom+1]
    ans.append(idx)
    if mv > 0:
        mv -= 1
        boom = mv % (N-i)
    else:
        boom = mv % -(N-i)
ans.append(bal_num[0][0])
print(*ans)

    
