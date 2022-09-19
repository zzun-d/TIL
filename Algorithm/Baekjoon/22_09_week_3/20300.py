N = int(input())
lst = list(map(int, input().split()))

lst.sort()
result = 0
if N%2:
    result = lst.pop()

for i in range(N//2):
    result = max(lst[i] + lst[-1-i], result)
print(result)