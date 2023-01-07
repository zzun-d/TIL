import sys
from collections import deque
def input():
    return sys.stdin.readline().rstrip()

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    info = deque(map(int, input().split()))
    i_info = deque((i, info[i]) for i in range(N))
    s_info = sorted(info)
    prin = None
    cnt = 0
    while prin != M:
        if i_info[0][1] != s_info[-1]:
            i_info.append(i_info.popleft())
        else:
            cnt += 1
            prin = i_info.popleft()[0]
            s_info.pop()
    print(cnt)