K, N = map(int, input().split())
lst = [int(input()) for _ in range(K)]
mn = max(lst)
lef = 0
rig = mn * 2

while True:
    mid = (lef+rig)//2
    sm = 0
    i = 0
    if lef > rig:
        break

    while sm < N and i < K:
        sm += lst[i] // mid
        i += 1
    
    if sm < N:
        rig = mid - 1
    
    else:
        lef = mid + 1

print(rig)
