import sys

t = int(input())
l = []
for _ in range(t):
    c = sys.stdin.readline().split()
    if c[0][:2] == 'pu':
        l.append(c[1])
    elif c[0][0] == 't':
        if l:
            print(int(l[-1]))
        else:
            print(-1)
    elif c[0][:2] == 'po':
        if l:
            print(int(l.pop()))
        else:
            print(-1)
    elif c[0][0] == 's':
        print(len(l))
    elif c[0][0] == 'e':
        if l:
            print(0)
        else:
            print(1)