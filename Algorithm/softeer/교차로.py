from collections import deque


def move(t, T):
    for now_t in range(T, t):
        l_lst = [len(cross['A']), len(cross['B']), len(cross['C']), len(cross['D'])]
        if all(l_lst) or not any(l_lst):
            return
        tmp = []
        for w1, w2 in zip('DABC', 'ABCD'):
            if len(cross[w1]) > 0 or len(cross[w2]) == 0:
                tmp.append(False)
            else:
                tmp.append(True)
        for i, w in enumerate('ABCD'):
            if tmp[i]:
                answer[cross[w].popleft()] = now_t
            
        


N = int(input())
answer = [-1]*N
cross = {
    'A':deque([]),
    'B':deque([]),
    'C':deque([]),
    'D':deque([]),
    }
T, w = input().split()
T = int(T)
cross[w].append(0)
for i in range(1, N):
    t, w = input().split()
    t = int(t)

    if t > T:
        move(t, T)
        T = t
    cross[w].append(i)
move(t + N, t)
for a in answer:
    print(a)    