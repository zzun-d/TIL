import sys, heapq

def input():
    return sys.stdin.readline().rstrip()

def distance(x1, y1, x2, y2):
    return int(((x1-x2)**2 + (y1 - y2)**2)**0.5)

def is_prime(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return 0
    if n < 2:
        return 0
    return 1

x1, y1, x2, y2 = map(int, input().split())
N = int(input())
nodes = [(x1, y1), (x2, y2)]
h_lst = [(0, 0)]
prime_lst = [-1]*8500
INF = sys.maxsize
dijk = [INF for _ in range(N+2)]
for _ in range(N):
    x, y = map(int, input().split())
    nodes.append((x, y))

ans = -1

while h_lst:
    d, i = heapq.heappop(h_lst)
    if d > dijk[i]:
        continue    
    
    if i == 1:
        ans = d
        break

    for j in range(N+2):
        x, y = nodes[j]
        tmp = distance(nodes[i][0], nodes[i][1], nodes[j][0], nodes[j][1])

        if prime_lst[tmp] < 0:
            prime_lst[tmp] = is_prime(tmp)
        if prime_lst[tmp] > 0 and dijk[j] > d+tmp:
            dijk[j] = d+tmp
            heapq.heappush(h_lst, (d+tmp, j))
            
print(ans)
