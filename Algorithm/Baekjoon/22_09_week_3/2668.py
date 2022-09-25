import sys
def input():
    return sys.stdin.readline().rstrip()

N = int(input())
lst = [0]
visited = [0]*101
for _ in range(N):
    lst.append(int(input()))
mx_set = []
for i in range(1, N+1):
    if visited[i]:
        continue
    
    lp = [i]
    while True:
        if lst[i] in lp:
            idx = lp.index(lst[i])
            mx_set += lp[idx:]
            break

        elif visited[lst[i]]:
            break
        
        else:
            i = lst[i]
            lp.append(i)
            visited[i] = 1
print(len(mx_set))
mx_set.sort()
for l in mx_set:
    print(l)