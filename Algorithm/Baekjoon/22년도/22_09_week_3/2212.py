N = int(input())
K = int(input())
lst = sorted(list(set(map(int, input().split()))))
gap = []
for i in range(1, len(lst)):
    gap.append(lst[i] - lst[i-1])
gap.sort()
for _ in range(1, K):
    if gap:
        gap.pop()
print(sum(gap))

