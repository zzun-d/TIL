from collections import deque


A, B = map(int, input().split())

greedy ={}
greedy[A] = 1
lst = deque([A*2 , A*10 +1])
cnt = 1
while lst:
    cnt += 1
    
    for _ in range(len(lst)):
        l = lst.popleft()
        if not greedy.get(l) and l <= B:
            greedy[l] = cnt
            lst += [l*2, l*10 +1]

if greedy.get(B):
    print(greedy[B])
else:
    print(-1)