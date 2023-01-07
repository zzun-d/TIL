N = int(input())
lst = list(map(int, input().split()))
for i in range(1, N):
    lst[i] = max(lst[i], lst[i-1] + lst[i])
        
print(max(lst))