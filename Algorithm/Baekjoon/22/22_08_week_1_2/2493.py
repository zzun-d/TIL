N = int(input())
heights = list(map(int, input().split()))
ans = [0] * N
tower = []
for i in range(N-1, -1, -1):
    while tower and heights[tower[-1]] <= heights[i]:
        ans[tower.pop()] += i+1
    tower.append(i)
print(*ans)