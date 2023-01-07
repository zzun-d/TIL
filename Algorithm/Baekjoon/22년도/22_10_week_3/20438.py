import sys


def input():
    return sys.stdin.readline().rstrip()


N, K, Q, M = map(int, input().split())
sleep_lst = list(map(int, input().split()))
sleep_set = set(sleep_lst)
call_lst = list(map(int, input().split()))

students = [1] * (N+4)
for c in call_lst:
    if sleep_set.intersection(set([c])):
        continue
    ori_c = c
    while c <= N+3:
        students[c] = 0
        c += ori_c
for s in sleep_lst:
    students[s] = 1

for _ in range(M):
    S, E = map(int, input().split())
    print(sum(students[S:E+1]))

