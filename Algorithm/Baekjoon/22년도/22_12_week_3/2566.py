r = c = mx = 0

for i in range(9):
    lst = list(map(int ,input().split()))
    for j in range(9):
        if lst[j] > mx:
            mx = lst[j]
            r = i
            c = j
print(mx)
print(r+1, c+1)