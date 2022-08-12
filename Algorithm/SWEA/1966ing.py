import sys
def input():
    return sys.stdin.readline().rstrip()

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    info = list(map(int, input().split()))
    s_info = sorted(info)
    prin = None
    i = 0
    cnt = 0
    while prin == M:
        if info[i%len(info)] == s_info[-1]:
            s_info.pop()
            info = info[:i%len(info)] + info[i%len(info)+1:]
            prin = i
            cnt += 1
        else:
            i += 1
    print(cnt)