import sys

def input():
    return sys.stdin.readline().rstrip()

N, atk = map(int, input().split())
mx_dam = 0
dam = 0
for _ in range(N):
    t, a, h = map(int, input().split())
    if t==1:
        if h%atk == 0:
            dam += a*(h//atk - 1)
        else:
            dam += a*(h//atk)
        mx_dam = max(dam, mx_dam)
    
    else:
        dam = max(0, dam-h)
        atk += a
print(mx_dam+1)