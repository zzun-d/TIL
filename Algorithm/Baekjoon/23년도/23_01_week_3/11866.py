from collections import deque

N, K = map(int, input().split())

lst = deque([str(i) for i in range(1, N+1)])
ans = []

while lst:
    for _ in range(K-1):
        lst.append(lst.popleft())
    ans.append(lst.popleft())

print(f'<{", ".join(ans)}>')