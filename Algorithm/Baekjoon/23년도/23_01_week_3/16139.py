import sys

def input():
    return sys.stdin.readline().rstrip()

S = input()

add_dict = {}

for i, s in enumerate(S):
    if add_dict.get(s):
        add_dict[s] += [add_dict[s][-1]]*(i - len(add_dict[s])) + [add_dict[s][-1]+1]
    else:
        add_dict[s] = [0]*i + [1]

N = int(input())

for _ in range(N):
    s, l, r = input().split()
    if not add_dict.get(s):
        print(0)
        continue
    l = int(l)
    r = int(r)
    length = len(add_dict[s])
    if length <= l:
        print(0)
    elif length <= r:
        if l != 0:
            print(add_dict[s][-1] - add_dict[s][l-1])
        else:
            print(add_dict[s][-1])
    else:
        if l != 0:
            print(add_dict[s][r] - add_dict[s][l-1])
        else:
            print(add_dict[s][r])



