import sys
from collections import deque
def input():
    return sys.stdin.readline().rstrip()

N = int(input())
q = deque()
for _ in range(N):
    c = input().split()
    
    if c[0] == 'push':
        q.append(c[1])

    elif c[0] == 'pop':
        if q:
            print(q.popleft())
        else:
            print(-1)
    elif c[0] == 'size':
        print(len(q))
    elif c[0] == 'empty':
        if q:
            print(0)
        else:
            print(1)
    elif c[0] == 'front':
        if q:
            print(q[0])
        else:
            print(-1)
    else:
        if q:
            print(q[-1])
        else:
            print(-1)

