import sys

def input():
    return sys.stdin.readline().rstrip()

T = int(input())

for _ in range(T):
    N = int(input())
    cloths = {}
    ans = 1
    for _ in range(N):
        name, ctgr = input().split()
        if cloths.get(ctgr):
            cloths[ctgr].append(name)
        else:
            cloths[ctgr] = [name]
    for k in cloths.keys():
        ans *= len(cloths[k]) + 1
    print(ans - 1)